import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.direction = digitalio.Direction.INPUT
button_B.pull = digitalio.Pull.DOWN

def main():
    while True:
        led.value = button_B.value
        print(button_B.value)
        time.sleep(.2)

main()
