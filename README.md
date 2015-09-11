# gdrive-upload
Upload file to specific folder using Google Drive API

## Getting Start :
#### 1. Clone this code for local copy
`git clone https://github.com/TheGU/gdrive-upload.git`

#### 2. Obtain OAuth 2.0 credentials from the Google Developers Console.
Visit the [Google Developers Console](https://console.developers.google.com/) to obtain OAuth 2.0 credentials such as a client ID and client secret that are known to both Google and your application. Choose option to download it as JSON format and save to "client_secrets.json" in the same folder as this code.

or follow [this guideline](https://developers.google.com/identity/protocols/OAuth2InstalledApp)

#### 3. Upload file to specific folder
On ubuntu you can run
```
pip install -r requirements.txt
python upload.py -i /path/to/file/image.png -o new-image-name.png -f foldername
```
If it run for the first time, it will show you an url to obtain key to create token to access Google drive. The script will auto create local server to intercept code to create token. 

But if your script cannot connect to Google use `--noauth_local_webserver` in command line to force it to tell Google to display code that will let you copy it and paste to you script manually. Copy that link and open it in your browser. It'll ask you to login to your google account then ask for access to your google drive. After accept the permissions it will show a code then pass that code to your script and hit enter.
![](https://developers.google.com/accounts/images/installedresult.png)
  
It will save the credential and token to local folder. So, next time you call this script it will not ask for permission again. A file will start upload and show progress bar and speed. 

### Supported versions
Write and test on python 2.7 windows 7 and ubuntu 14.04