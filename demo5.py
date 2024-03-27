import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QScrollArea


class ScrollablePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scrollable Page")
        self.setGeometry(100, 100, 800, 600)

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a main widget for the scroll area
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        # Create a vertical layout for the main widget
        layout = QVBoxLayout(scroll_widget)
        scroll_widget.setLayout(layout)

        # Add content to the layout
        for i in range(50):
            label = QLabel(f"Label {i}")
            layout.addWidget(label)

        # Set the central widget as the scroll area
        self.setCentralWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scrollable_page = ScrollablePage()
    scrollable_page.show()
    sys.exit(app.exec_())
