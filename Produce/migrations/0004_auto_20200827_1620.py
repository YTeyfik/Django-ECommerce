# Generated by Django 3.0.8 on 2020-08-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produce', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
