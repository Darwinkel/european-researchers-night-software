# Generated by Django 5.0.7 on 2024-07-20 15:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_sample_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='rating_reconstructed_accuracy',
            new_name='rating_reconstructed_human_accuracy',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='rating_reconstructed_flow',
            new_name='rating_reconstructed_human_flow',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='rating_reconstructed_fluency',
            new_name='rating_reconstructed_human_fluency',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='llm_reconstructed_story',
        ),
        migrations.AddField(
            model_name='sample',
            name='llm_reconstructed_human_story',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='sample',
            name='llm_reconstructed_random_story',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='sample',
            name='rating_reconstructed_random_accuracy',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='sample',
            name='rating_reconstructed_random_flow',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='sample',
            name='rating_reconstructed_random_fluency',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
