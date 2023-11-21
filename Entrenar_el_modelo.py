from nltk.classify import NaiveBayesClassifier

from Preprocezado_de_texto import preprocess_text
from Frecuencia_de_palabras import extract_features
from Datos_de_entrenamiento import training_data

# Preprocesamiento de los datos de entrenamiento
preprocessed_training_data = [(preprocess_text(text), label) for text, label in training_data]

# Extracción de características de los datos de entrenamiento
training_features = [(extract_features(text), label) for text, label in preprocessed_training_data]

# Entrenamiento del clasificador Naive Bayes
classifier = NaiveBayesClassifier.train(training_features)