# Generated by Django 3.2.16 on 2023-03-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.TextField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='descripton_long',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
