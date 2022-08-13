from django.shortcuts import render
from django.template import *
from .models import Incident
from datetime import datetime, date

# Create your views here.
def index(request):
    incident = Incident.objects.filter().order_by('-id')[:2]
    last_incident = reversed(incident)


    result = {}

    for last in last_incident:
        result[str(last.platform)] = {"name": last.name, "platform": last.platform, "color": str(last.type)}

    current_week = date.today().isocalendar()[1]
    recents = Incident.objects.filter(hour__week=current_week, platform="Lupa")

    week = {
        "Monday":[],
        "Tuesday":[],
        "Wednesday":[], 
        "Thursday":[], 
        "Friday":[], 
        "Saturday":[], 
        "Sunday":[]
    }

    for recent in recents:
        week[str(recent.hour.strftime("%A"))].append(int(float(recent.latency)))

    m = []

    for day in week:
        try:
            mean = sum(week[day])/len(week[day])
            m.append(mean)
        except:
            m.append(0)

    return render(request, "app/pages/index.html", {"last": result, "week": m})