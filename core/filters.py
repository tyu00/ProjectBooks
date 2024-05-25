from django_filters.rest_framework import FilterSet, filters
from .models import Book


class BookFilter(FilterSet):
    author = filters.CharFilter(label='Автор', lookup_expr='icontains')
    title = filters.CharFilter(label='название', lookup_expr='icontains')
    public_date = filters.DateFilter(field_name='publication_date', lookup_expr='lte', label='Дата публикации')

    class Meta:
        model = Book
        fields = ['title', 'author']
