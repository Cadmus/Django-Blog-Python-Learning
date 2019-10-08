# Generated by Django 2.2.6 on 2019-10-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191003_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_author_sugg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='reading_time',
            field=models.IntegerField(default=1, verbose_name='Reading time'),
        ),
    ]
