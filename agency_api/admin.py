from django.contrib import admin
from .models import Project, Images, Company


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created', 'description', 'site_url', 'instagram_url', 'title_url']
    list_editable = ['created']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['project', 'image']
    list_editable = ['image']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['projects', 'date_of_creation', 'awards']
    list_editable = ['date_of_creation']
