from django.db import models

class Phone(models.Model):
    identifiant = models.CharField(max_length=20, primary_key=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    phone_name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    image = models.URLField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    reviewUrl = models.URLField(max_length=200, null=True, blank=True)
    totalReviews = models.IntegerField(null=True, blank=True)
    os = models.CharField(max_length=20, null=True, blank=True)
    inches = models.FloatField(null=True, blank=True)
    resolution = models.CharField(max_length=20, null=True, blank=True)
    battery = models.IntegerField(null=True, blank=True)
    battery_type = models.CharField(max_length=20, null=True, blank=True)
    ram_GB = models.IntegerField(null=True, blank=True)
    announcement_date = models.DateField(null=True, blank=True)
    weight_g = models.IntegerField(null=True, blank=True)
    storage_GB = models.IntegerField(null=True, blank=True)
    video_720p = models.BooleanField(null=True, blank=True)
    video_1080p = models.BooleanField(null=True, blank=True)
    video_4K = models.BooleanField(null=True, blank=True)
    video_8K = models.BooleanField(null=True, blank=True)
    video_30fps = models.BooleanField(null=True, blank=True)
    video_60fps = models.BooleanField(null=True, blank=True)
    video_120fps = models.BooleanField(null=True, blank=True)
    video_240fps = models.BooleanField(null=True, blank=True)
    video_480fps = models.BooleanField(null=True, blank=True)
    video_960fps = models.BooleanField(null=True, blank=True)
    price_USD = models.IntegerField(null=True, blank=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.phone_name
# Create your models here.
class HistoriqueVisite(models.Model):
    brand = models.CharField(max_length=100, null=True, blank=True)
    phone_name = models.CharField(max_length=255, null=False, blank=False)
    store_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.brand} - {self.phone_name} - {self.store_name} - {self.location} - {self.prix}"