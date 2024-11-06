# Generated by Django 5.0.6 on 2024-08-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0013_delete_sociallinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_url', models.URLField(blank=True, max_length=255, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]