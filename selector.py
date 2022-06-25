import keyboard
import time
import os



def sys_run(args):
    os.system(args)

def updated(curr, old):
    if (curr != old):
        return True
    return False

def update_sel(sel):
    if (sel >= len(options)): sel = 0
    if (sel < 0): sel = len(options) - 1
    return sel


options = [
    "Settings",
    "Login",
    "Help"
]


selected = 0
old_sel = selected

sys_run("clear")
print(options[selected])

while True:
    if (keyboard.is_pressed("q")):
        exit(0)

    if (keyboard.is_pressed("ENTER")):
        print("=== ENTER ===") # TODO

    if (keyboard.is_pressed(keyboard.KEY_UP)): 
        selected -= 1
    elif (keyboard.is_pressed(keyboard.KEY_DOWN)):
        selected += 1;

    if (updated(selected, old_sel)):
        sys_run("clear")
        selected = update_sel(selected)
        print(options[selected]) #  + " | " + str(selected)
        old_sel = selected
    
    time.sleep(0.1)

