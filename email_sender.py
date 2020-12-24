import smtplib, ssl



# sender_email = "my@gmail.com"
# Send email here

def email_function(sender_email,reciver_email,your_password,message):
    smtp_server = "smtp.gmail.com"
    port = 465  # For starttls
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, your_password)
        server.sendmail(sender_email, reciver_email, message)


if __name__ == "__main__":
    password = "Iloveyou_3000"
    sender_email = "dhamejanimain@gmail.com"
    receiver_email = "dhamejanishivam@gmail.com"
    message = """\
    Subject: Hi there
    This message is sent from Python."""
    email_function(sender_email,receiver_email,password,message)

