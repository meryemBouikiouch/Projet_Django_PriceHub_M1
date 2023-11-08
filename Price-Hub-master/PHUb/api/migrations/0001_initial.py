# Generated by Django 4.2.5 on 2023-11-08 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('identifiant', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('phone_name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.URLField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=4)),
                ('reviewUrl', models.URLField()),
                ('totalReviews', models.IntegerField()),
                ('os', models.CharField(max_length=20)),
                ('inches', models.FloatField()),
                ('resolution', models.CharField(max_length=20)),
                ('battery', models.IntegerField()),
                ('battery_type', models.CharField(max_length=20)),
                ('ram_GB', models.IntegerField()),
                ('announcement_date', models.DateField()),
                ('weight_g', models.IntegerField()),
                ('storage_GB', models.IntegerField()),
                ('video_720p', models.BooleanField()),
                ('video_1080p', models.BooleanField()),
                ('video_4K', models.BooleanField()),
                ('video_8K', models.BooleanField()),
                ('video_30fps', models.BooleanField()),
                ('video_60fps', models.BooleanField()),
                ('video_120fps', models.BooleanField()),
                ('video_240fps', models.BooleanField()),
                ('video_480fps', models.BooleanField()),
                ('video_960fps', models.BooleanField()),
                ('price_USD', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
