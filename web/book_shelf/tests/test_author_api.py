from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from book_shelf.models.author import Author


class AuthorAPITests(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(firstname='a', lastname='b')

    def test_author_list(self):
        """
        Test author list
        """
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('firstname'), self.author.firstname)
        self.assertEqual(response.data[0].get('lastname'), self.author.lastname)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_retrive(self):
        """
        Test author detail
        """
        url = reverse('author-detail', args=[self.author.uuid])
        response = self.client.get(url, format='json')
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data.get('firstname'), self.author.firstname)
        self.assertEqual(response.data.get('lastname'), self.author.lastname)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_create(self):
        """
        Test author create
        """
        url = reverse('author-list')
        data = {'firstname': 'abc', 'lastname': 'def'}
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
        new_author = Author.objects.filter(uuid=response.data.get('uuid')).first()
        self.assertEqual(new_author.firstname, response.data.get('firstname'))
        self.assertEqual(new_author.lastname, response.data.get('lastname'))
