from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting
# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html", 
                  {"meetings": Meeting.objects.all()})


def about(request):
    return HttpResponse("This is a trivial app built while following the Pluralsight 'Django: Getting Started' tutorial.")