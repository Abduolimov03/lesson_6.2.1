from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home_page.html')
def iqtisodiyot(request):
    return render(request, 'iqtisodiyot.html')
def jahon_yangilik(request):
    return render(request, 'jahon_yangilik.html')
def madaniyat(request):
    return render(request, 'madaniyat.html')
def sport_yangilik(request):
    return render(request, 'sport_yangilik.html')
def texnologiya(request):
    return render(request, 'texnologiya.html')
def uzbek_yangilik(request):
    return render(request, 'uzbek_yangilik.html')
