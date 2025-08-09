from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author
from rest_framework.authtoken.models import Token


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user for authenticated actions
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # comment the next 2 lines if you want to use session authentication
        self.token = Token.objects.create(user=self.user) 
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create author and books
        self.author = Author.objects.create(name="Author One")
        self.book1 = Book.objects.create(title="A Book", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="B Book", publication_year=2021, author=self.author)

        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_requires_auth(self):
        response = self.client.post(self.list_url, {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(self.list_url, {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book_requires_auth(self):
        response = self.client.put(self.detail_url(self.book1.id), {
            "title": "Updated Title",
            "publication_year": 2025,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.put(self.detail_url(self.book1.id), {
            "title": "Updated Title",
            "publication_year": 2025,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ["B Book", "A Book"])
