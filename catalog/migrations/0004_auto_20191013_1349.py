# Generated by Django 2.2.6 on 2019-10-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191012_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmreview',
            name='image_source',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filmreview',
            name='description',
            field=models.CharField(max_length=700),
        ),
    ]
