# Generated by Django 4.2.5 on 2023-11-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_souhaits_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souhaits',
            name='status',
            field=models.CharField(choices=[('En cours de traitement', 'En cours de traitement'), ('Clôturé', 'Clôturé')], default='En cours de traitement', max_length=50),
        ),
    ]
