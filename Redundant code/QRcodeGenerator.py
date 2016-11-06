import pygame
import qrcode
import Tkinter
from PIL import Image
import time

piId = "1"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("www.$$$.com")
qr.make(fit=True)

img = qr.make_image()


with open(piId + '.png', 'wb') as f:
    img.save(f)

f.close()

pygame.init()
picture=pygame.image.load("1.png")
pygame.display.set_mode(picture.get_size())
main_surface = pygame.display.get_surface()
main_surface.blit(picture, (0,0))
pygame.display.update()
time.sleep(5)
pygame.quit()
