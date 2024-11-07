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

    text = pytesseract.image_to_string(Image.open(srcImage))
    date = getDate(text)
    heure = getHeure(text)
    dateIso = getIsoDate(date[0], heure[0])
    coordonne = getCoordonne(text)
    data = {
      "heure": dateIso,
      "Y": coordonne['Y'],
      "X": coordonne['X']
    }
    return data;

srcImage = "data/data1.png"

text = pytesseract.image_to_string(Image.open(srcImage))
print(getCoordonne(text))
