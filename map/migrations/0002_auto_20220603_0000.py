# Generated by Django 3.0 on 2022-06-03 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='town',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='num_cases',
            new_name='population',
        ),
    ]