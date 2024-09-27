from dotenv import load_dotenv
import os
from pushbullet import Pushbullet

load_dotenv()

PUSHBULLET_ACCESS_TOKEN = os.getenv('PUSHBULLET_ACCESS_TOKEN')

def send_push_notification():
    if not PUSHBULLET_ACCESS_TOKEN:
        raise ValueError("PUSHBULLET_ACCESS_TOKEN must be set in the .env file.")
    
    pb = Pushbullet(PUSHBULLET_ACCESS_TOKEN)
    push = pb.push_note("Breach Attempt Detected", "A honeypot credential was used!")
    print("Push notification sent!")
