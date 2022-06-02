from django.urls import path
from lang.views import (
    index,
)


urlpatterns = [
    path('', index, name='index'),

]
