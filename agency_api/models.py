from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='project_img', blank=True, null=True)
    created = models.DateTimeField()
    description = models.TextField(max_length=1000, blank=True)

    site_url = models.URLField()
    instagram_url = models.URLField()
    title_url = models.URLField()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('created',)
        app_label = 'agency_api'

    def __str__(self):
        return self.title


class Images(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class AboutCompany(models.Model):
    projects = models.CharField(max_length=150, db_index=True)
    date_of_creation = models.DateField()
    awards = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'company'


class Clients(models.Model):
    icon = models.ImageField(upload_to="icons", blank=True, null=True)
    client_partner = models.URLField()

    date_for_sort = models.DateTimeField()

    num_for_sort = models.IntegerField(unique=True)

    class Meta:
        ordering = ('num_for_sort',) # change to "date_for_sort" for sorting with date
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Services(models.Model):
    image = models.ImageField(upload_to='services', blank=True, null=True)
    title = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
        app_label = 'agency_api'

    def __str__(self):
        return self.title