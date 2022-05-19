from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from .models import Person
from .forms import PersonForm

class PersonCreate(CreateView):
    template_name = 'person.html'
    form_class = PersonForm
    # model = Person
    # fields = ['name', 'country']
    success_url = '/'


class PersonList(PaginationMixin, ListView):
    object = Person
    queryset = Person.objects.all()
    paginate_by = 2
    template_name = 'person_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('-id')
    