import sys
import io
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint
from ui_file import Ui_MainWindow


class ShowUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialize()

    def initialize(self):  # Инициализация всех систем и подгрузка UI
        self.setFixedSize(800, 570)
        self.pushButton.clicked.connect(self.creator)
        canvas = QPixmap(800, 570)
        self.label.setPixmap(canvas)

    def creator(self):
        x, y = [randint(10, 500) for z in range(2)]
        w, h = [randint(10, 100) for z in range(2)]

        painter = QPainter(self.label.pixmap())

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(*[randint(0, 255) for z in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowUI()
    ex.show()
    sys.exit(app.exec_())
