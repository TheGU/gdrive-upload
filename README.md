# gdrive-upload
Upload file to specific folder using Google Drive API

## Getting Start :
#### 1. Clone this code for local copy
`git clone https://github.com/TheGU/gdrive-upload.git`
and go to cloned folder
`cd gdrive-upload`

#### 2. Obtain OAuth 2.0 credentials from the Google Developers Console.
Visit the [Google Developers Console](https://console.developers.google.com/) to obtain OAuth 2.0 credentials such as a client ID and client secret that are known to both Google and your application. Choose option to download it as JSON format and save to `client_secret.json` in `gdrive-upload` folder as this code.

or follow [step 1 in this guideline](https://developers.google.com/drive/v3/web/quickstart/python#step_1_turn_on_the_api_name). We will use this key as [web service token](https://developers.google.com/identity/protocols/OAuth2WebServer)

#### 3. Install require package
```
pip install -r requirements.txt
```

#### 4. Test upload file to specific folder
At this point your folder structure should be
```
- upload.py
- client_secret.json
- gdrive_upload/
 |- gdrive_authen.py
 |- gdrive_uploader.py
 |- ...
```

You can test upload or see example on how to use this code by command line helper script `upload.py`. 
For example:
```
python upload.py -i /path/to/file/image.png -o new-image-name.png -f foldername
```
__Option__
'-i <file path>' : full path or relative path to source file to upload
'-o <file name>' : [Optional] target filename on gdrive, if none, use same name as source filename
'-f <folder name>' : [Optional] Set target folder name (from root) to store file in. If not exist, this folder will create under root folder on gdrive. if none, store on root folder
'-s' : [Optional] Call this flag if you want to use [service account](https://developers.google.com/identity/protocols/OAuth2ServiceAccount) instead of user account. If this flag is set you must have service account store in file `service_secret.json` for script to call.

##### Run for the first time
If it run for the first time, it will show you an url to obtain key to create token to access Google drive. The script will auto create local server to intercept code to create token. 

But if your script cannot connect to Google, use `--noauth_local_webserver` in command line to force it to tell Google to display code that will let you copy and paste to your script manually. 
```
python upload.py --noauth_local_webserver -i /path/to/file/image.png -o new-image-name.png -f foldername
```
Copy that link and open it in your browser. It'll ask you to login to your google account then ask for access to your google drive. After accept the permissions it will show a code then pass that code to your script and hit enter.

![](https://developers.google.com/accounts/images/installedresult.png)
  
It will save the credential and token to local folder. So, next time you call this script it will not ask for permission again. A file will start upload and show progress bar and speed. 

### Supported versions
Write and test on python 2.7, 3.6 on windows 7 and ubuntu 14.04