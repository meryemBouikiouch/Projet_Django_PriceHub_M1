# Generated by Django 4.1.3 on 2023-11-21 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_historiquevisite_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiquevisite',
            name='date_of_visit',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
