from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from models import athlete, school, coach, golfImage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    '''
    class Athlete(object):
        def __init__(self,):
            pass
            #Should I make objects using the data in my models and pass them
            #to my view?
            #How do i create an object that contains data from 2 different models
    class ObjectList(object):
        def __init__(self,athletes,schools):
            self.athletes = athletes
            self.schools = schools
        def genTableData(self):
            athleteList = []
            for athlete in self.athletes:
                pass
    '''
    image_url = golfImage.objects.order_by('?')[0]
    context={
        'athlete_count': athlete.objects.count(),
        'school_count': school.objects.count(),
        'coach_count': coach.objects.count(),
        'image': image_url
    }

    return render(request, 'roster/home.html', context)
def athleteView(request, pk):
    #My list of athletes is linking to an individual athlete's page
    theAthlete = get_object_or_404(athlete, pid=pk)
    return render(request, "roster/athlete.html", {'athlete':theAthlete})
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
