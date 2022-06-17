from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def homepage(request):
    return render(
        request=request,
        template_name='index.html',
    )
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"You've successfully created an account:{username}")
            login(request, user)
            return redirect ('homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
                
    form = UserCreationForm()
    return render(request= request,
					template_name ='main/register.html',
					context= {"form": form})


def logout(request):
	logout(request)
	messages.info(request, "You've successfully logged out")
	return redirect("homepage")

def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username= username, password = password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You have successfully logged in as {username}")
				return redirect("homepage")
			else:
				messages.error(request, "Invalid Username or Password")
		else:
			messages.error(request, "Invalid Username or Password")
	form = AuthenticationForm()
	return render(request,
					"main/login.html",
					{"form": form})
