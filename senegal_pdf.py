from pdf2image import convert_from_path
import pytesseract
import cv2
from PIL import Image 
import re
import pandas as pd

#Conver pages to images
pdfs = r"./assets/senegal.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save('assets/' + image_name, "JPEG")
    i = i+1  


#Define path to tessaract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
image = cv2.imread('assets/Page_1.jpg')
ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
text = str(pytesseract.image_to_string(thresh1, config='--psm 6'))
text_list = text.splitlines() 

stop = False
positive_cured_death = []
treatment = []
for line in text_list:
    if 'Ace jour' in line:
        positive_cured_death = re.findall('[0-9]+', line)
        stop = True
        continue
    if stop:
        treatment = re.findall('[0-9]+', line)
        break

df = pd.DataFrame({'Cumulative Positive': positive_cured_death[0], 'Cumulative Cured' : positive_cured_death[1], 'Cummulative Deaths': positive_cured_death[2], 'Cummulative Treatment': treatment})
df.to_csv('downloads/senegal_pdf.csv', index=False)

