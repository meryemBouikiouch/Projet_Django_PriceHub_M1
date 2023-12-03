from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    category= models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    store_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
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
    
# class Meeting(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category = models.CharField(max_length=255)
#     store_name = models.CharField(max_length=255)  # Nom du magasin
#     location = models.CharField(max_length=255)  # Lieu
#     date_of_meeting = models.DateField()
#     participants = models.ManyToManyField(Souhaits, related_name='meeting_participants', blank=True)

#     def __str__(self):
#         participant_names = ", ".join(self.participants.values_list('user__username', flat=True).distinct())
#         return f"{self.user.username} - {self.category} - {self.store_name} - {self.location} - {self.date_of_meeting} - Participants: {participant_names}"

class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_of_meeting = models.DateField()
    participants = models.ManyToManyField(Souhaits, related_name='meeting_participants', blank=True)

    def get_participant_names(self):
        return ", ".join(self.participants.values_list('user__username', flat=True).distinct())

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.store_name} - {self.location} - {self.date_of_meeting} - Participants: {self.get_participant_names()}"


