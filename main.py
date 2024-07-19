import os
import threading
import time
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QComboBox
from PySide6.QtCore import Signal, Slot, Qt, QTimer, QTime, QDate
from MainWindow import Ui_MainWindow
from ConnectionWindow import Ui_ConnectionWindow
from RecipeWindow import Ui_RecipipWindow
from recipeEditWindow import RecipeSubWindow
from DataWindow import Ui_Data_Win
from popWindow import Ui_Form
from namePopup import Ui_getName
from plcMapping import Ui_PLCMapping
import yaml
import subprocess
import pymelsec as pymc
import shutil
import os
from pymelsec.constants import DT
from datetime import datetime
from threading import Thread
from Decoder import Decoder
from blabel import LabelWriter
import sqlite3
import pandas as pd
from PLC_data import PLC


class Mapping(Ui_PLCMapping, QWidget):
    def __init__(self, StName: str):
        super().__init__()
        self.StName = StName
        self.setupUi(self)
        self.setWindowTitle(f"Mapping Window : {StName}")
        self.popup = popUpWindow()
        self.fileLst = os.listdir(f"Recipes/{StName}")
        print(self.fileLst)

        # Configuring actions
        self.pushButton.clicked.connect(self.addData)
        self.pushButton_4.clicked.connect(self.deleteLast)
        self.pushButton_2.clicked.connect(self.saveMappingData)

    def addData(self):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)

        # generating number for mapping
        item = QTableWidgetItem(f"{row_count + 1}")
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setItem(row_count, 0, item)

        fileNameSelection = QComboBox()
        fileNameSelection.addItems(self.fileLst)
        self.tableWidget.setCellWidget(row_count, 1, fileNameSelection)

    def deleteLast(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)

    def saveMappingData(self):
        data = {}
        for i in range(self.tableWidget.rowCount()):
            index = self.tableWidget.item(i, 0).text()
            name = self.tableWidget.cellWidget(i, 1).currentText()
            data[index] = name

        try:
            with open(f"Config/Mapping-{self.StName}.yaml", "w+") as file:
                yaml.dump(data, file, Dumper=yaml.SafeDumper)
            self.popup.whenCall(heading="Success !!!", mesg="Data Saved Successful !!")
        except Exception as e:
            print(e)
            self.popup.whenCall(heading="Error !!!", mesg=f"Unable To Save Data \n Reason-{e}")

    def showEvent(self, event):
        try:
            with open(f"Config/Mapping-{self.StName}.yaml") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            # Settings up row count
            self.tableWidget.setRowCount(len(data.keys()))

            i = 0
            for key in data:
                item = QTableWidgetItem(f"{key}")
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tableWidget.setItem(i, 0, item)
                selectionBox = QComboBox()
                selectionBox.addItems([data[key], *self.fileLst])
                self.tableWidget.setCellWidget(i, 1, selectionBox)
                i += 1

        except Exception as e:
            print(e)

        super().showEvent(event)


