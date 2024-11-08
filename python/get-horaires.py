from PIL import Image
import pytesseract
import re
import json

def getDate(text):
  patternDate = r'\d{4}/\d{2}/\d{2}'
  return re.findall(patternDate, text)

def getHeure(text):
  patternHeure = r'\d{2}:\d{2}:\d{2}'
  return re.findall(patternHeure, text)

def getCoordonne(text):
  patternE = r'E\s(.*?)\s'
  patternN = r'N\s(.*?)\s'
  X = re.findall(patternE, text)
  Y = re.findall(patternN, text)

  coordonne = {
    "X": X[0],
    "Y": Y[0]
  }
  return coordonne

def getHoraires(srcImage):
  date = getDate(srcImage)
  heure = getHeure(srcImage)
  dateIso = getDateIso



  date =

srcImage = "data/data1.png"

text = pytesseract.image_to_string(Image.open(srcImage))
result = getHoraires(text)
print(getHoraires(text))
