# Generated by Django 4.1.1 on 2022-10-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="num_users",
        ),
        migrations.AddField(
            model_name="student",
            name="disability",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
