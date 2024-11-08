import sys

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
    "X": coordonne['X'],
    "Y": coordonne['Y'],
  }
  return data

  ################NgonIni

if __name__ =="__main__":
  # srcImage = "data/data1.png"
  if(len(sys.argv))> 1:
    srcImage = sys.argv[1]
  text = pytesseract.image_to_string(Image.open(srcImage))
  print(getResult(text))
