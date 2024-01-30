# Generated by Django 4.2.5 on 2023-12-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_favori_delete_favoritephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='invitation_status',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='meeting_participants', to='api.souhaits'),
        ),
    ]