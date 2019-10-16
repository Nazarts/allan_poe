# Generated by Django 2.2.6 on 2019-10-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(default='none', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(default='none', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FilmReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('premiere', models.DateField()),
                ('review', models.TextField()),
                ('image', models.ImageField(upload_to='film_images')),
                ('image_source', models.URLField()),
                ('description', models.CharField(max_length=700)),
                ('director', models.CharField(max_length=255)),
                ('slug', models.CharField(default='none', max_length=255)),
                ('categories', models.ManyToManyField(to='catalog.Categories')),
                ('characters', models.ManyToManyField(to='catalog.Characters')),
            ],
        ),
    ]
