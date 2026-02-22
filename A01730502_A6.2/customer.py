"""
Módulo para la gestión de clientes (Customers).
Permite crear, eliminar, mostrar y modificar información de clientes
con persistencia en archivos JSON.
"""

import json
import os


class Customer:
    """Clase que representa la abstracción de un Cliente."""

    def __init__(self, filename='data/customer.json'):
        """Inicializa el gestor de clientes con un archivo específico."""
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        """Crea el archivo si no existe para evitar errores de lectura."""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def create_customer(self, customer_id, name, email):
        """Registra un nuevo cliente en el sistema."""
        customers = self.get_all_customers()
        # Caso negativo: ID duplicado
        if any(c['id'] == customer_id for c in customers):
            print(f"Error: El ID {customer_id} ya existe.")
            return False

        customers.append({
            "id": customer_id,
            "name": name,
            "email": email
        })
        self._save_data(customers)
        return True

    def get_all_customers(self):
        """Lee los clientes del archivo manejando datos corruptos."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            # Req 5: Mostrar error y continuar ejecución
            print(f"Error: Datos inválidos en {self.filename}.")
            return []

    def delete_customer(self, customer_id):
        """Elimina un cliente por su ID."""
        customers = self.get_all_customers()
        new_list = [c for c in customers if c['id'] != customer_id]
        if len(new_list) == len(customers):
            print(f"Error: Cliente {customer_id} no encontrado.")
            return False
        self._save_data(new_list)
        return True

    def _save_data(self, data):
        """Persiste los datos en el archivo JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
