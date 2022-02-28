import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from main_ui import Ui_MainWindow
from addEditCoffeeForm import Ui_Form


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_exit.clicked.connect(self.terminate)
        self.btn_update.clicked.connect(self.update)
        self.btn_add.clicked.connect(self.add_new)
        self.btn_change.clicked.connect(self.change)
        self.btn_delete.clicked.connect(self.delete)
        self.grid.itemClicked.connect(self.table_clicked)  # таблица
        self.con = sqlite3.connect('coffee.sqlite')
        self.update()
    
    def table_clicked(self, item):  # действие при нажатии на таблицу
        self.line_id.setText(self.grid.item(item.row(), 0).text())
    
    def add_new(self):  # вызов окна добавления нового заказа
        self.add_form = AddForm('0')
        self.add_form.show()
    
    def change(self):
        if self.line_id.text().isdigit() and int(self.line_id.text()) > 0:
            q = f"SELECT 1 FROM coffee WHERE ID = {self.line_id.text()}"
            res = self.con.cursor().execute(q).fetchone()
            if res:
                self.add_form = AddForm(self.line_id.text())
                self.add_form.show()
    
    def delete(self):
        if self.line_id.text().isdigit() and int(self.line_id.text()) > 0:
            q = f"SELECT 1 FROM coffee WHERE ID = {self.line_id.text()}"
            res = self.con.cursor().execute(q).fetchone()
            if res:
                q = F"DELETE FROM coffee WHERE ID = {self.line_id.text()}"
                self.con.cursor().execute(q)
        self.con.commit()
        self.update()

    
    def update(self):
        cur = self.con.cursor()
        q = f"SELECT * FROM coffee"  # условие поиска
        res = cur.execute(q).fetchall()  # получение списка деталей

        if res:  # проверка наличия результатов по критерию поиска
            self.grid.setRowCount(len(res))
            self.grid.setColumnCount(len(res[0]))
            self.grid.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 
                                                 'молотый/в зернах', 'описание вкуса', 
                                                 'цена', 'объем упаковки'])
            for i, elem in enumerate(res):
                for j, value in enumerate(elem):
                    self.grid.setItem(i, j, QTableWidgetItem(str(value)))
            self.grid.resizeColumnsToContents()
        else:
            self.grid.setRowCount(0)
    
    def terminate(self):
        self.close()


class AddForm(QWidget, Ui_Form):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id = id
        self.btn_exit.clicked.connect(self.terminate)
        self.btn_save.clicked.connect(self.save)
        self.con = sqlite3.connect('coffee.sqlite')
        if self.id != '0':
            q = f"SELECT * FROM coffee WHERE ID = {self.id}"
            res = self.con.cursor().execute(q).fetchone()
            self.lab_name.setText(str(res[1]))
            self.lab_sqrt.setText(str(res[2]))
            self.cb_stat.setCurrentText(str(res[3]))
            self.lab_cost.setText(str(res[4]))
            self.lab_tasty.setText(str(res[5]))
            self.lab_volume.setText(str(res[6]))
    
    def save(self):
        # self.id, lab_name, lab_sqrt, cb_stat, lab_tasty, lab_cost, lab_volume
        if not len(self.lab_name.text()) > 0:
            self.lab_err.setText('Не все поля заполнены!')
        elif not len(self.lab_sqrt.text()) > 0 or not self.lab_sqrt.text().isdigit():
            self.lab_err.setText('Не все поля заполнены или некорректные данные!')
        elif not len(self.lab_tasty.text()) > 0:
            self.lab_err.setText('Не все поля заполнены!')
        elif not len(self.lab_cost.text()) > 0 or not self.lab_cost.text().isdigit():
            self.lab_err.setText('Не все поля заполнены или некорректные данные!')
        elif not len(self.lab_volume.text()) > 0 or not self.lab_volume.text().isdigit():
            self.lab_err.setText('Не все поля заполнены или некорректные данные!')
        else:
            if self.id == '0':
                q = f"INSERT INTO coffee(variety_name,degree_of_roast,ground_or_in_grains,cost,taste,volume) \
                      VALUES('{self.lab_name.text()}', {self.lab_sqrt.text()}, '{self.cb_stat.currentText()}', \
                      {self.lab_cost.text()}, '{self.lab_tasty.text()}', {self.lab_volume.text()})"
            else:
                q = f"UPDATE coffee SET variety_name='{self.lab_name.text()}',degree_of_roast={self.lab_sqrt.text()},\
                      ground_or_in_grains='{self.cb_stat.currentText()}',cost={self.lab_cost.text()},\
                      taste='{self.lab_tasty.text()}',volume={self.lab_volume.text()} WHERE ID = {self.id}"
            self.con.cursor().execute(q)
            self.con.commit()
            self.close()

    def terminate(self):
        self.close()





if __name__ == '__main__':  # запуск программы
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
