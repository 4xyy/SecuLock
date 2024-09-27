import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_breach_email(time_of_breach):
    # Create the email message
    message = Mail(
        from_email='your_verified_sendgrid_email@example.com',  # Change this to your verified SendGrid email
        to_emails='recipient_email@example.com',                # Change this to the recipient's email
        subject='Urgent: Potential Security Breach Detected on SecuLock',
        html_content=f"""
        <html>
        <body>
            <h2 style="color:#1a73e8;">Security Alert: Honeypot Breach Detected</h2>
            <p>Dear User,</p>
            <p>We have detected a suspicious attempt to use one of our honeypot credentials on your SecuLock-protected account. Immediate action has been taken to secure your account and prevent further unauthorized access.</p>
            <p><strong>Details:</strong></p>
            <ul>
                <li>Credential: <strong>Honeypot User</strong></li>
                <li>Time of Attempt: <strong>{time_of_breach}</strong></li>
                <li>Action Taken: <strong>Password reset and account locked</strong></li>
            </ul>
            <p>We recommend you review your account activity and update your real account credentials if necessary. Please contact our support team if you need further assistance.</p>
            <p>Thank you for trusting SecuLock to protect your digital security.</p>
            <br>
            <p>Best regards,</p>
            <p>The SecuLock Security Team</p>
        </body>
        </html>
        """
    )
    
    try:
        # Send the email using SendGrid API
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")
