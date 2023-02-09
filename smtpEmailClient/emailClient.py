import smtplib

def send_email(subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        message = 'Subject: {}\n\n{}'.format(subject, body)
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email: ", e)


sender_email = "sender_email@gmail.com"
sender_password = "sender_email_password"
recipient_email = "recipient_email@gmail.com"

send_email("Subject of the email", "Body of the email")
