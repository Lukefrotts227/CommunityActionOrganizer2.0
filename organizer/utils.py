from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

def send_verification_email(user, request):
    token = default_token_generator.make_token(user)
    user_email = user.email
    subject = 'Verify your account'
    message = f"Please click the following link to verify your account: {request.build_absolute_uri('/verify-email/')}?token={token}"
    send_mail(subject, message, 'from@example.com', [user_email], fail_silently=False)
