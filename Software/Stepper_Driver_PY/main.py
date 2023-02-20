from machine import Pin
from time import sleep

CW = False

P21 = Pin(21, Pin.OUT)
P20 = Pin(20, Pin.OUT)
P19 = Pin(19, Pin.OUT)
P18 = Pin(18, Pin.OUT)

pins = [P21, P20, P19, P18]

CCW_seq = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
CW_seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


if CW:
    seq = CCW_seq
else:
    seq = CW_seq

while True:
    for step in seq:
        for i in range(len(pins)):
            pins[i].value(step[i])
            sleep(0.001)
