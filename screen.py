# Как сделать снимок экрана на Python
# В терминале установите библиотеку
# pillow командой 
# pip install pillow
from PIL import ImageGrab

screen = ImageGrab.grab()
screen.save('screenshot.png','PNG')

# @endgmPythON