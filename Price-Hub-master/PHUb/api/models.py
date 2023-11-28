from django.db import models

class Phone(models.Model):
    identifiant = models.CharField(max_length=20, primary_key=True)
    brand = models.CharField(max_length=100)
    phone_name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    image = models.URLField(max_length=200)
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    reviewUrl = models.URLField(max_length=200)
    totalReviews = models.IntegerField()
    os = models.CharField(max_length=20)
    inches = models.FloatField()
    resolution = models.CharField(max_length=20)
    battery = models.IntegerField()
    battery_type = models.CharField(max_length=20)
    ram_GB = models.IntegerField()
    announcement_date = models.DateField()
    weight_g = models.IntegerField()
    storage_GB = models.IntegerField()
    
    # Modifications pour autoriser NULL pour les champs vidéo
   # Modifications pour autoriser NULL pour les champs vidéo
    video_720p = models.BooleanField(null=True)
    video_1080p = models.BooleanField(null=True)
    video_4K = models.BooleanField(null=True)
    video_8K = models.BooleanField(null=True)
    video_30fps = models.BooleanField(null=True)
    video_60fps = models.BooleanField(null=True)
    video_120fps = models.BooleanField(null=True)
    video_240fps = models.BooleanField(null=True)
    video_480fps = models.BooleanField(null=True)
    video_960fps = models.BooleanField(null=True)

    price_USD = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.phone_name