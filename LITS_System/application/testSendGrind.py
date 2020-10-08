import os 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
load_dotenv()

# SENDGRID_API_KEY = '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'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
message = Mail(
    from_email='lloydgarcia77@gmail.com',
    to_emails='lloydsalazargarcia77@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

sg = SendGridAPIClient(SENDGRID_API_KEY)
response = sg.send(message)
print(response.status_code, response.body, response.headers)


  
 