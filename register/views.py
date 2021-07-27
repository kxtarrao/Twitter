from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User


def landing_page(response):
    return redirect('/login')


def signup(response):

    if response.method == 'POST':
        signup_form = SignupForm(data=response.POST)
        print(signup_form.errors.as_data())
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/home')
        elif {'password1','password2'}.intersection(signup_form.errors.as_data().keys()):
            messages.add_message(response, messages.ERROR, '[ERROR] Invalid Password.')
            return redirect('/signup')
        else:
            messages.add_message(response, messages.ERROR, '[ERROR] Unable to sign up.')
            return redirect('/signup')

    else:
        signup_form = SignupForm()
        return render(response, 'signup.html', {'signup_form':signup_form})


#
# def logout(response):
#     # LOGIN RESET
#     messages.add_message(response,messages.SUCCESS,'[SUCCESS] You are now logged out.')
#     return redirect('/login')
