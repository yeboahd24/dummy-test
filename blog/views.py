from django.shortcuts import render
from blog.models import Blog
# Create your views here.
from django.utils.translation import gettext as _


def blogIndex(request):
    context = dict()

    context['blog_1'] = Blog.objects.all()[0]

    context['blog_2']= _("Success")


    return render(request, 'blog/blog.html', context)
