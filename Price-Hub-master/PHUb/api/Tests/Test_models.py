from django.test import TestCase
from api.models import Phone


class PhoneModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Phone.objects.create(
    identifiant='test_id',
    brand='TestBrand',
    phone_name='TestPhone',
    url='https://example.com',
    image='https://example.com/image.jpg',
    rating=4.5,
    reviewUrl='https://example.com/review',
    totalReviews=100,
    os='TestOS',
    inches=6.0,
    resolution='TestResolution',
    battery=3000,
    battery_type='TestBatteryType',
    ram_GB=4,
    announcement_date='2023-01-01',
    weight_g=150,
    storage_GB=128,
    price_USD=500,
    video_720p=True,
    video_1080p=False,
    video_4K=True,  # Assurez-vous de spécifier une valeur pour video_4K
    # ... autres champs de modèle ...
)


    def test_phone_model(self):
        phone = Phone.objects.get(identifiant='test_id')
        self.assertEqual(phone.brand, 'TestBrand')
        # Assurez-vous de tester d'autres champs selon vos besoins
