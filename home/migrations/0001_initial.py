# Generated by Django 3.0.8 on 2020-08-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('fax', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('smtpserver', models.CharField(blank=True, max_length=100)),
                ('smtpemail', models.CharField(blank=True, max_length=100)),
                ('smtppassword', models.CharField(blank=True, max_length=100)),
                ('smtpport', models.CharField(blank=True, max_length=100)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('aboutus', models.TextField(blank=True, max_length=100)),
                ('contact', models.TextField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
