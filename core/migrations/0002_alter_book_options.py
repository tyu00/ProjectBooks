# Generated by Django 5.0.6 on 2024-05-25 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['publication_date'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
