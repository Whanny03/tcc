# Generated by Django 5.0.6 on 2024-07-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0002_imgcarrossel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eletiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
