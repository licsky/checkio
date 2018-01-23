import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    from_email = Email('lic8086939@163.com')
    to_email = Email(email)
    subject = SUBJECT
    body = Content("text/plain", BODY.format(name))
    mail = Mail(from_email, subject, to_email, body)
    response = sg.client.mail.send.post(request_body=mail.get())
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')

# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)