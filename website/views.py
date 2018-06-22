from django.shortcuts import render
from django.http import HttpResponse

# Website entry
def entry(request):
    return render(request, 'entry.html')

# Website home
def home(request):
    return render(request, 'home.html')