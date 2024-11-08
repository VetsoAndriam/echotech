import subprocess
import sys
import json 
ID_DEFAULT = "P5_1"
NOM_DEFAULT = "P5"
ILL_LICITE_DEFAULT = "licite"
TYPE_DEFAULT = "gratuit"
RANG_DEFAULT = 1
MARQUE = "Renault"
MODELE = "Scenic"
COULEUR_DEFAULT = "rouge"
argumentPlaque = "PH046EZ"
HEURE = "2024-11-07T15:23:40Z"
Y = 43.45774505
X = 6.48790391

def get_horaire(srcImage):
  ######### Fichier get-horaire
  get_horaires_path = 'get-horaires.py'
  commande = [get_horaires_path, srcImage]
  message = "python " + " ".join(commande)
  files_get_horaires = subprocess.run(message, capture_output=True, text=True)
  output = files_get_horaires.stdout
  allFiles = eval(output)
  HEURE = allFiles['heure']
  X = allFiles['X']
  Y = allFiles['Y']


def car_info(argument):
  ########## Fichier get-infos-car

  get_cars_info_path = 'get-car-infos.py'

  argumentPlaque = argument
  commande = [get_cars_info_path,argumentPlaque]
  message = "python " + " ".join(commande)
  files_get_infos_car = subprocess.run(message, capture_output=True, text=True)
  output = files_get_infos_car.stdout
  allVoitures = eval(output)
  MARQUE = allVoitures['marque']
  MODELE = allVoitures['modele']
  

  # Preparation JSON
  data = {
    "ID": ID_DEFAULT,
    "nom": NOM_DEFAULT,
    "ill-licite": ILL_LICITE_DEFAULT,
    "type": TYPE_DEFAULT,
    "rang": RANG_DEFAULT,
    "marque": MARQUE,
    "modele": MODELE,
    "couleur": COULEUR_DEFAULT,
    "plaque": argumentPlaque,
    "heure": HEURE,
    "y": Y,
    "x": X
  }
  
  with open("fichier.json", "w", encoding="utf-8") as fichier:
    json.dump(data, fichier, ensure_ascii=False, indent=4)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    input_file = sys.argv[1]
    get_horaire(sys.argv[1])
    print(car_info(sys.argv[2]))

