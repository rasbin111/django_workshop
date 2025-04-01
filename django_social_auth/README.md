### Setting up domain for localhost locally
If you are using Linux or macOS, the hosts file is located at: 
`/etc/hosts` 
If you are using Windows, the hosts file is located at: 
`C:\Windows\System32\Drivers\etc\hosts.`
Edit the hosts file of your machine and add the following line to it:
```bash
127.0.0.1 mysite.com
```
### Creating API key in Google Developer Console:
https://console.cloud.google.com/projectcreate

Add this for 'Authorised JavaScript origins'
https://mysite.com:8000

Add this for ' Authorised redirect URIs '
https://mysite.com:8000/social-auth/complete/google-oauth2/

### Running the code 
```bash
python manage.py runserver_plus --cert-file cert.crt
```

# adding API key to code
create `.env` file and 
```bash
GOOGLE_OAUTH2_KEY="YOUR_CLIENT_ID"
GOOGLE_OAUTH2_SECRET="YOUR_CLIENT_SECRET"
```