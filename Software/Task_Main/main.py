from machine import Pin, WDT
from time import sleep
import cotask
import task_share
from stepper import stepper
from atdc import atdc
import _thread


# =============================================================================
# TASK 1 Dual Stepper Motor Driving
# =============================================================================
def Task_1():

    while True:
        # State 0: State Director  
        if state1.get() == 0:
            if mode1.get() == 1:
                state1.put(1)
            elif mode1.get() == 2:
                state1.put(2)
            elif mode1.get() == 3:
                state1.put(3)
            elif mode1.get() == 4:
                state1.put(4)
            elif mode1.get() == 5:
                state1.put(5)
            elif mode1.get() == 6:
                state1.put(6)
            else:
                raise ValueError("Invalid State in Task 1")

        # State 1: Zero Motor 1    
        elif state1.get() == 1:
            complete = mot1.zero(z_flag1.get())
            if complete:
                state1.put(0)
                mode1.put(2)
            else:
                pass
            
        # State 2: Sleep & Sun Tracking Mode Check
        elif state1.get() == 2:
            if track_mode1.get() == 0:
                state1.put(0)
                mode1.put(3)
            elif track_mode1.get() == 1:
                state1.put(0)
                mode1.put(4)
            elif track_mode1.get() == 2:
                state1.put(0)
                mode1.put(5)
            else:
                raise ValueError("Invalid Tracking Mode")

        # State 3: Zero Tracking Mode
        elif state1.get() == 3:
            lost = mot1.zero_tracking()
            if lost:
                state1.put(0)
                mode1.put(1)
            else:
                pass

        # State 4: Constant Uptick Mode
        elif state1.get() == 4:
            reset = mot1.uptick_tracking()
            if reset:
                state1.put(0)
                mode1.put(1)
            else:
                pass

        # State 5: Memory Mode
        elif state1.get() == 5:
            mot1.memory_tracking()
            state1.put(0)
            mode1.put(6)

        # State 6: Dead/Sleep Mode
        elif state1.get() == 6:
            pass


# =============================================================================
# TASK 2 Dual Photodiode ADC Reading
# =============================================================================
def Task_2():
    pass

def button1_cb (GP01):
    print("System Zeroed")
    z_flag1.put(1)
    

def button2_cb (GP02):
    print("System Zeroed")
    z_flag2.put(1)
    

if __name__ == "__main__":
    adc1 = atdc(26,17,16)
    adc2 = atdc(27,2,3)

    mot1 = stepper(21,20,19,18,adc1)
    mot2 = stepper(10,11,12,13,adc2)

    wdt = WDT(timeout=2000)
    # Need to implement wdt.feed() in select locations 

    GP01 = Pin(1,Pin.IN,Pin.PULL_UP)
    GP01.irq(trigger=Pin.IRQ_FALLING, handler=button1_cb)
    GP02 = Pin(2,Pin.IN,Pin.PULL_UP)
    GP02.irq(trigger=Pin.IRQ_FALLING, handler=button2_cb)

    mode1 = task_share.Share ('B', thread_protect = False, name = "Panel 1 Mode-States")
    track_mode1 = task_share.Share ('B', thread_protect = False, name = "Panel 1 Sun Tracking Mode")
    state1 = task_share.Share ('B', thread_protect = False, name = "Panel 1 State")
    z_flag1 = task_share.Share ('B', thread_protect = False, name = "Motor 1 Zeroed Flag")

    mode2 = task_share.Share ('B', thread_protect = False, name = "Panel 2 Mode-States")
    track_mode2 = task_share.Share ('B', thread_protect = False, name = "Panel 2 Sun Tracking Mode")
    state2 = task_share.Share ('B', thread_protect = False, name = "Panel 2 State")
    z_flag2 = task_share.Share ('B', thread_protect = False, name = "Motor 2 Zeroed Flag")

    mode1.put(0)
    track_mode1.put(0)
    state1.put(0)
    z_flag1.put(0)

    mode2.put(0)
    track_mode2.put(0)
    state2.put(0)
    z_flag2.put(0)

    task2 = _thread.start_new_thread(Task_2,())