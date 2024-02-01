# Generated by Django 5.0.1 on 2024-02-01 22:24

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(help_text='Example: Comedy', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Premiered',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(help_text='Example: Winter 2024', max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Premiered',
                'verbose_name_plural': 'Premiered',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(help_text='Example: PG-13 - Teens 13 or older', max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('name_eng', models.CharField(help_text='Example: MAPPA', max_length=255, unique=True)),
                ('name_jpn', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='studios/', verbose_name='Image')),
                ('established', models.DateField()),
            ],
            options={
                'verbose_name': 'Studio',
                'verbose_name_plural': 'Studios',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('tag', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('title_eng', models.CharField(max_length=255, unique=True, verbose_name='Title - English')),
                ('title_jpn', models.CharField(max_length=255, unique=True, verbose_name='Title - Japanese')),
                ('image', models.ImageField(upload_to='contents/', verbose_name='Image')),
                ('synopsis', models.TextField(verbose_name='Synopsis')),
                ('episodes', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Episodes')),
                ('duration', models.CharField(help_text='Format: "25 min. per ep."', max_length=20, verbose_name='Duration')),
                ('release', models.DateField(verbose_name='Release')),
                ('category', models.CharField(choices=[('P', 'Pending'), ('O', 'ONA'), ('S', 'Series'), ('M', 'Movies')], default='P', max_length=1, verbose_name='Category')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Airing'), ('F', 'Finished'), ('U', 'Upcoming')], default='P', max_length=1, verbose_name='Status')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.genre')),
                ('premiered_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.premiered')),
                ('rating_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.rating')),
                ('studio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.studio')),
                ('url_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.url')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
            },
        ),
    ]
