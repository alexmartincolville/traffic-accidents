from unittest import TestCase
from django.db import connections
from traffic.models import InputAccidentInformation, InputVehicleInformation, FactAccidentVehicle


class SetupDbTest(TestCase):

    def test_connection(self):
        self.assertIsNot(connections['default'], None)

    def test_input_accidents(self):
        self.assertTrue(InputAccidentInformation.objects.exists())

    def test_input_vehicle(self):
        self.assertTrue(InputVehicleInformation.objects.exists())

    def test_fact(self):
        self.assertTrue(FactAccidentVehicle.objects.exists())
