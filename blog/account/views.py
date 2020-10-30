import logging

from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .forms import LoginForm
from .forms import SignUpForm


logger = logging.getLogger(__name__)

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
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            # signup way 1
            new_user = signup_form.save(commit=False)
            new_user.set_password(signup_form.cleaned_data["password"])
            new_user.save()
            return redirect("/")
    else:
        signup_form = SignUpForm()
    return render(request, "account/signup.html", {"signup_form": signup_form})
