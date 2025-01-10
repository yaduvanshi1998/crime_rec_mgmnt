from django.shortcuts import render, HttpResponse , redirect, get_object_or_404
from .models import Login_info,Court_info, Judge_info, Victim_info, Offender_info, Crime_info, Prison_information, Guard_information
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

from django.shortcuts import render, get_object_or_404
from .models import Judge_info, Court_info

def add_judge(request):
    if request.method == "POST":
        # Extract form data
        f_name = request.POST.get("F_name")
        l_name = request.POST.get("L_name")
        designation = request.POST.get("Designation")
        court_name = request.POST.get("Court_name")
        age = request.POST.get("Age")
        address = request.POST.get("Address")
        phone_no = request.POST.get("Phone")
        email = request.POST.get("Email")
    
        try:
            # Fetch the Court_id using the provided court_name
            court = get_object_or_404(Court_info, Court_name=court_name)
            print("court --------------", court)

            # Check if phone and email already exists
            if Judge_info.objects.filter(Email=email).exists(): 
                return render(request, 'add_judge.html', {
                    'error_message': f'Email {email} already exists. Please choose a different ID.'
                })
            
            elif Judge_info.objects.filter(Phone_no=phone_no).exists():
                return render(request, 'add_judge.html', {
                    'error_message': f'Phone no. {phone_no} already exists. Please choose a different phone no.'
                })

            # Create and save the Judge_info record
            judge = Judge_info(
                F_name=f_name,
                L_name=l_name,
                Designation=designation,
                Court_id=court,  # Use the Court_info instance directly
                Age=age,
                Address=address,
                Phone_no=phone_no,
                Email=email,
            )
            judge.save()

            #courts = Court_info.objects.all()
            #print("courts---------------", courts) # output for this is 
            #<QuerySet [<Court_info: Queens High Court>, <Court_info: Jackson Heights Court>, <Court_info: JH 73rd st Court>]>

            # Add success message
            return render(request, 'add_judge.html', {
                'success_message': 'Data added to the database successfully!',
                'courts': Court_info.objects.all(),  # Include courts for dropdown
            })
        except Exception as e:
            # Add error message
            return render(request, "add_judge.html", {
                "error_message": f"Error saving judge information: {str(e)}",
                'courts': Court_info.objects.all(),  # Include courts for dropdown
            })

    return render(request, "add_judge.html")

def add_victim(request):
    if request.method == "POST":
        f_name = request.POST.get("F_name")
        l_name = request.POST.get("L_name")
        age = request.POST.get("Age")
        nationality = request.POST.get("Nationality")
        address = request.POST.get("Address")
        phone = request.POST.get("Phone")
        court_name = request.POST.get("Court_name")
        judge_email = request.POST.get("Judge_email")

        try:
            # Fetch Court object based on court name
            court = get_object_or_404(Court_info, Court_name=court_name)
            
            # Fetch Judge object based on judge email
            judge = get_object_or_404(Judge_info, Email=judge_email)

            # Check if phone number exists in Judge_info or Victim_info (to avoid duplicates)
            if Victim_info.objects.filter(Phone_no=phone).exists():
                return render(request, "add_victim.html", {
                    "error_message": f"Phone number {phone} already exists. Please use a different phone number.",
                    'courts': Court_info.objects.all()  # Include courts for dropdown
                })

            # Check if the given Court_id exists
            if not Court_info.objects.filter(Court_name=court_name).exists():
                return render(request, "add_victim.html", {
                    "error_message": f"Court with name {court_name} does not exist.",
                    'courts': Court_info.objects.all()  # Include courts for dropdown
                })

            # Check if the Judge exists
            if not Judge_info.objects.filter(Email=judge_email).exists():
                return render(request, "add_victim.html", {
                    "error_message": f"Judge with email {judge_email} does not exist.",
                    'courts': Court_info.objects.all()  # Include courts for dropdown
                })

            # Create and save Victim_info object
            victim = Victim_info(
                F_name=f_name,
                L_name=l_name,
                Age=age,
                Nationality=nationality,
                Address=address,
                Phone_no=phone,
                Court_id=court,
                Judge_id=judge,
            )
            victim.save()  # Save victim data
            print("Victim data saved successfully.")

            # Add success message
            return render(request, 'add_victim.html', {
                'success_message': 'Victim data added successfully!',
                'courts': Court_info.objects.all()  # Include courts for dropdown
            })

        except Exception as e:
            # Add error message for unexpected errors
            return render(request, "add_victim.html", {
                "error_message": f"Error saving victim information: {str(e)}",
                'courts': Court_info.objects.all()  # Include courts for dropdown
            })

    # Handle GET request
    return render(request, "add_victim.html")

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Offender_info, Court_info, Victim_info, Judge_info

