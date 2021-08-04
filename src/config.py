class Color:
    background = ""
    vector = ""

class Fade:
    range_ = range(0, 11)
    divisor = 10
    slice = 4

from pynput.keyboard import Key
class Keys:
    screenshot = Key.print_screen
    stop = Key.space
