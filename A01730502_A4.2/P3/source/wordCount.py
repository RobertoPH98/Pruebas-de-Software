"""
Programa para contar la frecuencia de palabras en un archivo de texto.
Maneja errores de lectura y proporciona el tiempo total de ejecución.
"""

import sys
import time


def read_words(file_path):
    """Lee el archivo y extrae todas las palabras."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Separar por espacios y limpiar espacios en blanco
                line_words = line.strip().split()
                words.extend(line_words)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        return None
    except Exception as error: # pylint: disable=broad-exception-caught
        print(f"Error inesperado al leer el archivo: {error}")
        return None
    return words


def count_word_frequencies(word_list):
    """Cuenta la frecuencia de cada palabra usando un diccionario manual."""
    frequencies = {}
    for word in word_list:
        # Limpiar puntuación básica si es necesario (opcional)
        clean_word = word.strip('.,?!"();:').lower()
        if clean_word:
            frequencies[clean_word] = frequencies.get(clean_word, 0) + 1
    return frequencies


def main():
    """Función principal para coordinar el conteo de palabras y la salida."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    
    words = read_words(file_name)

    if words is None:
        return

    # Cálculo de frecuencias
    frequencies = count_word_frequencies(words)
    
    # Ordenar resultados por frecuencia (descendente) o alfabéticamente
    sorted_words = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

    elapsed_time = time.time() - start_time

    # Preparar resultados
    results_list = []
    results_list.append(f"--- Conteo de Palabras: {file_name} ---")
    results_list.append(f"{'PALABRA':<20} {'FRECUENCIA':<10}")
    results_list.append("-" * 30)

    for word, count in sorted_words:
        results_list.append(f"{word:<20} {count:<10}")

    results_list.append("-" * 30)
    results_list.append(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")

    # Preparar salida final
    final_output = "\n".join(results_list)
    
    # Mostrar en pantalla
    print(final_output)

    # Guardar en archivo
    with open("WordCountResults.txt", "w", encoding='utf-8') as res_file:
        res_file.write(final_output)


if __name__ == "__main__":
    main()