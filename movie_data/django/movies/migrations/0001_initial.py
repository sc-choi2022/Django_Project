# Generated by Django 3.2.7 on 2022-05-25 17:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField()),
                ('runtime', models.IntegerField()),
                ('video', models.CharField(max_length=100)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('users_mymovie', models.ManyToManyField(related_name='movies_mymovie', to=settings.AUTH_USER_MODEL)),
                ('users_wish', models.ManyToManyField(related_name='movies_wish', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(related_name='otts', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(related_name='keywords', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(related_name='genres', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(related_name='directors', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movies', models.ManyToManyField(related_name='certifications', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.CharField(max_length=200)),
                ('movies', models.ManyToManyField(related_name='actors', to='movies.Movie')),
            ],
        ),
    ]
