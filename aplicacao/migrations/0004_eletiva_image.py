# Generated by Django 5.0.6 on 2024-07-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0003_eletiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='eletiva',
            name='image',
            field=models.ImageField(null=True, upload_to='news_images/'),
        ),
    ]
