from blog.models import Blog
from modeltranslation.forms import TranslationModelForm

class BlogForm(TranslationModelForm):
    class Meta:
        model = Blog