# Generated by Django 4.2.5 on 2023-12-20 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_author_authorm_rename_book_bookm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorm',
            old_name='adresss',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='bookm',
            old_name='publication_year',
            new_name='pb_year',
        ),
    ]