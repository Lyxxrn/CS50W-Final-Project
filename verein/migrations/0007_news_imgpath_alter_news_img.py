# Generated by Django 4.0.5 on 2022-06-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verein', '0006_alter_news_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='imgpath',
            field=models.CharField(blank=True, max_length=99999999999),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
