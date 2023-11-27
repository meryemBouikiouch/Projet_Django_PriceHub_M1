from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    video_720p = models.BooleanField()
    video_1080p = models.BooleanField()
    video_4K = models.BooleanField()
    video_8K = models.BooleanField()
    video_30fps = models.BooleanField()
    video_60fps = models.BooleanField()
    video_120fps = models.BooleanField()
    video_240fps = models.BooleanField()
    video_480fps = models.BooleanField()
    video_960fps = models.BooleanField()
    price_USD = models.IntegerField()

    def __str__(self):
        return self.phone_name
# Create your models here.
class HistoriqueVisite(models.Model):
    category= models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    store_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_visit = models.DateField()

    def __str__(self):
        return f"{self.category} -{self.brand} - {self.name} - {self.store_name} - {self.location} - {self.prix}- {self.date_of_visit}"
    from django.db import models
from django.contrib.auth.models import User

class Souhaits(models.Model):
    STATUS_CHOICES = [
        ('En cours de traitement', 'En cours de traitement'),
        ('Clôturé', 'Clôturé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='En cours de traitement')  

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.brand} - {self.name} - {self.phone_number} - {self.status}"


