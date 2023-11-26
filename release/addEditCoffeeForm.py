import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from UI.addEditCoffeeFormUI import addEditCoffeeFormUI


class addEditCoffeeForm(QMainWindow, addEditCoffeeFormUI):
    def __init__(self, parent=None, id=None):
        super().__init__(parent)
        self.setupUi(self)
        self.con = sqlite3.connect("../data/coffee.sqlite")
        if id:
            self.id = id
            self.createButton.hide()
            self.saveButton.show()
            cur = self.con.cursor()
            sql_result = cur.execute(f"SELECT * FROM Coffee WHERE ID = id").fetchall()[0]
            self.coffee_grade.setText(sql_result[1])
            self.degree_of_roasting.setCurrentText(sql_result[2])
            self.ground_or_in_grains.setCurrentText(sql_result[3])
            self.taste_description.setText(sql_result[4])
            self.price.setText(str(sql_result[5]))
            self.packing_volume.setText(str(sql_result[6]))
        self.createButton.clicked.connect(self.create_new)
        self.saveButton.clicked.connect(self.save)
        self.parent = parent
        self.set_up_combox()

    def set_up_combox(self):
        self.degree_of_roasting.addItems(['слабая', 'средняя', 'сильная'])
        self.ground_or_in_grains.addItems(["молотый", 'в зёрнах'])

    def check(self):
        if not self.price.text().isdigit():
            self.statusbar.showMessage("У вас неверно введена цена")
            return False
        elif not self.packing_volume.text().isdigit():
            self.statusbar.showMessage("У вас неверно введён объём")
            return False
        return True

    def create_new(self):
        if self.check():
            cur = self.con.cursor()
            cur.execute(f"INSERT INTO Coffee(coffee_grade, degree_of_roasting, ground_or_in_grains, taste_description, "
                        f"price, packing_volume) VALUES('{self.coffee_grade.text()}', "
                        f"'{self.degree_of_roasting.currentText()}', '{self.ground_or_in_grains.currentText()}', "
                        f"'{self.taste_description.text()}', {self.price.text()}, "
                        f"{self.packing_volume.text()})").fetchall()
            self.con.commit()
            self.parent.update_result()
            self.close()

    def save(self):
        if self.check():
            cur = self.con.cursor()
            cur.execute(f"UPDATE Coffee SET coffee_grade = '{self.coffee_grade.text()}', "
                        f"degree_of_roasting = '{self.degree_of_roasting.currentText()}', "
                        f"ground_or_in_grains = '{self.ground_or_in_grains.currentText()}', "
                        f"taste_description = '{self.taste_description.text()}', "
                        f"price = {self.price.text()}, packing_volume = {self.packing_volume.text()} "
                        f"WHERE ID = {self.id}").fetchall()
            self.con.commit()
            self.parent.update_result()
            self.close()
