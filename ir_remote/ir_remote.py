import serial
import pygame
from pygame.locals import *

img = pygame.image.load('ir_remote.png')

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

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(img, (0, 0))

    remote = parse_serial()

    if remote != '':
        print(remote)

    pygame.display.flip()
