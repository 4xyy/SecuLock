import random
import string
from google_drive_auth import authenticate_google_drive
from googleapiclient.http import MediaFileUpload

def generate_fake_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def create_honeypot_file(fake_credentials):
    with open('honeypot_credentials.txt', 'w') as file:
        file.write(f"Username: {fake_credentials['username']}\n")
        file.write(f"Password: {fake_credentials['password']}\n")
    print("Honeypot credentials file created.")

def deploy_to_google_drive(fake_credentials):
    service = authenticate_google_drive()

    create_honeypot_file(fake_credentials)
    
    file_metadata = {
        'name': 'Honeypot-Credentials.txt',
        'mimeType': 'text/plain'
    }
    
    media = MediaFileUpload('honeypot_credentials.txt', mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Fake credentials deployed to Google Drive with file ID: {file.get('id')}")

def deploy_honeypots():
    fake_password = generate_fake_password()
    fake_credentials = {'username': 'decoyuser', 'password': fake_password}
    
    deploy_to_google_drive(fake_credentials)
