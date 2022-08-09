from rest_framework.test import APITestCase

from agency_api.models import AboutCompany, Clients, Project
from agency_api.serializers import CompanySerializer, ClientsSerializer, ProjectDetailSerializer


class SendMessageTestCase(APITestCase):
    def test_get(self):
        message = {
            'name': 'NAME',
            'phone': '+996700700700',
            'email': 'example@gmail.com',
            'project': 'PROJECT'
        }

        expected_data = {
            'status': 'OK'
        }

        url = '/api/v1/send_message/'
        response = self.client.post(url, message)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)


class ProjectListTestCase(APITestCase):
    def test_get_1(self):
        project_1 = Project.objects.create(
            title='test_project_1',
            image='test_image.png',
            created='2000-12-31T00:00:00Z',
            description='test_description_1',
            site_url='www.test_site_1.com',
            instagram_url='www.test_instagram_1.com',
            title_url='www.test_title_1.com'
        )
        data = ProjectDetailSerializer(project_1).data
        url = '/api/v1/project_list/1/'
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.data['post'])

    def test_get_2(self):
        project_2 = Project.objects.create(
            title='test_project_2',
            image='test_image.png',
            created='2000-12-31T00:00:00Z',
            description='test_description_2',
            site_url='www.test_site_2.com',
            instagram_url='www.test_instagram_2.com',
            title_url='www.test_title_2.com'
        )
        data = ProjectDetailSerializer(project_2).data
        url = '/api/v1/project_list/2/'
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.data['post'])


class AboutCompanyTestCase(APITestCase):
    def test_get(self):
        company_1 = AboutCompany.objects.create(
            projects='+10',
            date_of_creation='2021-12-21',
            awards='70.00'
        )
        company_2 = AboutCompany.objects.create(
            projects='+30',
            date_of_creation='2011-12-11',
            awards='50.00'
        )
        url = '/api/v1/about/'
        response = self.client.get(url)

        data = CompanySerializer([company_1, company_2], many=True).data

        self.assertEqual(200, response.status_code)
        self.assertEqual(data, response.data)


class ClientsApiTestCase(APITestCase):
    def test_get(self):
        client_1 = Clients.objects.create(
            icon='icons/test_icon.png',
            client_partner='test_client_1',
            date_for_sort='2000-12-31T00:00:00Z'
        )
        client_2 = Clients.objects.create(
            icon='icons/test_icon.png',
            client_partner='test_client_2',
            date_for_sort='2000-12-31T00:00:00Z'
        )
        url = '/api/v1/about/clients_list/'
        response = self.client.get(url)

        data = ClientsSerializer([client_1, client_2], many=True).data

        data_1 = []
        for i in data:
            for j in i:
                if j != 'icon':
                    data_1.append(i[j])
                elif j == 'icon':
                    data_1.append(i[j] is not None)

        expected_data_1 = []
        for k in response.data:
            for p in k:
                if p != 'icon':
                    expected_data_1.append(k[p])
                elif p == 'icon':
                    expected_data_1.append(k[p] is not None)

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_data_1, data_1)