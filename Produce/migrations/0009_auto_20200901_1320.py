# Generated by Django 3.0.8 on 2020-09-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produce', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
