# Generated by Django 3.2.16 on 2023-03-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_details_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='details_url',
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
