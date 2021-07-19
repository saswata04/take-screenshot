'''
INSTALLATION:
pip install pyscreenshot
pip install Pillow
pip install keyboard
'''

# import modules
import pyscreenshot as ps
import keyboard
import random
import string


# To generate random string
def generateRandomString():
    # length of the string
    N = 8
    result = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))
    return result


def takeScreenShot(msg):
    # capture the screen
    img = ps.grab()
    # display the captured screenshot
    img.show()
    # save the screenshot
    img.save(f"pictures/{generateRandomString()}.png")
    print(msg)


# create desired hotkey
keyboard.add_hotkey("ctrl+alt+p", takeScreenShot, args=("Screen captured!",))

while True:
    # keyboard.read_key() -> reads which key a user has pressed on the keyboard
    if keyboard.read_key() == "esc":
        print("You pressed esc")
        break

