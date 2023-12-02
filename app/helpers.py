


# # from django.core.mail import send_mail

# # from django.conf import settings 


# # def send_forget_password_mail(email , token ):
# #     subject = 'Your forget password link'
# #     message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
# #     email_from = settings.EMAIL_HOST_USER
# #     recipient_list = [email]
# #     send_mail(subject, message, email_from, recipient_list)
# #     return True

#  ------------------------------------------------------------------------------------------------------

# from django.core.mail import send_mail
# from django.conf import settings

# def send_forget_password_mail(email, token):
#     subject = 'Reset Your Password'

#     html_message = f'''\
#     <html>
#     <body>
	# <h1 class="text-center" style="color: #007bff; text-align: center;">Reset Your Password</h1>

#     <p>Dear User,</p>
    
#     <p>We hope this message finds you well. It has come to our attention that you may have encountered difficulty accessing your account. As such, we are here to assist you in resetting your password promptly and securely.</p>
    
#     <p>To initiate the password reset process, please follow the steps outlined below:</p>
    
#     <p>Click on the button below to reset your password:</p>
    
#     <a href="http://127.0.0.1:8000/change-password/{token}/" style="background-color:#008CBA;border:1px solid #008CBA;border-radius:5px;color:white;padding:10px 15px;text-align:center;text-decoration:none;display:inline-block;font-size:16px;">Reset Password</a>
    
#     <p>[Note: If the button doesn't work, please copy and paste the following URL into your browser's address bar: http://127.0.0.1:8000/change-password/{token}/]</p>
    
#     <p>We prioritize the security of your account and ensure that this process is encrypted and safeguarded. Should you not have requested this action or have any concerns, please contact our support team immediately at info@foreseeed.app.</p>
    
#     <p>Thank you for entrusting us with your account security.</p>
    
#     <p>Best Regards,<br/>Your Company/Organization Name Team</p>
    
#     <hr/>
#     <p>[Disclaimer: This is an automated email. Please do not reply directly to this message.]</p>
    
#     </body>
#     </html>
#     '''

#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]

#     send_mail(subject, '', email_from, recipient_list, html_message=html_message)
#     return True

# --------------------------------------------------------------------------------------- 

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_forget_password_mail(email, token):
    subject = 'Reset Your Password'

    # Render the HTML template for the email
    html_message = render_to_string('reset-password-email.html', {'token': token})

    # Extract the text content from HTML for the plain text version of the email
    text_content = strip_tags(html_message)

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    # Create an EmailMultiAlternatives object to include both HTML and plain text versions of the email
    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_message, "text/html")

    # Send the email
    msg.send()
    return True
