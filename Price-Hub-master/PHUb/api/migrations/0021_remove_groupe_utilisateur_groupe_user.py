# Generated by Django 4.2.5 on 2023-11-30 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0020_alter_groupe_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupe',
            name='utilisateur',
        ),
        migrations.AddField(
            model_name='groupe',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]