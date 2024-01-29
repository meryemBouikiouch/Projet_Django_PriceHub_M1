from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from .models import Phone  # Importez votre modèle ici

class ProductSearchTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Créer des données de test
        Phone.objects.create(identifiant=uuid.uuid4(),phone_name="GalaxyS8+", brand="Samsung")
        Phone.objects.create(identifiant=uuid.uuid4(),phone_name="iPhoneX", brand="Apple")
        # Ajoutez autant de produits que nécessaire pour couvrir vos tests

    def test_search_phone(self):
        # Test de la fonction de recherche
        response = self.client.get('/telephones/', {'q': 'Galaxy'})
        self.assertContains(response, "GalaxyS8+")
        self.assertNotContains(response, "iPhoneX")

class UserLoginTestCase(TestCase):
    def setUp(self):
        # Créer un utilisateur de test
        self.username = "testuser"
        self.password = "testpassword"
        User.objects.create_user(username=self.username, password=self.password)

    def test_valid_login(self):
        # Connexion avec des identifiants valides
        response = self.client.post(reverse('log_in'), {'username': self.username, 'password': self.password}, follow=True)
        
        # Vérifier que l'utilisateur est connecté et redirigé vers la page appropriée
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, expected_url=reverse('home'), status_code=302, target_status_code=200)

class NavigationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_navigation_from_home(self):
        # Tester la navigation depuis la page d'accueil
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)

        # Tester le clic sur le bouton téléphone
        response = self.client.get(reverse('telephones'), follow=True)
        self.assertEqual(response.status_code, 200)

        # Tester le clic sur le bouton tableau de bord
        response = self.client.get(reverse('tableaubord'), follow=True)
        self.assertEqual(response.status_code, 200)

        # Tester le clic sur le bouton communauté
        response = self.client.get(reverse('communaute'), follow=True)
        self.assertEqual(response.status_code, 200)
        # Tester le clic sur le bouton histoire
        response = self.client.get(reverse('histoire'), follow=True)
        self.assertEqual(response.status_code, 200)
        # Tester le clic sur le bouton souhaits
        response = self.client.get(reverse('souhaits'), follow=True)
        self.assertEqual(response.status_code, 200)

class ErrorHandlingTestCase(TestCase):

    def test_page_not_found(self):
        # Tenter d'accéder à une URL inexistante
        response = self.client.get('/Pc/')
        self.assertEqual(response.status_code, 404)

        # Vérifier la présence d'un message d'erreur spécifique
        self.assertContains(response, "Erreur 404 : Page Non Trouvée", status_code=404)