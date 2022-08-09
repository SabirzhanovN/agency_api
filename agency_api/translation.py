from modeltranslation.translator import register, TranslationOptions

from .models import Project, Services


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', )