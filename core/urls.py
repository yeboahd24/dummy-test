"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dummy.views import PersonCreate, PersonList, RegistrationFormView, BankFormView, home, login_view, signup
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from django.utils.translation import gettext_lazy as _
from lang.views import change_language


# urlpatterns = [
#     path('change_language/',
#         change_language,
#         name='change_language'),
#     path('i18n/', include('django.conf.urls.i18n')),

# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', PersonCreate.as_view(), name='person'),
    path('list/', PersonList.as_view(), name='person_list'),
    path('finance/', include('microfinance.urls')),
    path('emails', include('emails.urls', namespace='emails')),
    path('registration/', RegistrationFormView.as_view(), name='registration'),
    path('bank/', BankFormView.as_view(), name='bank'),
    # path('', include('lang.urls')),
    path(_('blog/'), include('blog.urls')),
    path('map', include('map.urls')),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),

    # prefix_default_language=False,
    
]
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
