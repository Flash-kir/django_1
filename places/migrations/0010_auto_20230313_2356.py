# Generated by Django 3.2.16 on 2023-03-13 20:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20230313_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='descripton_long',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]
