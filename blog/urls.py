from django.urls import path
from blog.views import (
    blogIndex,
)


urlpatterns = [
    path('', blogIndex, name='blog-index'),

]
