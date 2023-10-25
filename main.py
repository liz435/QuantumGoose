import sys
sys.path.append('lib')
import Goose
import serial

import time
from time import sleep


goose = Goose.Goose(button_pin = 18, DC_dir1 = [3, 5,7,11],
                    DC_dir2=[13, 15,19,21],
                    DC_enable = [29, 31,33,35],
                    pairs= [[29, 31], [33, 25]])
goose.gpio_setup()
goose.DC_stop()

#sleep(4)

def main():
    while True:
        
       
           
        button_released = goose.button_released()

        if button_released:
            goose.mount_mode(goose.switch_mode())
            

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 2000000)
    ser.reset_input_buffer()
    main()