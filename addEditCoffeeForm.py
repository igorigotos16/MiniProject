# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(332, 335)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lab_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lab_name.setObjectName("lab_name")
        self.verticalLayout.addWidget(self.lab_name)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lab_sqrt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lab_sqrt.setObjectName("lab_sqrt")
        self.verticalLayout.addWidget(self.lab_sqrt)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.cb_stat = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cb_stat.setObjectName("cb_stat")
        self.cb_stat.addItem("")
        self.cb_stat.addItem("")
        self.verticalLayout.addWidget(self.cb_stat)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lab_tasty = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lab_tasty.setObjectName("lab_tasty")
        self.verticalLayout.addWidget(self.lab_tasty)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lab_cost = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lab_cost.setObjectName("lab_cost")
        self.verticalLayout.addWidget(self.lab_cost)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lab_volume = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lab_volume.setObjectName("lab_volume")
        self.verticalLayout.addWidget(self.lab_volume)
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setGeometry(QtCore.QRect(220, 240, 101, 21))
        self.btn_save.setObjectName("btn_save")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(220, 270, 101, 21))
        self.btn_exit.setObjectName("btn_exit")
        self.lab_err = QtWidgets.QLabel(Form)
        self.lab_err.setGeometry(QtCore.QRect(20, 300, 301, 16))
        self.lab_err.setStyleSheet("color: #ff0000;")
        self.lab_err.setText("")
        self.lab_err.setObjectName("lab_err")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "???????????????? ??????????"))
        self.label_2.setText(_translate("Form", "?????????????? ????????????????"))
        self.label_3.setText(_translate("Form", "??????????????/?? ????????????"))
        self.cb_stat.setItemText(0, _translate("Form", "??????????????"))
        self.cb_stat.setItemText(1, _translate("Form", "?? ????????????"))
        self.label_4.setText(_translate("Form", "???????????????? ??????????"))
        self.label_5.setText(_translate("Form", "????????"))
        self.label_6.setText(_translate("Form", "??????????"))
        self.btn_save.setText(_translate("Form", "??????????????????"))
        self.btn_exit.setText(_translate("Form", "????????????"))
