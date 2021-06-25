from django.test import TestCase
from traffic.models import InputAccidentInformation, FactAccidentVehicle


class SetupDbTest(TestCase):

    def test_input(self):
        q = InputAccidentInformation.objects.first()
        self.assertTrue(q)

    def test_dwh(self):
        q = FactAccidentVehicle.objects.first()
        self.assertTrue(q)


