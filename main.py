import random
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.btn.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        r = random.randint(10, 100)
        self.circles.append((x, y, r))
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, r in self.circles:
            p.setBrush(QColor(255, 255, 0))  # Желтый цвет
            p.setPen(Qt.PenStyle.NoPen)
            p.drawEllipse(x - r // 2, y - r // 2, r, r)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
