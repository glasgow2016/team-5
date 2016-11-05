#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import qrcode
import pygame
import Tkinter
import os

TRIG = 11
ECHO = 12
piId = "1"


def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

def distance():
        GPIO.output(TRIG, 0)
        time.sleep(0.000002)

        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)

        
        while GPIO.input(ECHO) == 0:
                a = 0
        time1 = time.time()
        while GPIO.input(ECHO) == 1:
                a = 1
        time2 = time.time()

        during = time2 - time1
        return during * 340 / 2 * 100

def loop():
        while True:
                dis = distance()
                if dis <= 10.00:
                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                        )
                        
                        qr.add_data("www.google.co.uk")# + '/' + str(time.time()))
                        qr.make(fit=True)

                        img = qr.make_image()
                        with open(piId + '.png', 'wb') as f:
                            img.save(f)
                        f.close()

                        while dis <= 10.00:
                                

                                pygame.init()
                                picture=pygame.image.load( piId + '.png')
                                pygame.display.set_mode(picture.get_size())
                                main_surface = pygame.display.get_surface()
                                main_surface.blit(picture, (0,0))
                                pygame.display.update()
                                time.sleep(1)
                                dis  = distance()
                                
                        pygame.quit()
                        os.remove(piId + '.png')
                
                                
                time.sleep(1)


def destroy():
        GPIO.cleanup()

if __name__ == "__main__":
        setup()
        try:
                loop()
        except KeyboardInterrupt:
                destroy()
