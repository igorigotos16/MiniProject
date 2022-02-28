import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt5 import uic


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn_exit.clicked.connect(self.terminate)
        self.btn_update.clicked.connect(self.update)
        self.con = sqlite3.connect('coffee.sqlite')
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
        sys.exit(app.exec())




if __name__ == '__main__':  # запуск программы
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())
