from datetime import datetime
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("shaktirp1@gmail.com")
subject = "Hello World from the SendGrid Python Library!"
to_email = Email("shaktirp1@gmail.com")
content = Content("text/plain", "Time is: " + str(datetime.now()))
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
