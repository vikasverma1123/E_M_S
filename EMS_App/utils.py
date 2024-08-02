from django.core.mail import send_mail
from django.conf import settings

# def send_email_to_client():
#     subject = "Account Created"
#     message = "You Register Successfully you can now explore our services"
#     from_email = settings.EMAIL_HOST_USER
#     recipient_list = ["hbye20904@gmail.com"]
#     send_mail(subject, message, from_email,recipient_list)
    
def send_email_login():
    subject = "Login Successfully!"
    message = "You Login Successfully you can now explore our services"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["hbye20904@gmail.com"]
    send_mail(subject, message, from_email,recipient_list)
    
    
def send_custom_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'kidtales261@gmail.com',  # From email
        recipient_list,
        fail_silently=False,
    )