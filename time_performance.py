import time
import os
import requests
from indexer import indexer
from ingestion import index_folder_contents
# Définir le chemin du dossier contenant les documents
folder_path = 'data'


# Enregistrer le temps de début
start_total_time = time.time()

# Indexation des documents
start_time = time.time()
print("Indexation des documents...")
index_folder_contents(folder_path)
index_time = time.time() - start_time
print(f"Temps d'indexation : {index_time:.2f} secondes")

# Interrogation de l'application
query = "se protéger contre le phishing"
start_time = time.time()
print(f"Interrogation avec la requête : '{query}'")
response = requests.get(f"http://localhost:8000/query-document?query={query}")
query_time = time.time() - start_time
print(f"Temps de réponse : {query_time:.2f} secondes")

# #
# Total = str(float(query) + float(query_time))
# print(f"Temps total d'execution est de; {Total}")

if response.status_code == 200:
    results = response.json()["results"]
    print("Résultats :")
    for doc, score in results:
        print(f"Score : {score:.2f} - Document : {doc[:100]}...")
else:
    print(f"Erreur lors de l'interrogation : {response.text}")

# Calculer et afficher le temps total d'exécution
total_time = time.time() - start_total_time
print(f"Temps total d'exécution : {total_time:.2f} secondes")