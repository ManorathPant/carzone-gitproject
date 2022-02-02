# Generated by Django 3.0.7 on 2022-02-01 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220201_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(max_length=100),
        ),
    ]
