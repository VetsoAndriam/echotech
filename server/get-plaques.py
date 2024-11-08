import cv2
import requests
import os
import time
import argparse  # Importer argparse pour gérer les arguments

# Fonction principale pour traiter la vidéo
def process_video(video_path, frame_interval=200):
    # Clé API et URL de l'API d'image
    api_key = '4795d2ee880b6a0ccaf3af0d22a6655b38eb41de'
    url = "https://api.platerecognizer.com/v1/plate-reader/"

    # Créer un dossier temporaire pour les images extraites
    os.makedirs("video_frames", exist_ok=True)

    # Ouvrir la vidéo
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    extracted_count = 0

    # Liste pour stocker les plaques détectées (en éliminant les doublons)
    plates_detected = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Extraire une image toutes les `frame_interval`
        if frame_count % frame_interval == 0:
            # Augmenter la résolution de l'image
            resized_frame = cv2.resize(frame, (1280, 720))

            # Améliorer la qualité de l'image avec un filtre de contraste et de netteté
            gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
            enhanced_frame = cv2.equalizeHist(gray)  # Augmenter le contraste
            resized_frame = cv2.cvtColor(enhanced_frame, cv2.COLOR_GRAY2BGR)

            # Rogner la partie inférieure de l'image (où les plaques sont souvent situées)
            height, width = resized_frame.shape[:2]
            cropped_frame = resized_frame[int(height * 0.5):height, 0:width]  # Conserver la moitié inférieure

            # Enregistrer l'image temporairement pour inspection
            image_path = f"video_frames/frame_{extracted_count}.jpg"
            cv2.imwrite(image_path, cropped_frame)

            # Envoyer l'image à l'API de reconnaissance de plaques
            with open(image_path, 'rb') as img_file:
                files = {'upload': img_file}
                headers = {'Authorization': f'Token {api_key}'}
                response = requests.post(url, headers=headers, files=files)

            # Vérifier la réponse de l'API
            if response.status_code == 201:
                result = response.json()
                if result.get('results'):  # Si des plaques sont détectées
                    plates_in_image = [r['plate'] for r in result['results']]
                    plates_detected.update(plates_in_image)  # Ajouter les plaques à l'ensemble (sans doublons)
                    print(f"Image {extracted_count} : Plaques détectées - {plates_in_image}")
                else:
                    print(f"Image {extracted_count} : Aucune plaque détectée.")
            else:
                print(f"Erreur avec la requête : {response.status_code} -", response.text)

            # Supprimer l'image après l'upload pour économiser de l'espace
            os.remove(image_path)
            extracted_count += 1

            # Délai pour éviter le throttling
            time.sleep(2)  # Délai de 2 secondes entre les requêtes

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

    # Retourner les résultats des plaques détectées
    print(f"\nNombre total de plaques détectées : {len(plates_detected)}")
    return sorted(list(plates_detected))  # Retourner la liste triée des plaques

# Fonction pour analyser les arguments de la ligne de commande
def main():
    parser = argparse.ArgumentParser(description="Traitement de vidéo pour la reconnaissance de plaques")
    parser.add_argument('video_path', type=str, help="Le chemin vers la vidéo à traiter")
    parser.add_argument('--frame_interval', type=int, default=200, help="L'intervalle entre les frames à extraire (par défaut 200)")

    args = parser.parse_args()

    # Appeler la fonction de traitement de la vidéo
    plates = process_video(args.video_path, args.frame_interval)

    # Affichage des résultats ou autre utilisation de la liste
    print("\nRésultats finaux des plaques détectées (sans doublons) :")
    for plate in plates:
        print(plate)

    # Retourner la liste des plaques si nécessaire (par exemple, pour une API)
    return plates

if __name__ == "__main__":
    main()