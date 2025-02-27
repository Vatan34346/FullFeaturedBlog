from django.shortcuts import render, redirect
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
            messages.success(req, f"Account created for {username}!")
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(req, 'users/register.html', {'form': form})

