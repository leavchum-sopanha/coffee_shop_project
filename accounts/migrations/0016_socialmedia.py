# Generated by Django 5.1.2 on 2025-01-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_coffeetopmenu_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialMediaName', models.CharField(max_length=200, null=True)),
                ('socialMediaURL', models.CharField(max_length=200, null=True)),
                ('socialMediaImage', models.ImageField(upload_to='SocialImages')),
            ],
        ),
    ]
