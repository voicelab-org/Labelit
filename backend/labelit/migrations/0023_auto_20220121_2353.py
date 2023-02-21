# Generated by Django 3.1.7 on 2022-01-21 23:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("labelit", "0022_auto_20220121_2340"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="completeddocumentannotatorpair",
            unique_together={("annotator", "document", "batch")},
        ),
    ]
