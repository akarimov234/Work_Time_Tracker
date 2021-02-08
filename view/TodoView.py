from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class TodoView(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        root_layout = QVBoxLayout()

        dummy_label = QLabel("Dummy Todo")
        root_layout.addWidget(dummy_label)
        self.setLayout(root_layout)
