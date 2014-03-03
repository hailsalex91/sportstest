from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import athlete, school, coach, golfImage, statistics, sports
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    image_url = golfImage.objects.order_by('?')[0]
    teams = sports.objects.all()
    sport2 = sports.objects.get(pk=2)
    sport3 = sports.objects.get(pk=3)
    sport4 = sports.objects.get(pk=4)
    sport5 = sports.objects.get(pk=5)
    sport6 = sports.objects.get(pk=6)
    sport7 = sports.objects.get(pk=7)
    sport8 = sports.objects.get(pk=8)
    sport9 = sports.objects.get(pk=9)
    sport10 = sports.objects.get(pk=10)
    sport11 = sports.objects.get(pk=11)
    sport12 = sports.objects.get(pk=12)
    sport13 = sports.objects.get(pk=13)
    sport14 = sports.objects.get(pk=14)
    sport15 = sports.objects.get(pk=15)
    sport16 = sports.objects.get(pk=16)
    sport17 = sports.objects.get(pk=17)
    sport18 = sports.objects.get(pk=18)
    sport19 = sports.objects.get(pk=19)
    sport20 = sports.objects.get(pk=20)
    sport21 = sports.objects.get(pk=21)
    sport22 = sports.objects.get(pk=22)
    sport23 = sports.objects.get(pk=23)
    sport24 = sports.objects.get(pk=24)
    sport25 = sports.objects.get(pk=25)
    sport26 = sports.objects.get(pk=26)
    context={
        'image': image_url,
        'sports': teams,
        'sport2': sport2,
        'sport3': sport3,
        'sport4': sport4,
        'sport5': sport5,
        'sport6': sport6,
        'sport7': sport7,
        'sport8': sport8,
        'sport9': sport9,
        'sport10': sport10,
        'sport11': sport11,
        'sport12': sport12,
        'sport13': sport13,
        'sport14': sport14,
        'sport15': sport15,
        'sport16': sport16,
        'sport17': sport17,
        'sport18': sport18,
        'sport19': sport19,
        'sport20': sport20,
        'sport21': sport21,
        'sport22': sport22,
        'sport23': sport23,
        'sport24': sport24,
        'sport25': sport25,
        'sport26': sport26
    }

    return render(request, 'roster/home.html', context)
def athleteView(request, pk):
    #My list of athletes is linking to an individual athlete's page

    theAthlete = get_object_or_404(athlete, pid=pk)
    image_url = golfImage.objects.order_by('?')[0]
    stats = statistics.objects.all()
    context={
        'athlete':theAthlete,
        'image': image_url,
        'stats': stats
    }

    return render(request, "roster/athlete.html", context)
def athleteList(request):
    #NEED TO PASS A SCHOOL TO BE ABLE TO GET THE SCHOOL NAME FOR AN ATHLETE
    athlete1 = athlete.objects.get(pid=714821000)
    athlete2 = athlete.objects.get(pid=714821001)
    athlete3 = athlete.objects.get(pid=714821002)
    athlete4 = athlete.objects.get(pid=714821003)
    athlete5 = athlete.objects.get(pid=714821004)
    athlete6 = athlete.objects.get(pid=714821005)
    athlete7 = athlete.objects.get(pid=714821006)
    athlete8 = athlete.objects.get(pid=714821007)

    image_url = golfImage.objects.order_by('?')[0]
    context ={
        #'athletes': athlete.objects.all(),
        'athlete1':athlete1,
        'athlete2':athlete2,
        'athlete3':athlete3,
        'athlete4':athlete4,
        'athlete5':athlete5,
        'athlete6':athlete6,
        'athlete7':athlete7,
        'athlete8':athlete8,
        'image': image_url
    }
    return render(request, "roster/AllAthlete.html",context)
def schoolView(request):
    theSchool = school.objects.order_by('?')[0]
    return render(request, "roster/school.html", {'school':theSchool})
def coachView(request):
    theCoach = coach.objects.order_by('?')[0]
    return render(request, "roster/coach.html", {'coach': theCoach})
