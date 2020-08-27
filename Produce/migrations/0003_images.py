# Generated by Django 3.0.8 on 2020-08-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produce', '0002_produce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produce.Produce')),
            ],
        ),
    ]