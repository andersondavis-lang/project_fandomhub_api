# Generated by Django 5.0.1 on 2024-03-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_alter_anime_name_alter_manga_name'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='animes',
            field=models.ManyToManyField(through='playlists.PlaylistAnime', to='contents.anime'),
        ),
        migrations.AddField(
            model_name='playlistanime',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('watching', 'Watching'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('dropped', 'Dropped'), ('plan_watch', 'Plan to Watch')], db_index=True, default='pending', max_length=20, verbose_name='Status'),
        ),
    ]
