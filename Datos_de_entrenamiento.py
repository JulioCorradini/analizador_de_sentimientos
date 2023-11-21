import pandas as pd

#Ruta del archivo CSV
##ruta_arcivo_CSV = 'C:/Users/Nadia/Desktop/Proyectos_de_programacion/Programas hechos con Visual Studio/Analizador_de_sentimientos/test.csv'
ruta_archivo_CSV = 'C:/Users/Julio/Desktop/Proyectos_de_programacion/analizador_de_sentimientos/test.csv'

#Leer el archivo CSV con Pandas
datos = pd.read_csv(ruta_archivo_CSV, encoding='ISO-8859-1', header=None, skiprows=1)

#Crear un nuevo Data Frame con las columnas Sentimiento y Tweet
dataset = datos[[1, 2]]

# Crear la lista de tuplas
training_data = [(row[1], row[2]) for _, row in dataset.iterrows()]