# Generated by Django 5.0.6 on 2024-09-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0015_maissobre'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkEletiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
            ],
        ),
    ]
