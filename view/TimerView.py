from PySide6 import QtCore
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


class TimerView(QWidget):
    def __init__(self, model, stats):
        super().__init__()
        self.timer_is_on = False
        self.timer_model = model
        self.stats_model = stats
        self.timer_display = QLabel(self.timer_model.time_to_display)
        self.initialize_ui()

    def initialize_ui(self):
        root_layout = QVBoxLayout()

        self.timer_display.setAlignment(QtCore.Qt.AlignCenter)
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_timer)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.stop_timer)

        control_btn_layout = QHBoxLayout()
        control_btn_layout.addWidget(start_button)
        control_btn_layout.addWidget(stop_button)

        root_layout.addWidget(self.timer_display)
        root_layout.addLayout(control_btn_layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_timer)
        timer.start(1000)

        self.setLayout(root_layout)

    def update_timer(self):
        if self.timer_is_on:
            self.timer_model.update_time()
            self.timer_display.setText(self.timer_model.time_to_display)

    def start_timer(self):
        self.timer_is_on = True

    def stop_timer(self):
        self.timer_is_on = False


