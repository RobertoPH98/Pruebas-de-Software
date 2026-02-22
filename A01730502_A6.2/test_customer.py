"""Pruebas unitarias para la clase Customer."""

import unittest
import os
from customer import Customer


class TestCustomer(unittest.TestCase):
    """Pruebas para la gestión de clientes."""

    def setUp(self):
        """Configura un archivo de prueba temporal."""
        self.test_file = 'data/test_customer.json'
        self.manager = Customer(self.test_file)

    def tearDown(self):
        """Limpia el archivo de prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_customer_duplicate_id(self):
        """Caso Negativo 1: Intentar crear un cliente con ID duplicado."""
        self.manager.create_customer(1, "Juan", "juan@test.com")
        result = self.manager.create_customer(1, "Pedro", "pedro@test.com")
        self.assertFalse(result)

    def test_delete_non_existent_customer(self):
        """Caso Negativo 2: Intentar eliminar un ID que no existe."""
        result = self.manager.delete_customer(999)
        self.assertFalse(result)

    def test_corrupt_json_file(self):
        """Caso Negativo 3: Manejo de archivo JSON mal formado."""
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("formato_invalido")
        data = self.manager.get_all_customers()
        self.assertEqual(data, [])
