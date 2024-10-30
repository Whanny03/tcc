# Generated by Django 5.0.6 on 2024-09-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0017_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='NossaHistoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='nossa_historia/')),
            ],
        ),
    ]