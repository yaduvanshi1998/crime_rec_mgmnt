from django.shortcuts import render
from crime_rec_app.models import Court_info, Judge_info, Victim_info, Offender_info, Crime_info, Prison_information, Guard_information, Punishment_info
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