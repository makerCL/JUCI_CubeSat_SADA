from machine import Pin
from time import sleep

class stepper:
    def __init__ (self, IN1, IN2, IN3, IN4):
        self.IN1 = Pin(IN1, Pin.OUT)
        self.IN2 = Pin(IN2, Pin.OUT)
        self.IN3 = Pin(IN3, Pin.OUT)
        self.IN4 = Pin(IN4, Pin.OUT)
        self.pins = [self.IN1, self.IN2, self.IN3, self.IN4]
        self.CCW_seq = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
        self.CW_seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

    def move (target):
        target = target*2048/360
        if step < 0:
            seq = self.CW_seq
            target = -target
        elif step > 0:
            seq = self.CCW_seq
        else:
            return

        curr_step = 0
        while curr_step < target:
            for step in seq:
                for i in range(len(self.pins)):
                    pins[i].value(step[i])
                curr_step += 1
                sleep(0.001)
        print("Made it to target position: ",target)


if __name__ == "__main__":
    right_m = stepper(21,20,19,18)
    right_m.move(360)
    sleep(2)
    right_m.move(-360)
    sleep(2)