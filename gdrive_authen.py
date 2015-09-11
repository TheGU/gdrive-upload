#!/usr/bin/python
from __future__ import absolute_import
import os
import sys
import httplib2

from apiclient import discovery
from oauth2client import client as oauth_client, tools as oauth_tools, file as oauth_file

# Set scope to allow all action
SCOPES = 'https://www.googleapis.com/auth/drive'
# Google client secret : https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'GDrive Uploader'


def get_credentials(flags):
    """
    Read token file from ./.credentials/drive-access.json or create one if not exist.
    Creation process will ask user to copy url that display on screen to get allow token.
    :param flags : oauth2client flags. read more [https://goo.gl/dL03yF]
    :return:
        Oauth2 credential ready for use in client
    """
    home_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-access.json')

    store = oauth_file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:

        flow = oauth_client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if not flags:
            # if function call with non-implement flags, force to use default flags for oauth2client api
            import argparse
            parser = argparse.ArgumentParser(parents=[oauth_tools.argparser])
            flags = parser.parse_args()            
        credentials = oauth_tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)

    return credentials


def create_gdrive_service(flags=None):
    """
    Create Google API Service for Google Drive
    :return:
        A service for api call
    """
    credentials = get_credentials(flags)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
    return service
