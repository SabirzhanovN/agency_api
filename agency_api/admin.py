from django.contrib import admin
from .models import Project, Images, AboutCompany, Clients, Services

from modeltranslation.admin import TranslationAdmin


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ['title_en', 'title_ru', 'image', 'created', 'description_en', 'description_ru', 'site_url',
                    'instagram_url', 'title_url']
    list_editable = ['created']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['project', 'image']
    list_editable = ['image']


@admin.register(AboutCompany)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['projects', 'date_of_creation', 'awards']
    list_editable = ['date_of_creation']


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['icon', 'client_partner', 'date_for_sort', 'num_for_sort']
    list_editable = ['date_for_sort', 'num_for_sort']


@admin.register(Services)
class ServiceAdmin(TranslationAdmin):
    list_display = ['image', 'title_en', 'title_ru']
    list_editable = ['title_en', 'title_ru']
