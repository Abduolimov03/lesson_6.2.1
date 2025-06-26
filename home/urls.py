from tkinter.font import names

from django.urls import path

from .views import home, iqtisodiyot, jahon_yangilik, madaniyat, sport_yangilik, texnologiya, uzbek_yangilik

urlpatterns = [
    path('', home, name = 'home'),
    path('iqtisodiyot/', iqtisodiyot, name = 'iqtisodiyot'),
    path('jahon_yangilik/', jahon_yangilik, name = 'jahon_yangilik'),
    path('madaniyat/', madaniyat, name = 'madaniyat'),
    path('sport_yangilik/', madaniyat, name = 'sport_yangilik'),
    path('sport_yangilik/', sport_yangilik, name = 'sport_yangilik'),
    path('texnologiya/', texnologiya, name = 'texnologiya'),
    path('uzbek_yangilik', uzbek_yangilik, name = 'uzbek_yangilik')

]