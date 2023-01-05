# Generated by Django 3.1.7 on 2022-04-05 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("labelit", "0031_auto_20220316_1537"),
    ]

    operations = [
        migrations.CreateModel(
            name="TextEditionLabel",
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
                    "edited_text",
                    models.TextField(
                        blank=True, default="", verbose_name="the edited document text"
                    ),
                ),
            ],
            bases=("labelit.label",),
        ),
        migrations.CreateModel(
            name="TextEditionTask",
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
    ]
