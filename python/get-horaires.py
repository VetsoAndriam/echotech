from PIL import Image
import pytesseract
import re
from datetime import datetime
import json

def getDate(text):
  patternDate = r'\d{4}/\d{2}/\d{2}'
  return re.findall(patternDate, text)[0]

def getHeure(text):
  patternHeure = r'\d{2}:\d{2}:\d{2}'
  return re.findall(patternHeure, text)[0]

def getCoordonne(text):
  patternE = r'E\s(.*?)\s'
  patternN = r'N\s(.*?)\s'
  X = re.findall(patternE, text)[0]
  Y = re.findall(patternN, text)[0]

  coordonne = {
    "X": X,
    "Y": Y
  }
  return coordonne

def getIsoDate(date, heure):

  day, month, year = map(int, date.split('/'))
  hour, minute, second = map(int, heure.split(':'))

  return f"{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}"

def getResult(srcImage):
  date = getDate(srcImage)
  heure = getHeure(srcImage)
  dateIso = getIsoDate(date, heure)
  coordonne = getCoordonne(text)
  data = {
    "heure": dateIso,
    "Y": coordonne['Y'],
    "X": coordonne['X']
  }
  return data

################NgonIni
srcImage = "data/data1.png"

text = pytesseract.image_to_string(Image.open(srcImage))
# print(text)
# date = getDate(text)
# heure = getHeure(text)
# print(getCoordonne(text))
# print(getIsoDate(date, heure))
print(getResult(text))