"""Helper function to generate the context for the offender form. for offender info"""
def get_offender_form_context():
    return {
        'genders': ['Male', 'Female', 'Other'],
        'bail_status_choices': ['Jailed', 'Released'],
        'offense_types': ['Murder', 'Theft', 'Half_murder', 'Ragging', 'Ditching', 'Other'],
        'courts': Court_info.objects.all()
    }


def add_offender(request):
    if request.method == "POST":
        # Retrieve form data
        f_name = request.POST.get("F_name")
        l_name = request.POST.get("L_name")
        gender = request.POST.get("Gender")
        age = request.POST.get("Age")
        nationality = request.POST.get("Nationality")
        address = request.POST.get("Address")
        phone = request.POST.get("Phone")
        offense_type = request.POST.get("Offense_type")
        bail_status = request.POST.get("Bail_status")
        jail_terms = request.POST.get("Terms")
        court_name = request.POST.get("Court_name")
        victim_phone = request.POST.get("Victim_phone")
        judge_email = request.POST.get("Judge_email")

        # Get dynamic context for the form
        context = get_offender_form_context()

        # Check if offender phone number already exists
        if Offender_info.objects.filter(Phone_no=phone).exists():
            context['error_message'] = "Offender with this phone number already exists. Please use a unique phone number."
            return render(request, "add_offender.html", context)

        # Validate Court Name
        try:
            court = get_object_or_404(Court_info, Court_name=court_name)
        except:
            context['error_message'] = "Court name not found. Please select a valid court."
            return render(request, "add_offender.html", context)

        # Validate Victim Phone Number
        try:
            victim = get_object_or_404(Victim_info, Phone_no=victim_phone)
        except:
            context['error_message'] = "Victim phone number not found. Please enter a valid victim phone number."
            return render(request, "add_offender.html", context)

        # Validate Judge Email
        try:
            judge = get_object_or_404(Judge_info, Email=judge_email)
        except:
            context['error_message'] = "Judge email not found. Please enter a valid judge email."
            return render(request, "add_offender.html", context)

        # If no errors, create and save offender
        offender = Offender_info(
            F_name=f_name,
            L_name=l_name,
            Gender=gender,
            Age=age,
            Nationality=nationality,
            Address=address,
            Phone_no=phone,
            Offense_type=offense_type,
            Bail_status=bail_status,
            Jail_terms = jail_terms,
            Court_id=court,
            Victim_id=victim,
            Judge_id=judge
        )
        offender.save()

        # Success message
        context['success_message'] = "Offender information added successfully."
        return render(request, "add_offender.html", context)

    else:
        # For GET request, get the context for rendering the form
        context = get_offender_form_context()
        return render(request, "add_offender.html", context)
    
def add_crime(request):
    if request.method == "POST":
        # Retrieve form data
        weapon_used = request.POST.get("Weapon_used")
        crime_date = request.POST.get("Crime_date")
        crime_time = request.POST.get("Crime_time")
        crime_location = request.POST.get("Crime_location")
        offender_fname = request.POST.get("Offender_fname")
        offender_lname = request.POST.get("Offender_lname")
        victim_fname = request.POST.get("Victim_fname")
        victim_lname = request.POST.get("Victim_lname")

        context = {}  # Initialize context for error or success messages

        # Validate required fields
        if not all([weapon_used, crime_date, crime_time, crime_location, offender_fname, offender_lname, victim_fname, victim_lname]):
            context['error_message'] = "All fields are required. Please fill out the form completely."
            return render(request, "add_crime.html", context)

        # Validate and retrieve offender
        try:
            offender = Offender_info.objects.get(F_name=offender_fname, L_name=offender_lname)
        except Offender_info.DoesNotExist:
            context['error_message'] = "Offender not found. Please ensure the offender's details are correct."
            return render(request, "add_crime.html", context)

        # Validate and retrieve victim
        try:
            victim = Victim_info.objects.get(F_name=victim_fname, L_name=victim_lname)
        except Victim_info.DoesNotExist:
            context['error_message'] = "Victim not found. Please ensure the victim's details are correct."
            return render(request, "add_crime.html", context)

         # Fetch the Crime_type from the Offender_info table (using the Offense_type column)
        crime_type = offender.Offense_type

        # Create and save the crime record
        crime = Crime_info(
            Crime_type = crime_type,
            Weapon_used=weapon_used,
            Crime_date=crime_date,
            Crime_time=crime_time,
            Crime_loccation=crime_location,  # Note: This matches your model field name
            Offender_id=offender,
            Victim_id=victim
        )
        crime.save()

        # Success message
        context['success_message'] = "Crime information added successfully."
        return render(request, "add_crime.html", context)

    else:
        # Render the form for GET requests
        return render(request, "add_crime.html")

