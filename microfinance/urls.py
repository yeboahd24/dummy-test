from django.conf.urls import url
from django.urls import path
from microfinance.views import viewsCall, viewsMenu, viewsUssd


urlpatterns = [
      
      path('',viewsUssd.callback, name = 'ussd'),
      path('voice',viewsCall.voice, name = 'voice'),
      path('menu',viewsMenu.menu, name = 'menu'),
      
      

]
