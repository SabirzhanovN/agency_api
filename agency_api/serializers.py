from rest_framework import serializers

from .models import Project, Images, AboutCompany, Clients, Services


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image',)


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('image',)


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'image', 'description')


class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'id', 'title', 'image', 'description', 'created',
            'site_url', 'instagram_url', 'title_url', 'images'
        )


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = ('id', 'projects', 'date_of_creation', 'awards')


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'image', 'title')


class MessageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    project = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
