import sys
from PySide6 import QtWidgets
from view.MainView import MainView


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainView()
    sys.exit(app.exec_())
