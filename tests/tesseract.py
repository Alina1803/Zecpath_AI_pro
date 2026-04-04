import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"

img = Image.open(r"D:\Zecser\img.jpeg")
text = pytesseract.image_to_string(img)

print(text)