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

# login/logout
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = '@Linux70'


def login_view(request):
    if request.method == 'GET':
        username = DEFAULT_USERNAME 
        password = DEFAULT_PASSWORD
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


# default user/password: admin/admin
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')





# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# login as default user if user is not logged in
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


