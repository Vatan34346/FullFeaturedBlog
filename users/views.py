from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def register(req):
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f"Your account has been created. You can log in!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(req, 'users/register.html', {'form': form})


@login_required
def profile(req):
    return render(req, 'users/profile.html')

