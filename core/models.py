from django.db import models


class Book(models.Model):
    title = models.CharField('название', max_length=100)
    author = models.CharField('Автор', max_length=50)
    publication_date = models.DateField('Дата публикации')
    genre = models.CharField('Жанар', max_length=50)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['publication_date']

    def __str__(self):
        return self.title
