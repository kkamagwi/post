# Как обрезать картинку при помощи кода?

from PIL import Image
 
image = Image.open('путь/к/изображению.jpg')
image.show()

cropped = image.crop((0, 80, 200, 400))
cropped.save('название_нового_изображения.png')

# @endgmPythON