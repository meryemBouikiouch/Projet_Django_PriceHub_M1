import os
import django
from django.conf import settings
from django.test.utils import get_runner

# Indique à Django où se trouve le fichier settings.py de votre projet
os.environ['DJANGO_SETTINGS_MODULE'] = 'PHUb.settings'

# Charge les paramètres de configuration Django
django.setup()

# Obtient le test runner
TestRunner = get_runner(settings)

# Exécute les tests
test_runner = TestRunner()
failures = test_runner.run_tests(['api.tests.Test_models', 'api.tests.Test_urls', 'api.tests.Test_views'])

if failures:
    raise SystemExit(failures)
