# Generated by Django 2.2.6 on 2019-10-14 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20191013_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmreview',
            old_name='category',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='filmreview',
            old_name='characters',
            new_name='performers',
        ),
    ]