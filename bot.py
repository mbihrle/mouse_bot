from pynput import keyboard
import time
from mouse_behaviour.mouse_move import right_mouse_click


def main():
    right_mouse_click()


def on_press(key):
    global run_programm
    global run_loop
    print(key)

    if key == keyboard.Key.enter:
        print('Bot wird gestartet')
        run_loop = True

    if key == keyboard.Key.end and run_loop == False:
        print('Programm wird beendet')
        run_programm = False

    if key == keyboard.Key.end and run_loop:
        print('Bot wird beendet')
        run_loop = False


run_programm = True
run_loop = False
print("Drücke 'Enter' um den Bot zu starten")
print("Drücke 'Ende' um den Bot zu stoppen")
listener = keyboard.Listener(on_press=on_press)
listener.start()
while run_programm:
    if run_loop:
        main()
        time.sleep(60)
listener.stop()
print('Bis zum nächsten Mal! ;-)')
exit()
