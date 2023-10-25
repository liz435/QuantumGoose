import RPi.GPIO as GPIO
from time import sleep
import serial

class Goose:
    def __init__(self, button_pin = int,
                DC_dir1 = list[int], 
                DC_dir2=list[int],
                DC_enable = list[int],
                pairs= list[list[int]],
                **kwargs):
        
        self.button_pin = button_pin
        self.DC_dir1 = DC_dir1
        self.DC_dir2 = DC_dir2
        self.DC_enable = DC_enable
        self.pairs = pairs
        self.state = ['stop', 'spin']
        self.index_state = 0
        self.ser = serial.Serial('/dev/ttyACM0', 9600)

    def honk(self):
        print(f"{self.name} honks")
    

    def gpio_setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for i in self.DC_enable, self.DC_dir1, self.DC_dir2:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)

    def entangle(self, pairs= list[list[int]]):
        leng = len(pairs)
        for i in range(leng):
            pairs[i]
        pass
        

    def DC_forward(self):
        GPIO.output(self.DC_dir1, GPIO.HIGH)
        GPIO.output(self.DC_dir2, GPIO.LOW)
        GPIO.output(self.DC_enable, GPIO.HIGH)

    def DC_reverse(self):
        GPIO.output(self.DC_dir1, GPIO.LOW)
        GPIO.output(self.DC_dir2, GPIO.HIGH)
        GPIO.output(self.DC_enable, GPIO.HIGH)
    
    def DC_stop(self):
        GPIO.output(self.DC_enable, GPIO.LOW)

    def geese_spin(self):
        self.DC_forward()
    
    def geese_stop(self, which = int):
        for i in range(len(self.pairs)):
            if which in self.pairs[i]:
                for j in range(len(self.pairs[i])):
                    GPIO.output([self.pairs[i][j]], GPIO.LOW)
                    print(f"Geese {self.pairs[i][j]} stopped")
    

    def button_press(self):
        input_state = GPIO.input(18)
        if input_state == False:
            return True
        
    def button_release(self):
        input_state = GPIO.input(18)
        if input_state == True:
            return True
        

    def button_released(self):
        pressed = False
        if self.index_state == 1:
            self.index_state = -1
            
        if self.button_press() == True :
            pressed = True
        if self.button_release() == True and pressed == True:
            pressed = False
            print("button pressed")
            self.index_state += 1
            return True
        else:
            return False
        

    def switch_mode(self):
        self.mount_mode(self.state[self.index_state])
    
    def mount_mode(self,modes):
        cases = {
            'stop':lambda: self.observation(),
            'spin':lambda: self.spin(),
        }
        code_block = cases.get(modes)
        if code_block is not None:
            code_block()

    def stepper_spin(self):
        self.ser.write(b'start\n')
        

    def stepper_stop(self):
        self.ser.write(b'stop\n')
        
    def listener(self):

        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            print(line)
            return line
    
    def stepper_degree(self,data):
        print(data)
        
        degree = int(data)

        for i in range(0, 360, 45):
            if degree is not None and degree >= i and degree <= i + 45:
                return i + 45

        return None
        
    def determine_goose(self,dgree = int):
        pass


    def observation(self):
        self.stepper_stop()
        data = self.listener()
        self.geese_stop(29)
        c = self.stepper_degree(data)
        print(c)
        
        print("stopped")
        
    def spin(self):
        self.stepper_spin()
        print("spinning")
        

    