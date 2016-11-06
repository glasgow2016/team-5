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
                #get the distance of cloest thing to sensor
                dis = distance()

                #if someoneis close
                if dis <= 20.00:

                        #set up a qrcode
                        qr = qrcode.QRCode(
                            version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=10,
                            border=4,
                        )

                        #check if the qrcode is a code for the website home or a post
                        if postId == "website":
                                qr.add_data(domain + '/')
                                qr.make(fit=True)
                        else:
                                #create qrcode for the postId made unique by the time
                                qr.add_data(domain + "/posts/" + postId + '/' + str(time.time()))
                                qr.make(fit=True)

                        #save qr code as an image
                        img = qr.make_image()
                        with open(postId + '.png', 'wb') as f:
                            img.save(f)
                        f.close()

                        #display the picture for 5 seconds after person has moved away
                        while dis <= 20.00:
                                
                                pygame.init()
                                picture=pygame.image.load( postId + '.png')
                                pygame.display.set_mode(picture.get_size())
                                main_surface = pygame.display.get_surface()
                                main_surface.blit(picture, (0,0))
                                pygame.display.update()
                                time.sleep(5)
                                dis  = distance()

                        #stop showing the
                        pygame.quit()
                        os.remove(postId + '.png')

                #delay between getting new distance
                time.sleep(0.1)


def destroy():
        GPIO.cleanup()

def run():
        if __name__ == "__main__":
                setup()
                try:
                        loop()
                except KeyboardInterrupt:
                        destroy()
