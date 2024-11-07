import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

if len(sys.argv) < 2:
    print("Erreur : veuillez fournir une plaque d'immatriculation francaise en entrée.")
    sys.exit(1)


input_text = sys.argv[1]


driver = webdriver.Chrome()  

try:
    # Accéder à la page cible
    driver.get("https://www.oscaro.com/renault-scenic-iv-1-5-dci-110-cv-55861-0-t")  

    time.sleep(0.5)
    
    cookies_button = driver.find_element(By.CLASS_NAME, "popin-close")
    cookies_button.click()

    time.sleep(0.5)

    modify_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    modify_button.click()

    time.sleep(0.5)

    input_field = driver.find_element(By.ID, "vehicle-input-plate")  
    input_field.send_keys(input_text)

    time.sleep(0.5)

    ok_button = driver.find_element(By.CLASS_NAME, "btn-submit")
    ok_button.click()

    time.sleep(0.5)
    
    cookies_button = driver.find_element(By.CLASS_NAME, "popin-close")
    cookies_button.click()

    time.sleep(0.5)

    label = driver.find_element(By.CLASS_NAME, "vehicle-label")
    label_text = label.text  
    print("Marque et modèle :", label_text)
   
    time.sleep(1)

finally:
    
    driver.quit()
