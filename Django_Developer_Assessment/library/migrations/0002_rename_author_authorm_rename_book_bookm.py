# Generated by Django 4.2.5 on 2023-12-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='author',
            new_name='authorm',
        ),
        migrations.RenameModel(
            old_name='book',
            new_name='bookm',
        ),
    ]
