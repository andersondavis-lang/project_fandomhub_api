# Generated by Django 5.0.1 on 2024-06-04 18:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_anime_is_recommended'),
        ('persons', '0004_alter_person_alternate_names_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffAnime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True, verbose_name='available')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='updated at')),
                ('anime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_anime', to='animes.anime')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_anime', to='persons.person')),
            ],
            options={
                'verbose_name': 'staff anime',
                'verbose_name_plural': 'staff animes',
                'ordering': ['pk'],
            },
        ),
        migrations.AddConstraint(
            model_name='staffanime',
            constraint=models.UniqueConstraint(fields=('person_id', 'anime_id'), name='unique_staff_anime'),
        ),
    ]
