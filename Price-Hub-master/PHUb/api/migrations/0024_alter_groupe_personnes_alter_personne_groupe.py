# Generated by Django 4.2.5 on 2023-12-01 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_groupe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='personnes',
            field=models.ManyToManyField(related_name='groupes_groupe', to='api.souhaits'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='groupe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnes_personne', to='api.groupe'),
        ),
    ]
