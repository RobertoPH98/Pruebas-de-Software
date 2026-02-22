import json
import os


class Hotel:
    """Clase para gestionar la información de los hoteles."""

    def __init__(self, filename='data/hotels.json'):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Crea el archivo json si no existe."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def create_hotel(self, hotel_id, name, location, rooms):
        """Registra un nuevo hotel en el archivo JSON."""
        hotels = self.display_hotel_info()
        # Verificar si ya existe para evitar duplicados (puedes usarlo como
        #  caso de prueba)
        hotels.append({
            "id": hotel_id,
            "name": name,
            "location": location,
            "rooms": rooms
        })
        self._save_to_file(hotels)

    def display_hotel_info(self):
        """Lee y retorna la lista de hoteles manejando datos inválidos."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Req 5: Mostrar error y continuar ejecución
            print(f"Error: El archivo {self.filename} contiene datos "
                  "inválidos.")
            return []

    def _save_to_file(self, data):
        """Guarda los datos en el archivo JSON."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    # Implementar también: delete_hotel, modify_hotel...
