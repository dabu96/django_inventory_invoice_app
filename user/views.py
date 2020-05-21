from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegistrationForm, SecurityCodeForm
from .models import SecurityCode

def register(request):

    context = {}

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        code_form = SecurityCodeForm(request.POST)
        valid_codes = SecurityCode.objects.all()

        if form.is_valid() and code_form.is_valid():
            for code in valid_codes:
                if code_form.cleaned_data.get('code') == code.code:
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Account has successfully been created for the user: {username}')
                    return redirect('login')
                else:
                    messages.error(request, 'Invalid Security Code')

        else:
            for msg in form.error_messages:
                messages.error(request, f" {msg} : {form.cleaned_data[msg]}")

    form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form,
                                                   'code_form': SecurityCodeForm()
                                                   })


def profile(request):
    return render(request, 'users/profile.html')

