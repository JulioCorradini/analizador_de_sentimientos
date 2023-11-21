import pandas as pd

#Ruta del archivo CSV
ruta_arcivo_CSV = 'C:/Users/Nadia/Desktop/Proyectos_de_programacion/Programas hechos con Visual Studio/Analizador_de_sentimientos/test.csv'

#Leer el archivo CSV con Pandas
datos = pd.read_csv(ruta_arcivo_CSV, encoding='ISO-8859-1', header=None)
print(datos.head(10))

#Asignar nombres a las columnas
##columnas = ['Sentimiento', 'ID', 'Fecha', 'Query', 'Usuario', 'Tweet']
##datos.columns = columnas

#Crear un nuevo Data Frame con las columnas Sentimiento y Tweet
##dataset = datos[['Sentimiento', 'Tweet']]

# Mapear los valores de sentimiento a "negative" o "positive" utilizando loc
##dataset.loc[:, 'Sentimiento'] = dataset['Sentimiento'].map({0: 'negative', 4: 'positive'})

# Crear la lista de tuplas
##training_data = [(fila['Tweet'], fila['Sentimiento']) for _, fila in dataset.iterrows()]

##training_data = [
##    ("I love the content on the Analytics Lane blog, articles are fantastic.", "positive"),
##    ("The code does not work, it gave me an error when executing it.", "negative"),
##    ("I love this product!", "positive"),
##    ("This movie was terrible.", "negative"),
##    ("The weather is nice today.", "positive"),
##    ("I feel so sad about the news.", "negative"),
##    ("It's just an average book.", "neutral")
##]