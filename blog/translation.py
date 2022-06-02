from modeltranslation.translator import (
    translator,
    register,
    TranslationOptions,
)
from blog.models import Blog


class BlogTranslationsOptions(TranslationOptions):
    fields = ('title', 'slug')
    empty_values = {'slug': None}


translator.register(Blog, BlogTranslationsOptions)