"""
Licencia:       Apache
Organización:   UNIR - Master DevOps
Programa:       Ordenador de Palabras
Descripción:    Lee una lista de palabras desde un archivo,
                elimina duplicados opcionalmente (yes/no) y
                ordena la lista segun parametro (asc/desc).
Colaboradores:  Darwin Cuenca, Oswaldo Solano, [], []
Fecha:          14-oct-2024
"""

#* Importación de librerías
import os
import sys

#* Definición de constantes
DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True

#* Definición de función: sort_list
# Descripción: Ordena una lista de palabras
# Parámetros:
#   items: Lista de palabras
#   ascending: Indica si el ordenamiento es ascendente/descendente
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"It can't order {type(items)}")

    return sorted(items, reverse=(not ascending))

#* Definición de función: remove_duplicates_from_list
# Descripción: Elimina duplicados de una lista de palabras
# Parámetros:
#   items: Lista de palabras
def remove_duplicates_from_list(items):
    return list(set(items))

#* Definición de main
# Descripción: Función principal del script
if __name__ == "__main__":
    filename = DEFAULT_FILENAME # Nombre del archivo
    remove_duplicates = DEFAULT_DUPLICATES # valor booleano para eliminar duplicados, default es False
    ascending = DEFAULT_ASCENDING # valor booleano para orden ascendente, default es True

    # Si se pasan argumentos al script, se toman como nombre de archivo, si se eliminan duplicados y el orden
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending = sys.argv[3].lower() == "asc"
    else:
        print("The file must be indicated as the first argument")
        print("The second argument indicates whether you want to eliminate duplicates (yes/no)")
        print("The third argument indicates the sorting order (asc/desc)")
        sys.exit(1)

    # Se verifica si el archivo existe, si no existe se toma una lista por defecto
    print(f"The words from the file will be read {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = [] # Lista de palabras
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip()) # Se eliminan los saltos de línea
    else:
        print(f"File {filename} don't exist") # Se imprime un mensaje de error si el archivo no existe
        word_list = ["ravenclaw", "gryffindor", "slytherin", "ravenclaw", "hufflepuff", "slytherin"] # Lista por defecto

    # Se eliminan duplicados si se indica
    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Se ordena la lista y se imprime
    print(sort_list(word_list, ascending))
