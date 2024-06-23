from django.shortcuts import render, HttpResponse , redirect
from .models import Login_info


def login(request):
    if request.method == "POST":
        if 'login' in request.POST: # login will be the name of the button
            username = request.POST.get("Username")  # .get(Username) -----> match input tag's name in html
            password = request.POST.get("Password")  # .get(Password) -----> match input tag's name in html
            print(username)
            print(password)
            try:
                user = Login_info.objects.get(Username=username, Password=password) # used Username variable created in models.py file
                print(user)
                if user is not None:
                    return redirect('base') # base is taken from path of url.py page
            except Exception as e:
                print(e)  # Optionally print the exception to console for debugging
                return render(request, 'login.html', {'error_message': 'An error occurred'})
            
        elif 'signup' in request.POST: # signup will be the name of the button
                return redirect('signup')
    else:
        return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")

def base(request):
    return render(request, "base.html")
