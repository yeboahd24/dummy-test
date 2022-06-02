from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from .models import Person
from .forms import PersonForm, RegistrationForm, BankForm

from django.views.generic.edit import FormView

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
    


class RegistrationFormView(FormView):
    template_name = 'material/basic_form.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BankFormView(FormView):
    template_name = 'material/bank.html'
    form_class = BankForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)