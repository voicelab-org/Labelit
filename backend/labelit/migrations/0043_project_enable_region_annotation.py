# Generated by Django 3.1.7 on 2022-11-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labelit", "0042_auto_20221013_1059"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="enable_region_annotation",
            field=models.BooleanField(default=False),
        ),
    ]
