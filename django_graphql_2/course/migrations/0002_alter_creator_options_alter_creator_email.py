# Generated by Django 5.2 on 2025-04-07 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='creator',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
