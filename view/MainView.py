
from PySide6 import QtWidgets

from model.StatsModel import StatsModel
from model.TimerModel import TimerModel
from view.StatsView import StatsView
from view.TimerView import TimerView
from view.TodoView import TodoView


class MainView(QtWidgets.QWidget):
    """ MainWindow class is responsible of creating Window object and initiate all tab views"""

    def __init__(self):
        super().__init__()
        self.timer_model = TimerModel()
        self.stats_model = StatsModel(self.timer_model)
        self.tab_bar = QtWidgets.QTabWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.initialize_ui()

    def initialize_ui(self):

        self.setGeometry(300, 300, 310, 300)
        self.setWindowTitle("Work Time Tracker v2.0")
        self.main_layout.addWidget(self.setup_tabs())

        self.setLayout(self.main_layout)
        self.show()

    def setup_tabs(self):
        timer_tab = TimerView(self.timer_model, self.stats_model)
        stats_tab = StatsView(self.timer_model, self.stats_model)
        todo_tab = TodoView()
        
        self.tab_bar.addTab(timer_tab, "Timer")
        self.tab_bar.addTab(stats_tab, "Stats")
        self.tab_bar.addTab(todo_tab, "Todos")

        return self.tab_bar

    def closeEvent(self, event):
        self.stats_model.save_stats(self.timer_model.time_to_display)
        event.accept()
