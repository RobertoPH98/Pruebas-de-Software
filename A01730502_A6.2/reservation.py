"""
Módulo para la gestión de Reservaciones.
Vincula clientes con hoteles y gestiona la persistencia en JSON.
"""

import json
import os


class Reservation:
    """Clase para manejar las reservaciones del sistema."""

    def __init__(self, filename='data/reservations.json'):
        """Inicializa el gestor de reservaciones."""
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Crea el archivo de datos si no existe."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def create_reservation(self, customer_id, hotel_id):
        """
        Crea una reservación vinculando un cliente y un hotel.
        Se asume la existencia previa de IDs en sus respectivos archivos.
        """
        reservations = self.get_all_reservations()

        # En una implementación real, aquí validarías contra hotel.py y
        # customer.py
        new_res = {
            "reservation_id": len(reservations) + 1,
            "customer_id": customer_id,
            "hotel_id": hotel_id
        }

        reservations.append(new_res)
        self._save_data(reservations)
        return True

    def cancel_reservation(self, reservation_id):
        """Cancela una reservación existente."""
        reservations = self.get_all_reservations()
        initial_len = len(reservations)
        reservations = [r for r in reservations
                        if r['reservation_id'] != reservation_id]

        if len(reservations) == initial_len:
            print(f"Error: Reservación {reservation_id} no encontrada.")
            return False

        self._save_data(reservations)
        return True

    def get_all_reservations(self):
        """Lee reservaciones manejando posibles errores de formato (Req 5)."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Error: Datos inválidos en {self.filename}.")
            return []

    def _save_data(self, data):
        """Guarda los datos en el archivo JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
