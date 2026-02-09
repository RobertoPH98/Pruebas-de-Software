"""
Programa para convertir números de un archivo a sistemas binario y hexadecimal.
Implementa algoritmos de división sucesiva sin usar funciones nativas de Python.
"""

import sys
import time


def read_data(file_path):
    """Lee el archivo y extrae solo los números enteros válidos."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                val = line.strip()
                if not val:
                    continue
                try:
                    # Se asumen números enteros para conversión de base
                    numbers.append(int(float(val)))
                except ValueError:
                    print(f"Error de dato inválido: '{val}' no es un número.")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        return None
    return numbers


def to_binary(num):
    """Convierte un número a binario usando el método de divisiones."""
    if num == 0:
        return "0"
    
    is_negative = num < 0
    num = abs(num)
    binary = ""
    
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
        
    return "-" + binary if is_negative else binary


def to_hexadecimal(num):
    """Convierte un número a hexadecimal usando el método de divisiones."""
    if num == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    is_negative = num < 0
    num = abs(num)
    hexadecimal = ""
    
    while num > 0:
        remainder = num % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        num //= 16
        
    return "-" + hexadecimal if is_negative else hexadecimal


def main():
    """Función principal para coordinar la conversión y salida de datos."""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    data = read_data(file_name)

    if data is None:
        return

    results_list = []
    header = f"{'ITEM':<5} {'NUMBER':<10} {'BINARY':<15} {'HEXADECIMAL':<15}"
    results_list.append(header)
    results_list.append("-" * 45)

    for i, num in enumerate(data, 1):
        bin_val = to_binary(num)
        hex_val = to_hexadecimal(num)
        row = f"{i:<5} {num:<10} {bin_val:<15} {hex_val:<15}"
        results_list.append(row)

    elapsed_time = time.time() - start_time
    footer = f"\nTiempo de ejecución: {elapsed_time:.4f} segundos"
    results_list.append(footer)

    # Preparar salida final
    final_output = "\n".join(results_list)
    
    # Mostrar en pantalla
    print(final_output)

    # Guardar en archivo
    with open("ConversionResults.txt", "w", encoding='utf-8') as res_file:
        res_file.write(final_output)


if __name__ == "__main__":
    main()