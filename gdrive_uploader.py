#!/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
import os
import time

from apiclient import errors as api_errors, http as api_http


def get_or_create_folder(service, folder_name):
    """
    Search for specific folder name in target account and create one if not exist
    then return folder id
    :param service: gdrive api service
    :param folder_name: string of target folder name
    :return:
        folder id in gdrive
    """
    folder_id = None
    # search for folder name
    q = 'title="{}" and mimeType="application/vnd.google-apps.folder"'.format(folder_name)
    try:
        files = service.files().list(q=q).execute()
        items = files.get('items', [])
        if items:
            folder_id = items[0]['id']
        else:
            body = {
                "title": folder_name,
                "mimeType": "application/vnd.google-apps.folder"
            }
            request = service.files().insert(body=body).execute()
            folder_id = request['id']
    except api_errors.HttpError, error:
        print('An error occurred: %s' % error)

    return folder_id


def upload_file(service, input_file, output_name=None, folder_name=None):
    """
    Upload file to gdrive using MediaFileUpload that support large file upload and resumable
    Display upload speed and progress when call this function
    :param service: gdrive api service
    :param input_file: full path or relative path to source file to upload
    :param output_name: target filename on gdrive, if none, use same name as source filename
    :param folder_name: target folder name to store file. this folder will create under root folder on gdrive
    :return:
        File instance from google api or None if error occur
    """
    filename, ext = os.path.splitext(input_file)
    mime_type = None
    if not ext:
        mime_type = 'application/octet-stream'
    media = api_http.MediaFileUpload(input_file, mimetype=mime_type, resumable=True)

    if not output_name:
        output_name = os.path.basename(input_file)
    body = {
        'title': output_name,
    }
    if folder_name:
        parent_id = get_or_create_folder(service, folder_name)
        body['parents'] = [{'id': parent_id}]

    request = service.files().insert(media_body=media, body=body)
    response = None

    start_time = time.time()

    try:
        # Loop to show upload progress and speed
        while response is None:
            status, response = request.next_chunk()
            if status:
                upload_speed = int(status.resumable_progress / (1024*(time.time() - start_time)))
                print("Uploaded {}% - ({:,}/{:,}) - Avg {:,} Kps".format(
                    int(status.progress() * 100),
                    status.resumable_progress,
                    status.total_size,
                    upload_speed), end='\r')
        print()
        print("Upload Complete! -- {:,} seconds".format(time.time() - start_time))
        return file
    except api_errors.HttpError, error:
        print('An error occur: %s' % error)
        return None
