import serial
import pygame
from pygame.locals import *

pygame.init()

# Check the the Arduino IDE to make sure the COM port is correct!
arduino = serial.Serial('COM5', 9600, timeout=.1)
screen = pygame.display.set_mode((225, 225))


def parse_serial() -> str:
    """ Reads the serial and returns it as a friendly string. """
    serial_reading = arduino.readline()[:-2]  # We remove the new line.
    serial_reading = str(serial_reading)[2:-1]  # We convert from bytes to string and remove the b''.
    return serial_reading


run = True
img = pygame.image.load('ir_remote.png')
positions = {
    'CH-':  ( 88,  38),
    'CH':   (112,  38),
    'CH+':  (138,  38),
    '|<<':  ( 88,  62),
    '>>|':  (112,  62),
    '>|':   (138,  62),
    '-':    ( 88,  84),
    '+':    (112,  84),
    'EQ':   (138,  84),
    '0':    ( 88, 106),
    '100+': (112, 106),
    '200+': (138, 106),
    '1':    ( 88, 127),
    '2':    (112, 127),
    '3':    (138, 127),
    '4':    ( 88, 151),
    '5':    (112, 151),
    '6':    (138, 151),
    '7':    ( 88, 174),
    '8':    (112, 174),
    '9':    (138, 174)
}

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(img, (0, 0))

    remote = parse_serial()

    if remote != '':
        pygame.draw.circle(screen, (255, 0, 0), positions[remote], 10)

    pygame.display.flip()
