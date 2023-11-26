import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from UI.CoffeeUI import CoffeeUI
from release.addEditCoffeeForm import addEditCoffeeForm


class Coffee(QMainWindow, CoffeeUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("../data/coffee.sqlite")
        self.findButton.clicked.connect(self.update_result)
        self.createButton.clicked.connect(self.add)
        self.changeButton.clicked.connect(self.edit)
        self.deleteButton.clicked.connect(self.delete)
        self.modified = {}
        self.titles = None

    def update_result(self):
        headers = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена',
                   'объем упаковки']
        cur = self.con.cursor()
        sql_result = cur.execute(f"SELECT * FROM Coffee WHERE coffee_grade LIKE "
                                 f"'{self.coffe_grade.text()}%'").fetchall()
        self.result.setRowCount(len(sql_result))
        self.result.setColumnCount(7)
        self.result.setHorizontalHeaderLabels(headers)
        if not sql_result:
            self.statusBar().showMessage('По этому запросу ничего не найдено')
            self.result.clearContents()
        else:
            self.statusBar().showMessage('')
            self.titles = [header for header in headers]
            for i, elem in enumerate(sql_result):
                for j, val in enumerate(elem):
                    self.result.setItem(i, j, QTableWidgetItem(str(val)))

    def add(self):
        ex = addEditCoffeeForm(self)
        ex.show()

    def edit(self):
        row = list(set([i.row() for i in self.result.selectedItems()]))[0]
        id = self.result.item(row, 0).text()
        ex = addEditCoffeeForm(self, id)
        ex.show()

    def delete(self):
        row = list(set([i.row() for i in self.result.selectedItems()]))[0]
        id = self.result.item(row, 0).text()
        cur = self.con.cursor()
        cur.execute(f"DELETE FROM Coffee WHERE ID = {id}").fetchall()
        self.con.commit()
        self.update_result()


def my_excepthook(type, value, tback):
    sys.__excepthook__(type, value, tback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    sys.excepthook = my_excepthook
    ex.show()
    sys.exit(app.exec_())
