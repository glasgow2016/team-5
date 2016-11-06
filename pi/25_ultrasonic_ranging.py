#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import qrcode
import pygame
import Tkinter
import os

TRIG = 11
ECHO = 12
domain = "52.211.235.179:5000"
postId = "website"


def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
'visitorCentre'
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
                
                if dis <= 50.00:
                        
                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                        )

                        if postId == "website":
                                qr.add_data(domain + '/')
                                qr.make(fit=True)
                        else:
                                qr.add_data(domain + "/posts/" + postId + '/' + str(time.time()))
                                qr.make(fit=True)

                        img = qr.make_image()
                        with open(postId + '.png', 'wb') as f:
                            img.save(f)
                        f.close()

                        while dis <= 50.00:
                                
                                pygame.init()
                                picture=pygame.image.load( postId + '.png')
                                #infoObject = pygame.display.Info()
                                #pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

                                pygame.display.set_mode(picture.get_size())
                                main_surface = pygame.display.get_surface()
                                main_surface.blit(picture, (0,0))
                                pygame.display.update()
                                time.sleep(5)
                                dis  = distance()
                                
                        pygame.quit()
                        os.remove(postId + '.png')
                  
                time.sleep(1)


def destroy():
        GPIO.cleanup()

def run():
        if __name__ == "__main__":
                setup()
                try:
                        loop()
                except KeyboardInterrupt:
                        destroy()
