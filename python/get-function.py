import subprocess

ID_DEFAULT = "P5_1"
NOM_DEFAULT = "P5"
ILL_LICITE_DEFAULT = "licite"
TYPE_DEFAULT = "gratuit"
RANG_DEFAULT = 1
MARQUE_DEFAULT = "Renault"
MODELE_DEFAULT = "Scenic"
COULEUR_DEFAULT = "rouge"
argumentPlaque = "PH046EZ"
HEURE = "2024-11-07T15:23:40Z"
Y = 22
X = 10

######### Fichier get-horaire
get_horaires_path = 'get-horaires.py'
files_get_horaires = subprocess.run(['python',get_horaires_path], capture_output=True, text=True)
output = files_get_horaires.stdout
allFiles = eval(output)
HEURE = allFiles['heure']
X = allFiles['X']
Y = allFiles['Y']



# HEURE_DEFAULT = allHoraires['heure']


########## Fichier get-infos-car

get_cars_info_path = 'get-car-infos.py'

argumentPlaque = 'AL-126-PR'
commande = [get_cars_info_path,argumentPlaque]
message = "python " + " ".join(commande)
files_get_infos_car = subprocess.run(message, capture_output=True, text=True)
result_get_infos_car = files_get_infos_car.stdout
print('result_get_infos_car',result_get_infos_car)



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
    "plaque": argumentPlaque,
    "heure": HEURE,
    "y": Y,
    "x": X
}

print('json',json)

