from unittest import TestCase

from agency_api.models import AboutCompany
from agency_api.serializers import CompanySerializer, MessageSerializer


class CompanySerializerTestCase(TestCase):
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
        data = CompanySerializer([company_1, company_2], many=True).data
        expected_data = [
            {
                'id': company_1.id,
                'projects': company_1.projects,
                'date_of_creation': company_1.date_of_creation,
                'awards': company_1.awards,
            },
            {
                'id': company_2.id,
                'projects': company_2.projects,
                'date_of_creation': company_2.date_of_creation,
                'awards': company_2.awards,
            }
        ]
        self.assertEqual(expected_data, data)


class SendMessageSerializerTestCase(TestCase):
    def test_get(self):
        message = {
            'name': 'NAME',
            'phone': '+996995995719',
            'email': 'example@gmail.com',
            'project': 'PROJECT'
        }

        data = MessageSerializer(message).data
        expected_data = {
            'name': 'NAME',
            'phone': '+996995995719',
            'email': 'example@gmail.com',
            'project': 'PROJECT'
        }

        self.assertEqual(expected_data, data)
