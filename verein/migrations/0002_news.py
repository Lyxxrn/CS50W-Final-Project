# Generated by Django 4.0.5 on 2022-06-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verein', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999999999999999999999)),
                ('content', models.CharField(max_length=999999999999999999999999999999999999)),
                ('image', models.CharField(max_length=5000)),
                ('time', models.CharField(max_length=1000)),
            ],
        ),
    ]