class ConnWindow(Ui_ConnectionWindow, QWidget):
    monitorSignal = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.popup = popUpWindow()
        self.pushButton.clicked.connect(self.savePLCData)
        self.pushButton_7.clicked.connect(self.getPrinters)
        self.pushButton_8.clicked.connect(self.testPlcConn)
        self.pushButton_3.clicked.connect(lambda _: threading.Thread(target=self.monitorPLCData).start())
        self.pushButton_4.clicked.connect(self.saveConfig)
        self.pushButton_10.clicked.connect(self.savePrinterSetting)
        self.pushButton_12.clicked.connect(self.saveShiftSettings)
        self.monitorSignal.connect(self.runCommand)
        self.tabWidget.setCurrentIndex(0)
        self.keys = {"command_st01": self.lineEdit_3,
                     "printCount_st01": self.lineEdit_4,
                     "printRecipe_st01": self.lineEdit_26,
                     "serialNo_st01": self.lineEdit_18,
                     "barcode_st01": self.lineEdit_14,
                     "respReg_st01": self.lineEdit_23,
                     "command_st02": self.lineEdit_9,
                     "printCount_st02": self.lineEdit_11,
                     "printRecipe_st02": self.lineEdit_28,
                     "serialNo_st02": self.lineEdit_20,
                     "barcode_st02": self.lineEdit_22,
                     "respReg_st02": self.lineEdit_15,
                     "heartBeat": self.lineEdit_13,
                     "scanTime": self.lineEdit_7,
                     "plcTimeOut": self.lineEdit_8,
                     }

        # Settings up fixed size
        self.setFixedSize(551, 588)

    def savePLCData(self) -> None:
        try:
            ip = self.lineEdit.text()
            port = int(self.lineEdit_2.text())
            data = {"ip": ip, "port": port}
            with open("Config/PLC.yaml", "w+") as file:
                yaml.dump(data, file)
            self.popup.whenCall(heading="Success !!", mesg="File Save Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error", mesg=f"{e}")

    def saveConfig(self):
        # For station 1
        command_st01 = self.lineEdit_3.text()
        printCount_st01 = self.lineEdit_4.text()
        printRecipe_st01 = self.lineEdit_26.text()
        serialNo_st01 = self.lineEdit_18.text()
        barcode_st01 = self.lineEdit_14.text()
        respReg_st01 = self.lineEdit_23.text()

        # For station 2
        command_st02 = self.lineEdit_9.text()
        printCount_st02 = self.lineEdit_11.text()
        printRecipe_st02 = self.lineEdit_28.text()
        serialNo_st02 = self.lineEdit_20.text()
        barcode_st02 = self.lineEdit_22.text()
        respReg_st02 = self.lineEdit_15.text()

        # For server
        heartBeat = self.lineEdit_13.text()
        scanTime = self.lineEdit_7.text()
        plcTimeOut = self.lineEdit_8.text()
        data = {"command_st01": command_st01,
                "printCount_st01": printCount_st01,
                "printRecipe_st01": printRecipe_st01,
                "serialNo_st01": serialNo_st01,
                "barcode_st01": barcode_st01,
                "respReg_st01": respReg_st01,
                "command_st02": command_st02,
                "printCount_st02": printCount_st02,
                "printRecipe_st02": printRecipe_st02,
                "serialNo_st02": serialNo_st02,
                "barcode_st02": barcode_st02,
                "respReg_st02": respReg_st02,
                "heartBeat": heartBeat,
                "scanTime": scanTime,
                "plcTimeOut": plcTimeOut}
        try:
            with open("Config/PLCDataReg.yaml", "w+") as file:
                yaml.dump(data, file)

            self.popup.whenCall(heading="Success", mesg="File Saved Successfully")
        except Exception as e:
            print(e)
            self.popup.whenCall(heading="Error  !!", mesg=f"Unable to Save file -{e}")

    @Slot(str)
    def runCommand(self, command: str):
        command_split = command.split(":")
        match command_split[0]:
            case "command_st01":
                self.lineEdit_5.setText(command_split[1])
            case "printCount_st01":
                self.lineEdit_6.setText(command_split[1])
            case "serialNo_st01":
                self.lineEdit_19.setText(command_split[1])
            case "barcode_st01":
                self.lineEdit_16.setText(command_split[1])
            case "respReg_st01":
                self.lineEdit_25.setText(command_split[1])
            case "command_st02":
                self.lineEdit_10.setText(command_split[1])
            case "printCount_st02":
                self.lineEdit_12.setText(command_split[1])
            case "serialNo_st02":
                self.lineEdit_21.setText(command_split[1])
            case "barcode_st02":
                self.lineEdit_24.setText(command_split[1])
            case "respReg_st02":
                self.lineEdit_17.setText(command_split[1])
            case "printRecipe_st01":
                self.lineEdit_27.setText(command_split[1])
            case "printRecipe_st02":
                self.lineEdit_29.setText(command_split[1])
            case "popup":
                self.popup.whenCall("Error !!!", mesg=command_split[1])

    def getPrinters(self):
        command = 'powershell "Get-Printer | Select-Object Name"'
        process = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = process.stdout
        print(output)
        output_split = output.split("\n")
        printer_name = output_split[3:len(output_split) - 3]
        self.tableWidget.setRowCount(len(printer_name))
        self.tableWidget.setColumnCount(1)
        row = 0
        printer_name_list = []
        self.tableWidget.setColumnWidth(0, self.tabWidget.width() - 20)
        for printer in printer_name:
            printer_name_no_space = printer.rstrip(" ")
            printer_name_list.append(printer_name_no_space)
            item = QTableWidgetItem(printer_name_no_space)
            self.tableWidget.setItem(row, 0, item)
            row += 1

        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox.addItems(printer_name_list)
        self.comboBox_2.addItems(printer_name_list)

    def testPlcConn(self):
        try:
            print(self.lineEdit.text(), self.lineEdit_2.text())
            plc = pymc.Type3E(host=self.lineEdit.text(), port=int(self.lineEdit_2.text()))
            plc.connect(ip=self.lineEdit.text(), port=int(self.lineEdit_2.text()))
            plc.close()
            self.popup.whenCall(heading="Success !!!", mesg="PLC Connection Verified Successfully")
        except Exception as e:
            print(e)
            self.popup.whenCall(heading="Error !!!", mesg=f"PLC Connection Failed - {e}")

    def savePrinterSetting(self):
        st_01_printer = self.comboBox.currentText()
        st_02_printer = self.comboBox_2.currentText()
        data = {"st_01_printer": st_01_printer, "st_02_printer": st_02_printer}
        try:
            with open("Config/PrinterData.yaml", "w+") as file:
                yaml.dump(data, file, Dumper=yaml.SafeDumper)

            self.popup.whenCall(heading="Success !!", mesg=f"Data Saved Successful")

        except Exception as e:
            print(e)
            self.popup.whenCall(heading="Error !!", mesg=f"Unable to Save - {e}")

    def saveShiftSettings(self):
        shiftA = self.timeEdit.time().toPython().__str__()
        shiftB = self.timeEdit_2.time().toPython().__str__()
        shiftC = self.timeEdit_3.time().toPython().__str__()

        data = {
            "Shift_A": shiftA,
            "Shift_B": shiftB,
            "Shift_C": shiftC
        }
        with open("Config/Timer.yaml", "w+") as file:
            yaml.dump(data, file)
            self.popup.whenCall(heading="Success", mesg="Shift Timing Saved !!")

    def monitorPLCData(self):
        print("Monitor PLC Data")
        try:
            plc = pymc.Type3E(host=self.lineEdit.text(), port=int(self.lineEdit_2.text()))
            plc.connect(ip=self.lineEdit.text(), port=int(self.lineEdit_2.text()))
        except Exception as e:
            print(e)
            self.monitorSignal.emit(f"popup:Error:{e}")
            self.pushButton_3.setChecked(False)

        while self.pushButton_3.isChecked() and plc._is_connected:
            try:
                try:
                    for key in self.keys:
                        data = plc.batch_read(ref_device=self.keys[key].text(), read_size=1, data_type=DT.UWORD)[0]
                        self.monitorSignal.emit(f"{key}:{data}")
                except Exception as e:
                    print(e)

                # delay for the scan time
                time.sleep(float(self.lineEdit_8.text()))

            except Exception as e:
                print(e)
                self.monitorSignal.emit(f"popup:Error:{e}")
                break

        try:
            plc.close()
        except Exception as e:
            print(e)

    def showEvent(self, event):
        # Loading the Ip and port data
        try:
            with open("Config/PLC.yaml") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.lineEdit.setText(f"{data['ip']}")
            self.lineEdit_2.setText(f"{data['port']}")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

        try:
            # Loading the recipie data
            with open("Config/PLCDataReg.yaml", "r") as file:
                data: dict = yaml.load(file, Loader=yaml.SafeLoader)

            for key, value in data.items():
                self.keys[key].setText(value)


        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

        try:
            with open("Config/PrinterData.yaml", "r") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.comboBox.addItems([f"{data['st_01_printer']}"])
            self.comboBox_2.addItems([f"{data['st_02_printer']}"])
        except Exception as e:
            print(e)

        with open("Config/Timer.yaml", "r") as file:
            data = yaml.load(file, Loader=yaml.SafeLoader)

        self.timeEdit.setTime(QTime.fromString(data["Shift_A"]))
        self.timeEdit_2.setTime(QTime.fromString(data["Shift_B"]))
        self.timeEdit_3.setTime(QTime.fromString(data["Shift_C"]))

        return super().showEvent(event)

    def closeEvent(self, event):
        self.pushButton_3.setChecked(False)
        return super().closeEvent(event)


