from lang.models import Home
from modeltranslation.forms import TranslationModelForm

class MyForm(TranslationModelForm):
    class Meta:
        model = Home
     