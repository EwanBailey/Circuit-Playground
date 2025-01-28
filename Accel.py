import time
from adafruit_circuitplayground import cp


while True:
    x, y, z = cp.acceleration
    x, y, z = x*10, y*10, z*10
    x, y, z = int(x), int(y), int(z)
    X, Y, Z = x/10, y/10, z/10
    print((X, Y, Z))

    time.sleep(0.01)
