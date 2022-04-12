# Generated by Django 3.1.7 on 2021-07-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labelit', '0008_document_audio_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timer_inactivity_threshold',
            field=models.IntegerField(default=60000, verbose_name='\n        Delay (ms) past which the timer is paused during annotation\n        '),
        ),
    ]
