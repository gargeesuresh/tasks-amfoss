from PIL import Image
from PIL import ImageColor
new = Image.open('oswald.png')
new.rotate(270).save('oswald.png')
new = Image.open('oswald.png')
new = new.convert('1')
new.save('oswald.png')
