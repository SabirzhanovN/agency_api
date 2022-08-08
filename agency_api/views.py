from django_filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404

from .service import send_message
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Images, AboutCompany, Clients, Services
from .serializers import ProjectListSerializer, ProjectDetailSerializer, ImageSerializer, CompanySerializer, \
    ClientsSerializer, ProjectImageSerializer, MessageSerializer, ServiceSerializer


# pagination classes
class ProjectsPageSize(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProjectListPageSize(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


class ServicesPageSize(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


# views
class ProjectListAPIView(generics.ListAPIView):
    pagination_class = ProjectsPageSize
    filter_backends = [DjangoFilterBackend, SearchFilter]
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer

    search_fields = ['title', 'description']


class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        w = get_object_or_404(Project, pk=pk)
        return Response({"post": ProjectDetailSerializer(w).data})


class CompanyListAPIView(generics.ListAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = CompanySerializer


class ClientsListAPIView(generics.ListAPIView):
    queryset = Clients.objects.all().order_by('num_for_sort')
    serializer_class = ClientsSerializer


class ImageListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectImageSerializer
    pagination_class = ProjectListPageSize


class ServiceListAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = ServicesPageSize


############################################


class SendMessageView(generics.GenericAPIView):
    serializer_class = MessageSerializer

    def __init__(self, name, email, phone, project):
        self.name = name
        self.email = email
        self.phone = phone
        self.project = project

    def post(self, request):
        serializer = MessageSerializer(request.data)
        name = serializer.data['name']
        phone = serializer.data['phone']
        email = serializer.data['email']
        project = serializer.data['project']
        message = "*ЗАЯВКА С САЙТА* :" + "\n" + "*Name*: " + str(name) + "\n" + "*Phone* : " + str(
            phone) + '\n' + '*email*: ' + str(email) + '\n' + '*Project*: ' + str(project)
        send_message(message)
        return Response({'status': 'OK'})
