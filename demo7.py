import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QRegion
from PyQt5.QtCore import Qt, QRect


class CircularWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Circular Window')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout(self)
        label = QLabel('Circular Window Content', alignment=Qt.AlignCenter)
        layout.addWidget(label)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Create a circular region for the central content area
        content_rect = QRect(50, 50, self.width() - 100, self.height() - 100)
        content_region = QRegion(content_rect, QRegion.Ellipse)
        painter.setClipRegion(content_region)

        # Fill the central content area with a semi-transparent color
        painter.fillRect(self.rect(), QColor(255, 255, 255, 200))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircularWindow()
    window.show()
    sys.exit(app.exec_())
