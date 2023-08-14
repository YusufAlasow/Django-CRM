from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect


def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging in, Please Try Again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

'''def login_user(request):
    # Implement your login logic here
    logout(request)
    messeges.success(request, "You have been logged out")
    return redirect('home')'''


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')
  
def register_user(request):
	return render(request,'register.html', {})