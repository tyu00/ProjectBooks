from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book


class BookTests(APITestCase):
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Test Book', 'author': 'Test Author', 'publication_date': '2024-05-25', 'genre': 'Test Genre'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    class BookTests(APITestCase):
        def test_get_book_list(self):
            url = reverse('book-list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_get_single_book(self):
            book = Book.objects.create(title='Test Book', author='Test Author', publication_date='2024-05-25',
                                       genre='Test Genre')
            url = reverse('book-detail', kwargs={'pk': book.pk})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    class BookTests(APITestCase):
        def test_update_book(self):
            book = Book.objects.create(title='Test Book', author='Test Author', publication_date='2024-05-25',
                                       genre='Test Genre')
            url = reverse('book-detail', kwargs={'pk': book.pk})
            data = {'title': 'Updated Title'}
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            book.refresh_from_db()
            self.assertEqual(book.title, 'Updated Title')

        def test_partial_update_book(self):
            book = Book.objects.create(title='Test Book', author='Test Author', publication_date='2024-05-25',
                                       genre='Test Genre')
            url = reverse('book-detail', kwargs={'pk': book.pk})
            data = {'title': 'Partial Update'}
            response = self.client.patch(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            book.refresh_from_db()
            self.assertEqual(book.title, 'Partial Update')

    class BookTests(APITestCase):
        def test_delete_book(self):
            book = Book.objects.create(title='Test Book', author='Test Author', publication_date='2024-05-25',
                                       genre='Test Genre')
            url = reverse('book-detail', kwargs={'pk': book.pk})
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Book.objects.count(), 0)
