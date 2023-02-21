# Generated by Django 3.1.7 on 2022-04-07 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("labelit", "0033_texteditiontask_validator"),
    ]

    operations = [
        migrations.CreateModel(
            name="NestedCategoricalTask",
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
                (
                    "single_select",
                    models.BooleanField(
                        default=True,
                        verbose_name="\n        If true, the annotator cannot select more than one label.\n        ",
                    ),
                ),
            ],
            bases=("labelit.task",),
        ),
        migrations.CreateModel(
            name="NestedCategoricalLabel",
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
                    "single_child_select",
                    models.BooleanField(
                        default=True,
                        verbose_name="Whether only one child label can be selected at any time",
                    ),
                ),
                (
                    "parent_label",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nested_children_labels",
                        to="labelit.label",
                    ),
                ),
            ],
            bases=("labelit.label",),
        ),
    ]
