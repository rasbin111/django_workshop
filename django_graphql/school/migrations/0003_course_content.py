# Generated by Django 5.2 on 2025-04-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_course_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
