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
    "ID": ID_DEFAULT,
    "nom": NOM_DEFAULT,
    "ill-licite": ILL_LICITE_DEFAULT,
    "type": TYPE_DEFAULT,
    "rang": RANG_DEFAULT,
    "marque": MARQUE_DEFAULT,
    "modele": MODELE_DEFAULT,
    "couleur": COULEUR_DEFAULT,
    "plaque": PLAQUE_DEFAULT,
    "heure": HEURE_DEFAULT,
    "y": Y_DEFAULT,
    "x": X_DEFAULT
}

print('json',json)

