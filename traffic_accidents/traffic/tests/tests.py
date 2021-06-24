from io import StringIO
from django.core.management import call_command
from django.test import TestCase


class SetupDbTest(TestCase):

    def test_setup_db(self):
        out = StringIO()
        call_command('setup_db', stdout=out)
        self.assertIn('Expected output', out.getvalue())
