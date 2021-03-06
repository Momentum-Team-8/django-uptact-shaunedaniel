# Generated by Django 3.2.4 on 2021-06-18 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20210617_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
