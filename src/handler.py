import sys

from pynput import mouse, keyboard

from src.gui.frame import Frame
from src.config import Keys


class _Mouse:
    def _on_move(self, x, y):
        if Handler.record:
            Handler.frame.resize(x, y)
    
    def _on_click(self, x, y, button, pressed):
        if Handler.record and pressed:
            Handler.frame.create(x, y)
        else:
            if Handler.record:
                Handler.frame.delete(x, y)
            Handler.record = False
    
    def track(self):
        listener = mouse.Listener(
            on_move=self._on_move,
            on_click=self._on_click
        )
        listener.start()

class _Keyboard:
    def _on_press(self, key: keyboard.Key):
        if key == Keys.screenshot:
            Handler.record = True
        elif key == Keys.stop:
            sys.exit()
    
    def track(self):
        listener = keyboard.Listener(on_press=self._on_press)
        listener.start()

class Handler:
    frame = Frame()
    record: bool = False

    def start():
        _Keyboard().track()
        _Mouse().track()
