from django.shortcuts import render
from crime_rec_app.models import Court_info, Judge_info, Victim_info, Offender_info, Crime_info, Prison_information, Guard_information, Punishment_info
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' for server-side rendering (since i was getting error as "RuntimeError: main thread is not in main loop")

from io import BytesIO
from django.templatetags.static import static
import base64

# Create your views here.

def court_record(request):
    courts = Court_info.objects.all() # getting all the details by creating this object
    return render(request, 'court_record.html',{'courts': courts})

def judge_record(request):
    judges = Judge_info.objects.all()
    return render(request,'judge_record.html', {'judges': judges})

def victim_record(request):
    victims = Victim_info.objects.all()
    return render(request, 'victim_record.html',{'victims': victims})

def offender_record(request):
    offenders = Offender_info.objects.all()
    return render(request, 'offender_record.html',{'offenders': offenders})

def crime_record(request):
    crimes = Crime_info.objects.all()
    return render(request, 'crime_record.html',{'crimes': crimes})

def prison_record(request):
    prisons = Prison_information.objects.all()
    return render(request, 'prison_record.html',{'prisons': prisons})

def guard_record(request):
    guards = Guard_information.objects.all()
    return render(request, 'guard_record.html',{'guards': guards})

def punishment_record(request):
    punishments = Punishment_info.objects.all()
    return render(request, 'punishment_record.html',{'punishments': punishments})

# To display the chart of crime yearly basis

def crime_data_view(request):
    # Query all the crime data
    crimes = Crime_info.objects.all()

    # Prepare data for charting
    crime_dates = [crime.Crime_date for crime in crimes]
    crime_types = [crime.Crime_type for crime in crimes]

    # Create a DataFrame
    df = pd.DataFrame({
        'Crime Date': crime_dates,
        'Crime Type': crime_types
    })

    # Count crimes per year
    df['Year'] = pd.to_datetime(df['Crime Date']).dt.year
    crime_count_by_year = df.groupby('Year').size()

    # Plot the pie chart
    plt.figure(figsize=(6, 6))  # Adjust size as needed
    plt.pie(crime_count_by_year, labels=crime_count_by_year.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Crime Counts by Year')

    # Save the chart to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the image as a URL
    img_url = "data:image/png;base64," + base64.b64encode(img.getvalue()).decode('utf8')

    # Pass the data and the image URL to the template
    return render(request, 'crime_record.html', {'crimes': crimes, 'plot_url': img_url})
