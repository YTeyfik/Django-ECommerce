# Generated by Django 3.0.8 on 2020-08-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produce', '0005_auto_20200828_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]