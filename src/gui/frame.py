from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath
from PyQt5.QtWidgets import QFrame

from src.config import Color, Fade


class Frame(QFrame):
    def __init__(self):
        types = Qt.WindowType
        super().__init__(parent=None, flags=(
                types.FramelessWindowHint 
                | Qt.MSWindowsFixedSizeDialogHint 
                | Qt.WindowStaysOnTopHint
            )
        )

        self.path = QPainterPath()
        self.screen = list()

    def _change_transparency(self, fade: bool = False):
        if fade:
            values = Fade.range_[:Fade.slice]
        else:
            values = Fade.range_[Fade.slice:]
        
        for value in values:
            self.setWindowOpacity(value / Fade.divisor)
    
    def create(self, x, y):
        self.screen = self.screen + [x, y]

        self._change_transparency()

        self.setStyleSheet("background-color: " + Color.background)
        self.path.addRoundedRect(0, 0, x, y, 0, 0)

        self.show()

    def delete(self, x, y):
        self.screen = self.screen + [x, y]
        self._change_transparency(fade=True)

        ... #TODO pillow and delete

        self.screen = []
