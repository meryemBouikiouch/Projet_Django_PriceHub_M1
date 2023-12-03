# Generated by Django 4.1.3 on 2023-12-03 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_merge_0005_phone_new_price_0008_alter_souhaits_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiquevisite',
            name='prix',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=255)),
                ('store_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date_of_meeting', models.DateField()),
                ('participants', models.ManyToManyField(blank=True, related_name='meeting_participants', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]