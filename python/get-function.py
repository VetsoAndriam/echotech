import subprocess

# Fichier get-horaire
get_horaires_path = 'get-horaires.py'
files_get_horaires = subprocess.run(['python',get_horaires_path], capture_output=True, text=True)
result_get_horaires = files_get_horaires.stdout

# Fichier get-infos-path

get_cars_info_path = 'get-car-infos.py'

argument = '22-AAA-22'
commande = [get_cars_info_path,argument]
message = "python " + " ".join(commande)
print(message)
    # get_car_infos_path = 'get-car-infos.py'
    # argument = '22-AAA-22'
    #
    # command = [get_car_infos_path, argument]
    # message = "python " + " ".join(command)
    # print(message)
    # files_get_infos_car = subprocess.run(message, capture_output=True, text=True)
    # result_get_infos_car = files_get_infos.stdout
    # print(result_get_infos_car)



