# Generated by Django 4.2.5 on 2023-11-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_merge_0005_phone_new_price_0008_alter_souhaits_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('souhait_commun', models.CharField(max_length=255)),
                ('personnes', models.ManyToManyField(related_name='groupes', to='api.souhaits')),
            ],
        ),
    ]