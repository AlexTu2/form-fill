import keyboard
import pynput

from pynput.keyboard import Key, Controller
kb = Controller()

def read_file(file):
    f = open(file, "r")
    clean_input = []

    for line in f:
        if not line.strip():
            continue
            #print(line)
        if line:
            #print(line.strip())
            clean_input.append(line.strip().lower())

    f.close()

    return clean_input

def form_fill(input):
    for i in input:
        kb.type('%s\t' % (i))

    keyboard.press_and_release('enter')

def main():
    #Read input file
    clean_input = read_file("input.txt")

    #Fill form
    #form_fill(clean_input)

    #Add hotkey to call form_fill
    keyboard.add_hotkey('f2', form_fill, args=(clean_input,))
    keyboard.wait('esc')
    print("done")

if __name__ == "__main__":
    main()
