from machine import Pin, ADC

class atdc:
    def __init__(self,IN1,OUT1,OUT2):
        self.IN1 = Pin(IN1, Pin.IN)
        self.OUT1 = Pin(OUT1, Pin.OUT)
        self.OUT2 = Pin(OUT2, Pin.OUT)
        self.adc = ADC(self.IN1)
        self.seq1 = [0,0,1,1]
        self.seq2 = [0,1,0,1]
        self.adc.on()

    def read(self):
        self.reading = 0
        for i in range(4):
            self.OUT1.value(self.seq1[i])
            self.OUT2.value(self.seq2[i])
            self.reading = self.adc.read_u16() + self.reading
        avg_read = self.reading/4
        return avg_read

