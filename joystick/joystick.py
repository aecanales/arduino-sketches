import serial
import pygame

pygame.init()

# Check the the Arduino IDE to make sure the COM port is correct!
arduino = serial.Serial('COM5', 9600, timeout=.1)
screen = pygame.display.set_mode((300, 300))


def parse_serial() -> list:
    """ Reads the serial string (in format "X Y Button") and returns them as list of ints. """
    serial_reading = arduino.readline()[:-2]  # We remove the new line.
    serial_reading = str(serial_reading)[2:-1]  # We convert from bytes to string and remove the b''.
    return list(map(lambda x: int(x), serial_reading.split()))  # We return a list with the values as ints.


def position(joy_x, joy_y) -> tuple:
    x, y = joy_x / 1023 * 300, joy_y / 1023 * 300
    return tuple(map(lambda value: int(round(value)), (x, y)))


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    joystick = parse_serial()

    if joystick != []:  # Only draw when the serial is actually receiving information.
        screen.fill((0, 0, 0))
        pygame.draw.circle(
            screen, (255, 255, 255) if joystick[2] else (255, 0, 0),
            position(joystick[0], joystick[1]),
            15
            )

    pygame.display.flip()
