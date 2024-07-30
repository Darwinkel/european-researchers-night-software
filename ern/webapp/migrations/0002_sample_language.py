# Generated by Django 5.0.7 on 2024-07-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sample",
            name="language",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other/Unspecified/Prefer not to say")],
                default="nl",
                max_length=2,
            ),
        ),
    ]
