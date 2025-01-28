import time
from adafruit_circuitplayground import cp

data_smoothing = 10

while True:
    x, y, z = cp.acceleration
    x, y, z = x*data_smoothing, y*data_smoothing, z*data_smoothing
    x, y, z = int(x), int(y), int(z)
    X, Y, Z = x/data_smoothing, y/data_smoothing, z/data_smoothing
    print((X, Y, Z))

    time.sleep(0.01)
