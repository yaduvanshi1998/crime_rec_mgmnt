from django.shortcuts import render, HttpResponse , redirect
from .models import Login_info,Court_info
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
                new_login_info = Login_info(
                    Username=username, 
                    F_name=fname, 
                    L_name=lname, 
                    Email=email, 
                    Password=password, 
                    DateTime=datetime.today()
                    )
                
                new_login_info.save()
                return render(request, 'signup.html', {'success_message': 'Data added to database successfully!'})
        except Exception as e:
            print(e)  # Print the exception for debugging purposes
            return render(request, 'signup.html', {'error_message': 'An error occurred while processing your request.'})
    
    else:
        return render(request, "signup.html")

def base(request):
    return render(request, "base.html")


def add_court(request):
    if request.method == "POST":
        # Retrieve data from the form
        court_id = request.POST.get("Court_Id")
        court_name = request.POST.get("Name")
        address = request.POST.get("Address")
        level = request.POST.get("Level")
        phone = request.POST.get("Phone")
        email = request.POST.get("Email")

        try:
            # Check if Court_Id already exists
            if Court_info.objects.filter(Court_id=court_id).exists(): #Court_id - from models, court_id - variable in this code
                return render(request, 'add_court.html', {
                    'error_message': f'Court_Id {court_id} already exists. Please choose a different ID.'
                })
            elif Court_info.objects.filter(Phone_no=phone).exists():
                return render(request, 'add_court.html', {
                    'error_message': f'Phone no. {phone} already exists. Please choose a different phone no.'
                })

            # Save court information to the database
            court_info = Court_info(
                Court_id=court_id,
                Court_name=court_name,
                Address=address,
                Level=level,
                Phone_no=phone,
                Email=email
            )
            court_info.save()
            return render(request, 'add_court.html', {
                'success_message': 'Data added to the database successfully!'
            })
        except Exception as e:
            print(e)  # Debugging: Log the exception to the console
            return render(request, 'add_court.html', {
                'error_message': 'An error occurred while processing your request.'
            })

    # Render the form if the request method is not POST
    return render(request, "add_court.html")
