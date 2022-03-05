#!/bin/python

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QApplication, QPushButton, QSpacerItem
import sys
import subprocess

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.init_ui()
        self.events()
        self.fill_table()
        self.show()

    def init_ui(self):
        self.layout = QGridLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Date"])
        self.table.horizontalHeader().setStretchLastSection(True)

        self.refresh_button = QPushButton(QIcon().fromTheme("gtk-refresh"), "Rafraichir")
        self.close_button = QPushButton(QIcon().fromTheme("gtk-close"), "Fermer")

        self.layout.addWidget(self.table, 0, 0)
        self.layout.addWidget(self.refresh_button, 1, 0)
        self.layout.addWidget(self.close_button, 2, 0)

        self.setLayout(self.layout)

    def events(self):
        self.refresh_button.clicked.connect(self.fill_table)
        self.close_button.clicked.connect(self.close)

    def fill_table(self):
        """

        :return: none
        """

        self.table.clearContents()

        rows = self.get_entries()[:-2]
        row_count = rows.__len__() -2 # (remove the two last rows)

        self.table.setRowCount(row_count)

        for id, row in enumerate(rows):
            row_string = row.decode()
            item = QTableWidgetItem(row_string)
            self.table.setItem(id, 0, item)

    def get_entries(self):
        """

        :return: list
        """

        out, err = subprocess.Popen(['last'], stdout=subprocess.PIPE).communicate()
        out = out.splitlines()

        return out

app = QApplication(sys.argv)
app.setApplicationName("Liste des connections")
app.setWindowIcon(QIcon().fromTheme("gtk-system"))

mainwindow = MainWindow()
app.exec()