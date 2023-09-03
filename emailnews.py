import smtplib, ssl


def sent_mail(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "navwin34@gmail.com"
    password = "fllnshvtdzxpxycd"
    receiver = "navwin34@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)


