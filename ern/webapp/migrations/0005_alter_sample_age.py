# Generated by Django 5.0.7 on 2024-07-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_sample_age_alter_sample_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='age',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]