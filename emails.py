from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs): #We create a mail_message function that takes in 4 parameters which are the subject of the email,
    sender_email ='jacorugano@gmail.com'   #create sender_email where we store our email address.
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs) # We then set up the email body and HTML.
    mail.send(email) # use the send method of the mail instance and pass in the email instance.