# Generated by Django 3.1.7 on 2021-07-14 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("labelit", "0010_timedtranscript_timedtranscriptsegment"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="timed_transcript",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="labelit.timedtranscript",
            ),
        ),
        migrations.AddField(
            model_name="timedtranscriptsegment",
            name="start_time",
            field=models.FloatField(
                default=0.0,
                verbose_name="The start time relative to beginning of audio",
            ),
            preserve_default=False,
        ),
    ]
