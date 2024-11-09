import pytesseract
from PIL import Image
from PIL import Image, ImageEnhance, ImageFilter


image_path = "/Users/hunglv/Library/Mobile Documents/com~apple~CloudDocs/Scanned PDf/Khi ban dang mo/Khi ban Dang Mo Ghi Nguoi Khac Dang No Luc - 79.jpg"
image = Image.open(image_path)
enhancer = ImageEnhance.Contrast(image)
image_enhanced = enhancer.enhance(2)
image_filtered = image_enhanced.filter(ImageFilter.SHARPEN)

text = pytesseract.image_to_string(image_filtered, lang="vie")
print(text)
