from django.views.generic import CreateView
from .service import send_message
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Images, Company, Clients
from .serializers import ProjectListSerializer, ProjectDetailSerializer, ImageSerializer, CompanySerializer, \
    ClientsSerializer, ProjectImageSerializer, MessageSerializer


# page-size for all 'projects'
class ProjectsPageSize(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000


# page-size for projects in other pages
class ProjectListPageSize(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


# views
class ProjectListAPIView(generics.ListAPIView):
    pagination_class = ProjectsPageSize
    filter_backends = [DjangoFilterBackend]
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        w = Project.objects.get(pk=pk)
        return Response({"post": ProjectDetailSerializer(w).data})


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ClientsListAPIView(generics.ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ImageListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectImageSerializer
    pagination_class = ProjectListPageSize


############################################

class SendMessageView(generics.GenericAPIView):
    serializer_class = MessageSerializer

    def post(self, request):
        serializer = MessageSerializer(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone']
        email = serializer.data['email']
        project = serializer.data['project']
        message = "*ЗАЯВКА С САЙТА* :" + "\n" + "*Name*: " + str(name) + "\n" + "*Phone* : " + str(
            phone) + '\n'+ '*email*: ' + str(email) + '\n' + '*Project*: ' + str(project)
        send_message(message)
        return Response('Ok')
