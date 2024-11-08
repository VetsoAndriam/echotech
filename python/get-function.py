import subprocess

ID_DEFAULT = "P5_1"
NOM_DEFAULT = "P5"
ILL_LICITE_DEFAULT = "licite"
TYPE_DEFAULT = "gratuit"
RANG_DEFAULT = 1
MARQUE_DEFAULT = "Renault"
MODELE_DEFAULT = "Scenic"
COULEUR_DEFAULT = "rouge"
PLAQUE_DEFAULT = "PH046EZ"
HEURE_DEFAULT = "2024-11-07T15:23:40Z"
Y_DEFAULT = 43.45774505
X_DEFAULT = 6.48790391

# Fichier get-horaire
get_horaires_path = 'get-horaires.py'
files_get_horaires = subprocess.run(['python',get_horaires_path], capture_output=True, text=True)
HEURE = files_get_horaires.stdout

print(HEURE)

# Fichier get-infos-path

# get_cars_info_path = 'get-car-infos.py'
#
# argument = 'AL-126-PR'
# commande = [get_cars_info_path,argument]
# message = "python " + " ".join(commande)
# print(message)
# files_get_infos_car = subprocess.run(message, capture_output=True, text=True)
# result_get_infos_car = files_get_infos_car.stdout
# print('result_get_infos_car',result_get_infos_car)



# Preparation JSON
json = {
    "ID": "P5_1",
    "nom": "P5",
    "ill-licite": "licite",
    "type": "gratuit",
    "rang": 1,
    "marque": "Renault",
    "modele": "Scenic",
    "couleur": "rouge",
    "plaque": "PH046EZ",
    "heure": "2024-11-07T15:23:40Z",
    "y": 43.45774505,
    "x": 6.48790391
}
