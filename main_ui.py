# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(710, 330, 101, 21))
        self.btn_update.setObjectName("btn_update")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(710, 360, 101, 21))
        self.btn_exit.setObjectName("btn_exit")
        self.grid = QtWidgets.QTableWidget(self.centralwidget)
        self.grid.setGeometry(QtCore.QRect(10, 10, 691, 371))
        self.grid.setObjectName("grid")
        self.grid.setColumnCount(0)
        self.grid.setRowCount(0)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(710, 40, 101, 21))
        self.btn_add.setObjectName("btn_add")
        self.btn_change = QtWidgets.QPushButton(self.centralwidget)
        self.btn_change.setGeometry(QtCore.QRect(710, 70, 101, 21))
        self.btn_change.setObjectName("btn_change")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(710, 100, 101, 21))
        self.btn_delete.setObjectName("btn_delete")
        self.line_id = QtWidgets.QLineEdit(self.centralwidget)
        self.line_id.setGeometry(QtCore.QRect(710, 10, 101, 20))
        self.line_id.setObjectName("line_id")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_update.setText(_translate("MainWindow", "Обновить"))
        self.btn_exit.setText(_translate("MainWindow", "Выйти"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
        self.btn_change.setText(_translate("MainWindow", "Изменить"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))
