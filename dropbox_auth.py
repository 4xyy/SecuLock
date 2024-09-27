from dotenv import load_dotenv
import os
import dropbox

load_dotenv()

DROPBOX_ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')

def authenticate_dropbox():
    if not DROPBOX_ACCESS_TOKEN:
        raise ValueError("DROPBOX_ACCESS_TOKEN must be set in the .env file.")
    
    dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
    return dbx
