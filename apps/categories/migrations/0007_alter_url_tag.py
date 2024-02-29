# Generated by Django 5.0.1 on 2024-02-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_alter_url_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='tag',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Official Site'), (2, 'Crunchyroll'), (3, 'Netflix'), (4, 'Youtube Acccount'), (5, 'X Account')], default=0, verbose_name='Tag'),
        ),
    ]
