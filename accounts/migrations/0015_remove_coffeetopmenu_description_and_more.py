# Generated by Django 5.1.3 on 2025-01-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeetopmenu',
            name='description',
        ),
        migrations.RemoveField(
            model_name='coffeetopmenu',
            name='url',
        ),
        migrations.AddField(
            model_name='coffeetopmenu',
            name='section_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
