from machine import Pin
from time import sleep

class stepper:
    def __init__ (self, IN1, IN2, IN3, IN4, adc):
        self.IN1 = Pin(IN1, Pin.OUT) # Step pin 1
        self.IN2 = Pin(IN2, Pin.OUT) # Step pin 2
        self.IN3 = Pin(IN3, Pin.OUT) # Step pin 3
        self.IN4 = Pin(IN4, Pin.OUT) # Step pin 4
        self.adc = adc               # ADC port for photodiode readings
        self.pins = [self.IN1, self.IN2, self.IN3, self.IN4]      # Pin array
        self.CCW_seq = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]  # Bit sequence for counter-clockwise spin
        self.CW_seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]   # Bit sequence for clockwise spin
        self.direct_light = 500      # Tested number that represents direct sunlight output of photodiode
        self.pos = 0                 # Absolute position of stepper motor currently
        self.pos1 = 0                # The position of the first value less than direct light in orbit
        self.pos2 = 0                # The position of the last value less than direct light in orbit
        self.first_time = True       # Flag if position 1 has already been determined

# =============================================================================
# Move: Input a target step value for motor to move to.
# =============================================================================
    def move (self,target):
        if target < 0:
            seq = self.CW_seq
            target = -target
        elif target > 0:
            seq = self.CCW_seq
        else:
            pass
        
        curr_step = 0
        while curr_step < target:
            for step in seq:
                for i in range(len(self.pins)):
                    self.pins[i].value(step[i])
                    sleep(0.001)
                curr_step += 1
                self.pos = self.pos + 1

# =============================================================================
# Zero: Find the zero position of the stepper motor with a hall sensor.
# =============================================================================
    def zero (self,z_flag):
        if z_flag == 0:
            self.move(-1)
            return False
        else:
            self.pos = 0
            return True
    
# =============================================================================
# Uptick Tracking: Track the sun by continuing to increase the tick until lost.
# =============================================================================
    def uptick_tracking(self):
        curr_light = self.adc.read()
        if curr_light <= self.direct_light:
            if self.first_time:
                self.pos1 = self.pos
                self.first_time = False
            else:
                self.pos2 = self.pos
            return False
        elif curr_light > self.direct_light and self.pos <= 1024:
            self.move(8)
            return False
        else:
            self.first_time = True
            self.best_pos = (self.pos1 + self.pos2)/2
            return True

# =============================================================================
# Memory Tracking: Remember the best position value from uptick counting and
# go to that value and stay there. 
# =============================================================================
    def memory_tracking(self):
        self.move(self.best_pos)
        
