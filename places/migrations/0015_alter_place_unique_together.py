# Generated by Django 3.2.16 on 2023-03-20 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_auto_20230315_1237'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('title', 'lat', 'lng')},
        ),
    ]