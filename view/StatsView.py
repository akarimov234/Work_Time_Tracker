from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class StatsView(QWidget):

    def __init__(self, timer_m, stats_m):
        super().__init__()
        self.timer_model = timer_m
        self.stats_model = stats_m
        self.initialize_ui()

    def initialize_ui(self):
        root_layout = QVBoxLayout()
        table = QTableWidget()
        table.setRowCount(len(self.stats_model.stats_list))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Date", "Worked"])

        for i, line in enumerate(self.stats_model.stats_list):
            date_cell = QTableWidgetItem(line[0:10])
            time_cell = QTableWidgetItem(line[11:16])
            table.setItem(i, 0, date_cell)
            table.setItem(i, 1, time_cell)

        root_layout.addWidget(table)
        self.setLayout(root_layout)
