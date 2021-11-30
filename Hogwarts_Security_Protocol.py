# import libraries and modules
from sense_hat import SenseHat
import time
from time import sleep
from signal import pause
import send_email                                # import send_email.py

sensor = SenseHat()                              # instantiate SenseHat object
sensor.flip_v()                                  # flip the display vertically
sensor.low_light = True                          # turn on low light mode
sensor.set_imu_config(False, False, True)        # disable compass, disable gyroscope, enable accelerometer  

while True:
    accel_only = sensor.get_accelerometer_raw()  # get accelerometer data
    roll = accel_only['x']                       # get x-axis roll data
    #pitch = accel_only['y']
    #yaw = accel_only['z']
    roll = abs(roll)                             # get absolute value of roll
    if roll > 0.10:                              # if roll is greater than 0.20
        sensor.show_message("!! Email Sent !!", text_colour=[255, 0, 0]) # display message
        send_email.main()              # send email stating that device was tampered with
        sensor.clear()                           # clear the display
        sensor.show_message("!! STEP AWAY !!", text_colour=[0, 255, 0]) # display message    
    print(sensor.accelerometer_raw)              # print accelerometer data for visualization
    time.sleep(0.5)                              # wait for 0.5 seconds

   
