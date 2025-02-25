import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Circle App")
        MainWindow.resize(400, 300)
        self.pushButton = QPushButton("Draw Circle", MainWindow)
        self.pushButton.setGeometry(150, 120, 100, 30)


class CircleApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)
            painter.drawEllipse(QPoint(x, y), diameter // 2, diameter // 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec())
