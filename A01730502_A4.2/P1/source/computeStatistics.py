"""
Programa para calcular estadísticas descriptivas (Media, Mediana, Moda,
Desviación Estándar y Varianza) a partir de un archivo de texto.
"""

import sys
import time


def read_data(file_path):
    """Lee el archivo y extrae solo los números válidos."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                val = line.strip()
                if not val:
                    continue
                try:
                    numbers.append(float(val))
                except ValueError:
                    print(f"Error de dato inválido: '{val}' no es un número.")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        return None
    return numbers


def calculate_mean(data):
    """Calcula la media aritmética."""
    total = 0.0
    count = 0
    for num in data:
        total += num
        count += 1
    return total / count if count > 0 else 0


def calculate_median(data):
    """Calcula la mediana."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    return sorted_data[mid]


def calculate_mode(data):
    """Calcula la moda (el valor más frecuente)."""
    if not data:
        return 0
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    
    max_freq = 0
    for freq in counts.values():
        if freq > max_freq:
            max_freq = freq
            
    modes = [val for val, freq in counts.items() if freq == max_freq]
    return modes[0]  # Retorna el primer valor encontrado


def calculate_variance(data, mean):
    """Calcula la varianza poblacional."""
    n = len(data)
    if n == 0:
        return 0
    sum_sq_diff = 0.0
    for num in data:
        sum_sq_diff += (num - mean) ** 2
    return sum_sq_diff / n


def main():
    """Función principal para coordinar el cálculo y salida."""
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    data = read_data(file_name)

    if data is None or len(data) == 0:
        print("No se encontraron datos válidos para procesar.")
        return

    # Cálculos
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    std_dev = variance ** 0.5
    elapsed_time = time.time() - start_time

    # Preparar resultados
    results = (
        f"--- Estadísticas: {file_name} ---\n"
        f"Media: {mean}\n"
        f"Mediana: {median}\n"
        f"Moda: {mode}\n"
        f"Desviación Estándar: {std_dev}\n"
        f"Varianza: {variance}\n"
        f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
    )

    # Mostrar en pantalla
    print(results)

    # Guardar en archivo
    with open("StatisticsResults.txt", "w", encoding='utf-8') as res_file:
        res_file.write(results)


if __name__ == "__main__":
    main()