from PIL import Image
from pytesseract import pytesseract
from facebook_scraper import get_posts
from facebook_scraper import get_page_info
from facebook_scraper import get_posts_by_search


for post in get_posts_by_search('GetVaccinated'):
    print(post)

#Define path to tessaract.exe
# path_to_tesseract = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Define path to image
# path_to_image = 'C:/tesseract/zambia_img.jpg'

#Point tessaract_cmd to tessaract.exe
# pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
# img = Image.open(path_to_image)

#Extract text from image
# text = pytesseract.image_to_string(img)

# print(text)