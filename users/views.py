from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        messages.success(request,f'Welcome {username}, your account is now created.')
        form.save()
        return redirect('mainapp:index')
    return render(request,'users/register.html',{"form":form})