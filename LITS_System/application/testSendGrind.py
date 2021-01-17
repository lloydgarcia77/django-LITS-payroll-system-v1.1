import os 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import requests 
load_dotenv()
 
# SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
# message = Mail(
#     from_email='lloydgarcia77@gmail.com',
#     to_emails='lloyd.garcia@lits.com.ph',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')

# sg = SendGridAPIClient(SENDGRID_API_KEY)
# response = sg.send(message)
# print(response.status_code, response.body, response.headers)

# mail gun
# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandbox577e6f3449264b1e9322955b85b2252f.mailgun.org/messages",
# 		auth=("api", "9dc92c3cb50b0f14b8279e1fe1ac2613-2fbe671d-b3f627d1"),
# 		data={"from": "lloydgarcia77@gmail.com",
# 			"to": ["lloydgarcia77@gmail.com",],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})



# try:

#     send_simple_message()

# except Error as e:
#     print(e)