import requests  # Se importa el módulo requests para realizar solicitudes HTTP.
import re        # Se importa el módulo re para trabajar con expresiones regulares.
from collections import Counter  # Se importa la clase Counter del módulo collections para contar elementos.
import os  # Se importa el módulo os para realizar operaciones relacionadas con el sistema operativo.

url = "https://dummyjson.com/quotes"    # Se define la URL de la cual se obtendrán los datos.

response = requests.get(url)    # Se realiza una solicitud HTTP GET a la URL especificada.
data = response.json()  # Se obtiene la respuesta en formato JSON y se convierte a un objeto Python.

quotes = data['quotes'] # Se extraen las citas del objeto JSON.
texts = [quote['quote'] for quote in quotes]    # Se crea una lista que contiene solo los textos de las citas.

excluded_words = ['a', 'an', 'the', 'and', 'but', 'or', 'in', 'on', 'at', 'for', 'to', 'with']  # Se define una lista de palabras que se excluirán del recuento.

# Se crea una lista de listas donde cada sublista contiene las palabras individuales de cada texto en minúsculas.
word_list = [re.findall(r'\b\w+\b', text.lower()) for text in texts]

# Se crea una lista plana de todas las palabras de los textos, excluyendo las palabras en excluded_words.
words = [word for sublist in word_list for word in sublist if word not in excluded_words]

word_counts = Counter(words)    # Se utiliza la clase Counter para contar la frecuencia de cada palabra en la lista de palabras.

top_ten_words = word_counts.most_common(10) # Se obtiene una lista con las diez palabras más comunes y su conteo.

# Imprime un encabezado que indica que se mostrará el top 10 de palabras más repetidas, excluyendo artículos y conectores.
print("Top 10 de palabras más repetidas (excluyendo artículos y conectores):")

for word, count in top_ten_words:   # Se itera sobre las palabras y sus conteos en la lista top_ten_words.
    print(f"{word}: {count}")   # Se muestra cada palabra y su conteo en el formato "palabra: conteo".

# Crear un directorio para almacenar los archivos si no existe
directory = 'archivos_texto'
if not os.path.exists(directory):
    os.makedirs(directory)

for word, count in top_ten_words:
    file_name = f'{directory}/{word}.txt'  # Se forma el nombre del archivo utilizando la palabra actual.
    with open(file_name, 'w') as file:  # Se abre el archivo en modo de escritura.
        file.write(f'La palabra "{word}" se repite {count} veces.\n')  # Se escribe la frase en el archivo.

    # Establecer permisos chmod 400
    os.chmod(file_name, 0o400)  # Se establecen los permisos del archivo como 400.

print("Se han creado los archivos de texto con los nombres de las palabras más repetidas.")
