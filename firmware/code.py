import digitalio
from board import *
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# A simple neat keyboard demo in circuitpython
buttonpins = [D0]

# the keyboard object!
kbd = Keyboard(usb_hid.devices)

# our array of button objects
buttons = []

toggle = True

# make all pin objects, make them inputs w/pullups
for pin in buttonpins:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP   
    buttons.append(button)
 
print("Waiting for button presses")

while True:
    # check each button
    for button in buttons:
        if (not button.value):   # pressed?
            i = buttons.index(button)
            
            print("Button #%d Pressed" % i)

            # type the keycode!
            # k = buttonkeys[i]    # get the corresp. keycode
            if toggle == True:
                kbd.press(Keycode.EIGHT, Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND)
                toggle = False
                # go to SHOE CAM.
            else: 
                kbd.press(Keycode.NINE, Keycode.CONTROL, Keycode.OPTION, Keycode.COMMAND)
                toggle = True
                # go BACK.
            # Use this line for key combos kbd.press(k, controlkey)
            kbd.release_all()

            while (not button.value):
                pass  # wait for it to be released!
    time.sleep(0.01)















