from django.shortcuts import render

def register(request):
    return render(request,'accounts/register.html')


def signin(request):
    return render(request,'accounts/signin.html')


def profile(request):
    return render(request,'accounts/dashboard.html')