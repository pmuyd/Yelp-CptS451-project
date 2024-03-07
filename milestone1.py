import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon, QPixmap
import psycopg2

qtCreatorFile = "Milestone1UI.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class milestone1(QMainWindow):
    def __init__(self):
        super(milestone1, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadStateList()
        self.ui.stateList.currentTextChanged.connect(self.stateChanged)
        self.ui.cityList.itemSelectionChanged.connect(self.cityChanged)

    def executeQuery(self,sql_str):
        try:
            conn = psycopg2.connect("dbname ='milestone1db' user='postgres' host='localhost' password='tupacat11'")
        except:
            print('Unable to connect to database!')
        cur = conn.cursor()
        cur.execute(sql_str)
        conn.commit()
        result = cur.fetchall()
        conn.close()
        return result

    def loadStateList(self):
        sql_str = "SELECT distinct state FROM business ORDER BY state;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.stateList.addItem(row[0])
        except:
            print("Query to distinct state failed")
        self.ui.stateList.setCurrentIndex(-1)
        self.ui.stateList.clearEditText()

    def stateChanged(self):
        self.ui.cityList.clear()
        state = self.ui.stateList.currentText()

        if(self.ui.stateList.currentIndex()>=0):
            sql_str = "SELECT distinct city FROM business WHERE state ='" + state + "'ORDER BY city;"
            try:
                results = self.executeQuery(sql_str)
                for row in results:
                    self.ui.cityList.addItem(row[0])

            except:
                print("Query to distinct city has failed!")

            for i in reversed(range(self.ui.businesses.rowCount())):
                self.ui.businesses.removeoRow(i)

            sql_str = "SELECT name,city,state FROM business WHERE state ='" + state + "'ORDER BY name;"
            try:
                results = self.executeQuery(sql_str)
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businesses.horizontalHeader().setStyleSheet(style)
                self.ui.businesses.setColumnCount(len(results[0]))
                self.ui.businesses.setRowCount(len(results))
                self.ui.businesses.setHorizontalHeaderLabels(["Business Name", "City", "State"])
                self.ui.businesses.resizeColumnsToContents()
                self.ui.businesses.setColumnWidth(0,300)
                self.ui.businesses.setColumnWidth(1,100)
                self.ui.businesses.setColumnWidth(2,50)

                currentRowCount = 0

                for row in results:
                    for colCount in range (0, len(results[0])):
                        self.ui.businesses.setItem(currentRowCount,colCount,QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query for business has failed!")

    def cityChanged(self):
        if(self.ui.stateList.currentIndex() >= 0) and (len(self.ui.cityList.selectedItems()) > 0):
            state = self.ui.stateList.currentText()
            city = self.ui.cityList.selectedItems()[0].text()
            sql_str = "SELECT name, city, state FROM business WHERE state = '" + state + "'AND city ='" + city + "'ORDER BY name;"
            results = self.executeQuery(sql_str)
            try:
                results = self.executeQuery(sql_str)
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businesses.horizontalHeader().setStyleSheet(style)
                self.ui.businesses.setColumnCount(len(results[0]))
                self.ui.businesses.setRowCount(len(results))
                self.ui.businesses.setHorizontalHeaderLabels(["Business Name", "City", "State"])
                self.ui.businesses.resizeColumnsToContents()
                self.ui.businesses.setColumnWidth(0, 300)
                self.ui.businesses.setColumnWidth(1, 100)
                self.ui.businesses.setColumnWidth(2, 50)

                currentRowCount = 0

                for row in results:
                    for colCount in range(0, len(results[0])):
                        self.ui.businesses.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query has failed!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = milestone1()
    window.show()
    sys.exit(app.exec_())