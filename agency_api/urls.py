from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import path, include

from . import views

urlpatterns = [
    path('send_message/', views.SendMessageView.as_view()),
    path('service_list/', views.ServiceListAPIView.as_view()),

    path('about/', views.CompanyListAPIView.as_view()),
    path('about/images/', views.ProjectListAPIView.as_view()),
    path('about/clients_list/', views.ClientsListAPIView.as_view()),

    path('project_list/', views.ProjectListAPIView.as_view()),
    path('project_list/<int:pk>/', views.ProjectDetailAPIView.as_view())
]
