"""Pruebas unitarias para la clase Reservation."""

import unittest
import os
from reservation import Reservation


class TestReservation(unittest.TestCase):
    """Pruebas para el ciclo de vida de las reservaciones."""

    def setUp(self):
        """Configuración de archivos de prueba."""
        self.test_file = 'data/test_reservations.json'
        self.manager = Reservation(self.test_file)

    def tearDown(self):
        """Limpieza de archivos temporales."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_cancel_non_existent_reservation(self):
        """Caso Negativo 4: Intentar cancelar un ID que no existe."""
        result = self.manager.cancel_reservation(999)
        self.assertFalse(result)

    def test_reservation_file_corruption(self):
        """Caso Negativo 5: Manejo de archivo JSON corrupto (Req 5)."""
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("!!!invalid_json!!!")
        data = self.manager.get_all_reservations()
        self.assertEqual(data, [])
