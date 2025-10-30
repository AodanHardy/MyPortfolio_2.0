import glob
import os

from django.shortcuts import render

from myPortfolio_2 import settings


# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def experience(request):
    return render(request, "experience.html")

def contact(request):
    return render(request, "contact.html")

def projects(request):
    return render(request, "projects.html")


def nextGenVoting(request):
    return render(request, "projects/nextGenVoting.html")
def restaurantManagementSyetem(request):
    return render(request, "projects/restaurantManagementSyetem.html")