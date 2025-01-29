# Generated by Django 5.1.2 on 2025-01-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField()),
                ('newsletter_link', models.URLField()),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('dribbble_link', models.URLField()),
                ('behance_link', models.URLField()),
            ],
        ),
    ]