def add_prison(request):
    context = {}  # Context to pass error or success messages to the template
    
    if request.method == "POST":
        # Retrieve form data
        prison_name = request.POST.get("Prison_name")
        telephone_no = request.POST.get("Telephone")
        address = request.POST.get("Address")
        offender_fname = request.POST.get("Offender_fname")
        offender_lname = request.POST.get("Offender_lname")
        
        # Check for existing telephone number in the database
        if Prison_information.objects.filter(Telephone_no=telephone_no).exists():
            context['error_message'] = "This telephone number is already associated with another prison. Please enter a unique telephone number."
            return render(request, "add_prison.html", context)

        # Retrieve offender details
        try:
            offender = Offender_info.objects.get(F_name=offender_fname, L_name=offender_lname)
        except Offender_info.DoesNotExist:
            context['error_message'] = "Offender not found. Please ensure the offender's details are correct."
            return render(request, "add_prison.html", context)

        # Create and save the prison record
        prison = Prison_information(
            Prison_name=prison_name,
            Telephone_no=telephone_no,
            Address=address,
            Offender_id=offender
        )
        prison.save()

        # Success message
        context['success_message'] = "Prison information added successfully."

    # Return the form view with any messages in the context
    return render(request, "add_prison.html", context)

"""Helper function to generate the context for the guard form. for guard info"""
def get_guard_form_context():
    return {
        'genders': ['Male', 'Female', 'Other']
    }

def add_guard(request):
    if request.method == "POST":
        # Retrieve form data
        f_name = request.POST.get("F_name")
        l_name = request.POST.get("L_name")
        gender = request.POST.get("Gender")
        age = request.POST.get("Age")
        address = request.POST.get("Address")
        phone = request.POST.get("Phone")
        shift_start = request.POST.get("Shift_start")
        shift_end = request.POST.get("Shift_end")
        email = request.POST.get("Email")
        prison_name = request.POST.get("Prison_name")

        # Get dynamic context for the form
        context = get_guard_form_context()

        # Check if guard phone number already exists
        if Guard_information.objects.filter(Phone_no=phone).exists():
            context['error_message'] = "Guard with this phone number already exists. Please use a unique phone number."
            return render(request, "add_guard.html", context)

        # Check if guard email already exists
        if Guard_information.objects.filter(Email=email).exists():
            context['error_message'] = "Guard with this email already exists. Please use a unique email."
            return render(request, "add_guard.html", context)

        # Validate prison name
        try:
            prison = get_object_or_404(Prison_information, Prison_name=prison_name)
        except:
            context['error_message'] = "Prison name not found. Please enter a valid prison name."
            return render(request, "add_guard.html", context)

        # If no errors, create and save guard
        guard = Guard_information(
            F_name=f_name,
            L_name=l_name,
            Gender=gender,
            Age=age,
            Address=address,
            Phone_no=phone,
            Shift_start=shift_start,
            Shift_end=shift_end,
            Email=email,
            Prison_id=prison
        )
        guard.save()

        # Success message
        context['success_message'] = "Guard information added successfully."
        return render(request, "add_guard.html", context)

    else:
        # For GET request, get the context for rendering the form
        context = get_guard_form_context()
        return render(request, "add_guard.html", context)

