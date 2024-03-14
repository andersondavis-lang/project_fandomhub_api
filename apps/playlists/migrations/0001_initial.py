# Generated by Django 5.0.1 on 2024-03-14 19:07

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0007_alter_anime_name_alter_manga_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.CreateModel(
            name='PlaylistAnime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('watching', 'Watching'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('dropped', 'Dropped'), ('plan_watch', 'Plan to Watch')], db_index=True, default='pending', max_length=20)),
                ('is_watched', models.BooleanField(db_index=True, default=False)),
                ('is_favorite', models.BooleanField(db_index=True, default=False)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_animes', to='contents.anime', verbose_name='Anime')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist', verbose_name='Playlist')),
            ],
            options={
                'verbose_name': 'PlaylistAnime',
                'verbose_name_plural': 'PlaylistAnimes',
            },
        ),
        migrations.CreateModel(
            name='PlaylistManga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='Available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('watching', 'Watching'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('dropped', 'Dropped'), ('plan_watch', 'Plan to Watch')], db_index=True, default='pending', max_length=20)),
                ('is_watched', models.BooleanField(db_index=True, default=False)),
                ('is_favorite', models.BooleanField(db_index=True, default=False)),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist_mangas', to='contents.manga', verbose_name='Manga')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist', verbose_name='Playlist')),
            ],
            options={
                'verbose_name': 'PlaylistManga',
                'verbose_name_plural': 'PlaylistMangas',
            },
        ),
    ]
