import logging

from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# email activation
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

from .forms import LoginForm
from .forms import SignUpForm

from .activation import account_activation_token

logger = logging.getLogger('blog')

# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             acct = form.cleaned_data
#             user = authenticate(request, username=acct["username"], password=acct["password"])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect("/")
#                 else:
#                     return HttpResponse("Disabled account")
#             else:
#                 return HttpResponse("Invalid login")
#     else:
#         form = LoginForm()
#     return render(request, "account/login.html", {"form": form})


def sign_up(request):
    """
    Sign up
    """
    logger.info("sign_up")
    User = get_user_model()
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            email = signup_form.cleaned_data.get("email")
            if User.objects.filter(email__iexact=email).count() == 0:
                # signup way 1
                new_user = signup_form.save(commit=False)
                new_user.set_password(signup_form.cleaned_data["password"])
                new_user.is_active = False
                new_user.save()

                current_site = request.get_host()
                mail_subject = "Welcome to Django Blog!"

                message = render_to_string(
                    "account/activation.html",
                    {
                        "user": new_user,
                        "domain": current_site,
                        "uid": urlsafe_base64_encode(force_bytes(new_user.id)),
                        "token": account_activation_token.make_token(new_user),
                    },
                )

                try:
                    email = EmailMessage(mail_subject, message, to=[new_user.email])
                    email.send()
                except Exception:
                    logger.error("Email error")
                return HttpResponse("Verification link has been sent to linked email addresses")
    else:
        signup_form = SignUpForm()
    return render(request, "account/signup.html", {"signup_form": signup_form})


def activate(request, uidb64, token):
    """
    Email Activation
    """
    logger.info("activate")
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse(
            "Thank you for your email confirmation. Now you can login your account."
        )
    else:
        return HttpResponse("Activation link is invalid!")
