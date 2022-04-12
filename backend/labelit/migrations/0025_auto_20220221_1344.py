# Generated by Django 3.1.7 on 2022-02-21 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labelit', '0024_entitylabel_source_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitylabel',
            name='source_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_labels', to='labelit.label'),
        ),
    ]
