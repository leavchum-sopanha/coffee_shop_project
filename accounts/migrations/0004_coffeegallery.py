# Generated by Django 5.1.4 on 2025-01-12 08:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_coffee_menu_coffeemenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coffee-gallery')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
