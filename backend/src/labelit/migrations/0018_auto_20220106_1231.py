# Generated by Django 3.1.7 on 2022-01-06 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("labelit", "0017_auto_20210826_1134"),
    ]

    operations = [
        migrations.CreateModel(
            name="EntityLabel",
            fields=[
                (
                    "label_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="labelit.label",
                    ),
                ),
                (
                    "start_offset",
                    models.IntegerField(
                        verbose_name="start offset of the entity in the document text"
                    ),
                ),
                (
                    "end_offset",
                    models.IntegerField(
                        verbose_name="end offset of the entity in the document text"
                    ),
                ),
            ],
            bases=("labelit.label",),
        ),
        migrations.CreateModel(
            name="EntityTask",
            fields=[
                (
                    "task_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="labelit.task",
                    ),
                ),
            ],
            bases=("labelit.task",),
        ),
        migrations.AlterField(
            model_name="annotation",
            name="document",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="annotations",
                to="labelit.document",
            ),
        ),
    ]
