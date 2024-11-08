import csv
import json
import sys
import os

def generate_csv(input_file, output_file="output.csv"):
    # Charger les données JSON depuis le fichier d'entrée
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Vérifier si le fichier existe déjà pour gérer les en-têtes
    file_exists = os.path.isfile(output_file)

    # Ouvrir le fichier en mode ajout ("a") pour ne pas écraser les données existantes
    with open(output_file, mode="a", newline="") as file:
        if data and isinstance(data, list):
            # Utiliser les clés du premier élément pour les en-têtes
            headers = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # Écrire les en-têtes seulement si le fichier n'existe pas encore
            if not file_exists:
                writer.writeheader()
            
            # Ajouter les nouvelles données à la suite
            writer.writerows(data)

if __name__ == "__main__":
    # Vérifier si le fichier d'entrée JSON est passé en argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        generate_csv(input_file)
    else:
        print("Erreur : aucun fichier d'entrée fourni")
