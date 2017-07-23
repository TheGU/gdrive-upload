#!/usr/bin/python
from __future__ import absolute_import

from oauth2client import tools as oauth_tools

from gdrive_upload.gdrive_authen import create_gdrive_service
from gdrive_upload.gdrive_uploader import upload_file

try:
    import argparse
except ImportError:
    argparse = None

if argparse:
    parser = argparse.ArgumentParser(parents=[oauth_tools.argparser])
    parser.add_argument('-s', '--serviceaccount', help='Set to use service account intead of normal user account',
                        action="store_true")
    parser.add_argument('-i', '--inputfile', required=True, help='Input full path filename')
    parser.add_argument('-o', '--outputfile', help='Specific output name or not set for use same name as input')
    parser.add_argument('-f', '--foldername', help='specific folder name to upload to')
    flags = parser.parse_args()
else:
    flags = None


def main():
    serviceaccount = flags.serviceaccount
    input_file = flags.inputfile
    output_name = flags.outputfile
    folder_name = flags.foldername

    service = create_gdrive_service(flags=flags, service_account=serviceaccount)
    upload_file(service, input_file, output_name, folder_name)

if __name__ == '__main__':
    import logging
    log_level = logging.DEBUG
    logging.basicConfig(handlers=[logging.StreamHandler()], level=log_level,
                        format='[%(asctime)s] %(process)d %(name)s:%(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    main()
