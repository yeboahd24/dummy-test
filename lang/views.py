from django.shortcuts import render
from lang.models import Home

# Create your views here.
from django.utils.translation import gettext as _
from django.conf import settings
from django.http import HttpResponseRedirect


def index(request):
    context = dict()

    context['a'] = Home.objects.all()[2]
    context['b']= _("How are you?")


    return render(request, 'translation/index.html', context)


def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response