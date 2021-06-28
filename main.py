import pynput
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

def read_file(file):
    f = open(file, "r")
    clean_input = []

    for line in f:
        if not line.strip():
            print(line)
        if line:
            print(line.strip())
            clean_input.append(line.strip())

    f.close()

    return clean_input

def form_fill(input):
    for i in input:
        keyboard.type('%s\t' % (i))

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def main():
    #Read input file
    clean_input = read_file("input.txt")

    #Fill form
    time.sleep(1.5)
    form_fill(clean_input)

if __name__ == "__main__":
    main()
