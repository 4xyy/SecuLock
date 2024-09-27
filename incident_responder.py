import logging
from datetime import datetime
from send_email import send_breach_email
from push_notification import send_push_notification

logging.basicConfig(filename='logs/breach_logs.log', level=logging.INFO)

def generate_new_password():
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    new_password = ''.join(random.choices(characters, k=12))
    return new_password

def log_breach(details):
    logging.info(f"Breach detected at {datetime.now()} | Details: {details}")

def change_real_password():
    new_password = generate_new_password()
    print(f"Changing real account password to: {new_password}")
    return new_password

def notify_user(time_of_breach):
    send_breach_email(time_of_breach) 

def lock_account():
    print("Locking account to prevent further access...")

def handle_breach():
    breach_details = {
        'action': 'Password changed and account locked',
        'time': str(datetime.now())
    }

    time_of_breach = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_password = change_real_password()
    print(f"New password: {new_password}")

    notify_user(time_of_breach)

    lock_account()

    breach_details['new_password'] = new_password
    log_breach(breach_details) 
