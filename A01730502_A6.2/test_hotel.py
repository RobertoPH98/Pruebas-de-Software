"""
Módulo de pruebas unitarias para la clase Hotel.
Incluye casos de prueba negativos para validar la robustez del sistema.
"""

import unittest
from hotel import Hotel


class TestHotelNegative(unittest.TestCase):
    """Pruebas unitarias para casos negativos del sistema de hoteles."""

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        self.hotel_manager = Hotel('data/test_hotels.json')

    def test_delete_non_existent_hotel(self):
        """Prueba que no se puede eliminar un hotel que no existe."""
        # Suponiendo que el ID 999 no existe
        result = self.hotel_manager.delete_hotel(999)
        self.assertFalse(
            result,
            "No debería ser posible eliminar un hotel inexistente")

    def test_invalid_json_handling(self):
        """Prueba el manejo de archivos con formato JSON corrupto (Req 5)."""
        # Escribimos basura en el archivo de prueba
        with open('data/test_hotels.json', 'w', encoding='utf-8') as f:
            f.write("esto_no_es_un_json")

        # El método display debería manejar el error y retornar lista vacía
        hotels = self.hotel_manager.display_hotel_info()
        self.assertEqual(
            hotels, [],
            "Debe retornar lista vacía ante JSON inválido")

# ... continuar con los demás casos