# Creating UI for getting name popup
class GetNamePopup(Ui_getName, QWidget):
    loadSignal = Signal(bool)

    def __init__(self, stName: str):
        super().__init__()
        self.setupUi(self)
        self.stationName.setText(stName)
        self.setFixedSize(368, 202)
        self.create.clicked.connect(self.createRecipe)
        self.popup = popUpWindow()

    def createRecipe(self):
        recipeName = self.lineEdit.text()
        if recipeName != "":
            try:
                shutil.copytree(src="Config/Sample", dst=f"Recipes/{self.stationName.text()}/{recipeName}")
                self.popup.whenCall(heading="Success", mesg="File Created Successfully")
                self.close()
            except Exception as e:
                self.popup.whenCall(heading="Error !!", mesg=f"{e}")
        else:
            self.popup.whenCall(heading="Error !!!", mesg="Please Enter a Recipe Name")

    def closeEvent(self, event):
        self.loadSignal.emit(True)
        return super().closeEvent(event)


# Class for the recipe window
class RecWindow(Ui_RecipipWindow, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openCreateRecipeST01)
        self.pushButton_4.clicked.connect(self.openCreateRecipeSt02)
        self.pushButton_2.clicked.connect(self.loadRecipeSt01)
        self.pushButton_10.clicked.connect(self.deleteRecipe)
        self.pushButton_5.clicked.connect(self.loadRecipeSt02)
        self.pushButton_9.clicked.connect(self.deleteRecipe2)
        self.pushButton_7.clicked.connect(self.loadMappingTable1)
        self.pushButton_8.clicked.connect(self.loadMappingTable2)

        self.loadTable()
        self.loadTable2()
        self.popup = popUpWindow()
        self.getName = GetNamePopup("Station_01")
        self.getName2 = GetNamePopup("Station_02")
        self.getName.loadSignal.connect(self.loadTable)
        self.getName2.loadSignal.connect(self.loadTable2)

    def loadMappingTable1(self):
        self.mappingTable = Mapping("Station_01")
        self.mappingTable.show()

    def loadMappingTable2(self):
        self.mappingTable2 = Mapping("Station_02")
        self.mappingTable2.show()

    def openCreateRecipeST01(self):
        self.getName.show()

    def openCreateRecipeSt02(self):
        self.getName2.show()

    def deleteRecipe(self):
        nameLis = self.tableWidget.selectedItems()
        if len(nameLis) != 1:
            self.popup.whenCall(heading="Error !!", mesg="Please Select one")
        else:
            name = nameLis[0].text()
            shutil.rmtree(f"Recipes/Station_01/{name}")
            self.loadTable()

    def deleteRecipe2(self):
        nameLis = self.tableWidget_2.selectedItems()
        if len(nameLis) != 1:
            self.popup.whenCall(heading="Error !!", mesg="Please Select one")
        else:
            name = nameLis[0].text()
            shutil.rmtree(f"Recipes/Station_02/{name}")
            self.loadTable2()

    def loadRecipeSt01(self):
        selected = self.tableWidget.selectedItems()
        if len(selected) != 1:
            self.popup.whenCall(heading="Error !!", mesg="Please Select One Option")
        else:
            item = selected[0].text()
            self.subRecipeWindow = RecipeSubWindow(f"Station_01-{item}")
            self.subRecipeWindow.show()

    def loadRecipeSt02(self):
        selected = self.tableWidget_2.selectedItems()
        if len(selected) != 1:
            self.popup.whenCall(heading="Error !!", mesg="Please Select One Option")
        else:
            item = selected[0].text()
            self.subRecipeWindow2 = RecipeSubWindow(f"Station_02-{item}")
            self.subRecipeWindow2.show()

    def loadTable(self):
        recipeList = os.listdir("Recipes/Station_01")
        row = 0
        self.tableWidget.setColumnWidth(0, 600)
        self.tableWidget.setRowCount(len(recipeList))
        for recipe in recipeList:
            # print(recipe)
            item = QTableWidgetItem(f"{recipe}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(row, 0, item)
            row += 1

    def loadTable2(self):
        recipeList = os.listdir("Recipes/Station_02")
        row = 0
        self.tableWidget_2.setColumnWidth(0, 600)
        self.tableWidget_2.setRowCount(len(recipeList))
        for recipe in recipeList:
            # print(recipe)
            item = QTableWidgetItem(f"{recipe}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget_2.setItem(row, 0, item)
            row += 1

    def closeEvent(self, event):
        try:
            self.subRecipeWindow.close()
        except Exception as e:
            print(e)

        return super().closeEvent(event)


# Class For making Popups
class popUpWindow(Ui_Form, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.conform.clicked.connect(self.close)

    def whenCall(self, heading: str, mesg: str) -> None:
        self.label.setText(heading)
        self.label_2.setText(mesg)
        self.show()


class ShowDataWindow(Ui_Data_Win, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.popup = popUpWindow()
        self.pushButton_4.clicked.connect(self.SearchByDate)
        self.pushButton_5.clicked.connect(self.createExcel)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit_2.setDate(QDate.currentDate())

        # Setting Up database Connection 
        try:
            self.db = sqlite3.connect("Database\database.db")
            self.cur = self.db.cursor()
        except Exception as e:
            print(e)

    def SearchByDate(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(0)
        startDate = self.dateEdit.date().toPython().__str__()
        endDate = self.dateEdit_2.date().toPython().__str__()
        print(startDate, endDate)
        df = pd.read_sql_query(f"SELECT * FROM data WHERE DATE BETWEEN '{startDate}' and '{endDate};'", self.db)
        # print(df)
        self.tableWidget_2.makeTable(df)

    def createExcel(self):
        startDate = self.dateEdit.date().toPython().__str__()
        endDate = self.dateEdit_2.date().toPython().__str__()
        df = pd.read_sql_query(f"SELECT * FROM data WHERE DATE BETWEEN '{startDate}' and '{endDate};'", self.db)
        df.to_excel(f"Excel/{startDate} to {endDate}.xlsx")
        self.popup.whenCall(heading="Sucess !!!", mesg=f"Excel Created at Excel/{startDate} to {endDate}.xlsx")


class MyApp(QMainWindow, Ui_MainWindow):
    FendSingal = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.actionOpen_Recipie_Editor.triggered.connect(self.openRecipie)
        self.actionConnection_Settings.triggered.connect(self.openConnWindow)
        self.actionData.triggered.connect(self.showdata)
        self.pushButton_2.clicked.connect(self.runPLC)

        self.recWindow = RecWindow()
        self.connectionWindow = ConnWindow()
        self.datawindow = ShowDataWindow()
        
        self.plc = PLC()
        self.plc.start()
        self.plc.logSignal.connect(self.commandHandler)

        # Creating popup window
        self.popup = popUpWindow()
        self.textEdit.log("Logs will show here...")

        self.fileList = ["barcode.yaml", "label1.yaml", "label2.yaml", "label3.yaml", "label4.yaml", "template.html",
                         "style.css", "label_spec.yaml"]
        self.name = None

        # Setting Up database Connection 
        try:
            self.db = sqlite3.connect("Database\database.db")
            self.cur = self.db.cursor()
        except Exception as e:
            print(e)

    def openRecipie(self) -> None:
        self.recWindow.show()
        self.plc.terminate()

    def openConnWindow(self) -> None:
        self.connectionWindow.show()
        self.plc.terminate()

    def showdata(self):
        self.datawindow.show()
    
    def runPLC(self):
        self.plc.start()
    
    @Slot(str)
    def commandHandler(self, command:str):
        self.textEdit.log(command)


    def closeEvent(self, event: QCloseEvent) -> None:
        self.plc.terminate()
        self.destroy()
        return super().closeEvent(event)


if __name__ == "__main__":
    App = QApplication()
    window = MyApp()
    window.show()
    App.exec()
