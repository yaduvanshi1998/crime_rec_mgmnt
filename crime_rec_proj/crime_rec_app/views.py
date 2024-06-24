from django.shortcuts import render, HttpResponse , redirect
from .models import Login_info
from datetime import datetime


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
    if request.method == "POST":
        username = request.POST.get("Username")
        fname = request.POST.get("Fname")
        lname = request.POST.get("Lname")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
            # Check if username or email already exists
        try:
            if Login_info.objects.filter(Username=username).exists():
                return render(request, 'signup.html', {'error_message': 'Username {} already exists. Please choose a different username.'.format(username)})
            elif Login_info.objects.filter(Email=email).exists():
                return render(request, 'signup.html', {'error_message': 'Email {} already exists. Please use a different email address.'.format(email)})
            else:
                new_login_info = Login_info(Username=username, F_name=fname, L_name=lname, Email=email, Password=password, DateTime=datetime.today())
                new_login_info.save()
                return render(request, 'signup.html', {'success_message': 'Data added to database successfully!'})
        except Exception as e:
            print(e)  # Print the exception for debugging purposes
            return render(request, 'signup.html', {'error_message': 'An error occurred while processing your request.'})
    
    else:
        return render(request, "signup.html")

def base(request):
    return render(request, "base.html")
