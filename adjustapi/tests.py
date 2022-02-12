import unittest
import requests
from rest_framework import status

class TestData(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/'

    def test_first_api_case(self):
        response = requests.get(self.url
                                + """?date__lte=2017-06-01&group_by=country\
&group_by=channel&ordering=-clicks&limit=impressions&limit=clicks""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 25)

    def test_second_api_case(self):
        response = requests.get(self.url
                                + """?date__range=2017-05-01,2017-05-31\
&ordering=date&os=ios&group_by=date&limit=installs""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 15)

    def test_third_api_case(self):
        response = requests.get(self.url
                                + """?date__lte=2017-06-01&country=US\
&group_by=os&ordering=-revenue&limit=revenue""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 2)

    def test_fourth_api_case(self):
        response = requests.get(self.url
                                + """?country=CA&group_by=channel&cpi=cpi&\
limit=spend&ordering=-cpi""")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 4)