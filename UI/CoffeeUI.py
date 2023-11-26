from PyQt5 import QtCore, QtGui, QtWidgets


class CoffeeUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result = QtWidgets.QTableWidget(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 40, 481, 361))
        self.result.setObjectName("result")
        self.result.setColumnCount(0)
        self.result.setRowCount(0)
        self.coffe_grade = QtWidgets.QLineEdit(self.centralwidget)
        self.coffe_grade.setGeometry(QtCore.QRect(10, 10, 181, 20))
        self.coffe_grade.setObjectName("coffe_grade")
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(200, 10, 61, 23))
        self.findButton.setObjectName("findButton")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(270, 10, 71, 23))
        self.changeButton.setObjectName("changeButton")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(350, 10, 61, 23))
        self.createButton.setObjectName("createButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(420, 10, 61, 23))
        self.deleteButton.setObjectName("deleteButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.findButton.setText(_translate("MainWindow", "Найти"))
        self.changeButton.setText(_translate("MainWindow", "Изменить"))
        self.createButton.setText(_translate("MainWindow", "Создать"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
