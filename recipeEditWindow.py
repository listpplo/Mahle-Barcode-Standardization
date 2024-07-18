import yaml
from subRecipe import Ui_SubWindow
from PySide6.QtWidgets import QWidget
from popWindow import Ui_Form
from Decoder import Decoder
from blabel import LabelWriter
import os


class popUpWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def whenCall(self, heading: str, mesg: str) -> None:
        self.label.setText(heading)
        self.label_2.setText(mesg)
        self.show()


class RecipeSubWindow(Ui_SubWindow, QWidget):
    def __init__(self, windowName: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(windowName)
        self.fileList = ["barcode.yaml", "label1.yaml", "label2.yaml", "label3.yaml", "label4.yaml", "template.html",
                         "style.css", "label_spec.yaml"]
        self.pushButton_2.clicked.connect(self.reloadDataBarcode)
        self.pushButton_17.clicked.connect(self.reloadDataLabel1)
        self.pushButton_20.clicked.connect(self.reloadDataLabel2)
        self.pushButton_24.clicked.connect(self.reloadDataLabel3)
        self.pushButton_26.clicked.connect(self.reloadDataLabel4)
        self.pushButton.clicked.connect(self.saveBarcodeData)
        self.pushButton_16.clicked.connect(self.saveLabel1Data)
        self.pushButton_19.clicked.connect(self.saveLabel2Data)
        self.pushButton_22.clicked.connect(self.saveLabel3Data)
        self.pushButton_25.clicked.connect(self.saveLabel4Data)
        self.pushButton_3.clicked.connect(self.generateBarcodeData)
        self.pushButton_18.clicked.connect(self.generateLabel1Data)
        self.pushButton_21.clicked.connect(self.generateLabel2Data)
        self.pushButton_23.clicked.connect(self.generateLabel3Data)
        self.pushButton_27.clicked.connect(self.generateLabel4Data)
        self.pushButton_30.clicked.connect(self.generateLabelPrint)
        self.pushButton_28.clicked.connect(self.saveGenCode)
        self.setFixedSize(610, 502)
        self.popup = popUpWindow()
        self.name = None

    def showEvent(self, event):
        self.name = name = self.windowTitle().split("-")
        try:
            # Loading the barcode page
            with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[0]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadBarcodePage(data)

            # Loading the label1 page
            with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[1]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel1Page(data)

            # Loading Label2 page
            with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[2]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel2Data(data)

            #  Loading label 3 page
            with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[3]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel3Data(data)

            with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[4]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel4Data(data)

            with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[7]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)
            
            self.loadLabelSpec(data)

            # with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[5]}") as file:
            #     self.textEdit.setPlainText(file.read())
            #
            # with open(f"Recipes/{name[0]}/{name[1]}/{self.fileList[6]}") as file:
            #     self.textEdit_2.setPlainText(file.read())

        except Exception as e:
            print("Error at loading ", e)

        return super().showEvent(event)

    def reloadDataBarcode(self):
        # print("Reloading Barcode Data")
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[0]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadBarcodePage(data)
            self.popup.whenCall(heading="Success", mesg="Data Loading Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def reloadDataLabel1(self):
        # print("reloading Data Label 1")
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[1]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel1Page(data)
            self.popup.whenCall(heading="Success", mesg="Data Loading Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def reloadDataLabel2(self):
        # print("reload data Label 2")
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[2]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel2Data(data)
            self.popup.whenCall(heading="Success", mesg="Data Loading Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def reloadDataLabel3(self):
        # print("Reloading Data Label 3")
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[3]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel3Data(data)
            self.popup.whenCall(heading="Success", mesg="Data Loading Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def reloadDataLabel4(self):
        # print("Reloading Data Label 4")
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[4]}") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            self.loadLabel4Data(data)
            self.popup.whenCall(heading="Success", mesg="Data Loading Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def loadBarcodePage(self, data: dict):
        self.checkBox.setChecked(data["enable"])

        typ, value = data["arg1"].split("~")
        self.QR_arg1_value.setText(value)
        self.QR_arg1.setCurrentIndex(int(typ))

        typ, value = data["arg2"].split("~")
        self.QR_arg2_value.setText(value)
        self.QR_arg2.setCurrentIndex(int(typ))

        typ, value = data["arg3"].split("~")
        self.QR_arg3_value.setText(value)
        self.QR_arg3.setCurrentIndex(int(typ))

        typ, value = data["arg4"].split("~")
        self.QR_arg4_value.setText(value)
        self.QR_arg4.setCurrentIndex(int(typ))

        typ, value = data["arg5"].split("~")
        self.QR_arg5_value.setText(value)
        self.QR_arg5.setCurrentIndex(int(typ))

        typ, value = data["arg6"].split("~")
        self.QR_arg6_value.setText(value)
        self.QR_arg6.setCurrentIndex(int(typ))

        typ, value = data["arg7"].split("~")
        self.QR_arg7_value.setText(value)
        self.QR_arg7.setCurrentIndex(int(typ))

        typ, value = data["arg8"].split("~")
        self.QR_arg8_value.setText(value)
        self.QR_arg8.setCurrentIndex(int(typ))

        typ, value = data["arg9"].split("~")
        self.QR_arg9_value.setText(value)
        self.QR_arg9.setCurrentIndex(int(typ))

        typ, value = data["arg10"].split("~")
        self.QR_arg10_value.setText(value)
        self.QR_arg10.setCurrentIndex(int(typ))

        typ, value = data["arg11"].split("~")
        self.QR_arg11_value.setText(value)
        self.QR_arg11.setCurrentIndex(int(typ))

        typ, value = data["arg12"].split("~")
        self.QR_arg12_value.setText(value)
        self.QR_arg12.setCurrentIndex(int(typ))

        typ, value = data["arg13"].split("~")
        self.QR_arg13_value.setText(value)
        self.QR_arg13.setCurrentIndex(int(typ))

        typ, value = data["arg14"].split("~")
        self.QR_arg14_value.setText(value)
        self.QR_arg14.setCurrentIndex(int(typ))

        typ, value = data["arg15"].split("~")
        self.QR_arg15_value.setText(value)
        self.QR_arg15.setCurrentIndex(int(typ))

        typ, value = data["arg16"].split("~")
        self.QR_arg16_value.setText(value)
        self.QR_arg16.setCurrentIndex(int(typ))

    def loadLabel1Page(self, data: dict):
        self.checkBox_2.setChecked(data["enable"])

        print("Load data label 2 start")

        typ, value = data["arg1"].split("~")
        self.Label1_arg1.setCurrentIndex(int(typ))
        self.Label1_arg1_value.setText(value)

        typ, value = data["arg2"].split("~")
        self.Label1_arg2.setCurrentIndex(int(typ))
        self.Label1_arg2_value.setText(value)

        typ, value = data["arg3"].split("~")
        self.Label1_arg3.setCurrentIndex(int(typ))
        self.Label1_arg3_value.setText(value)

        typ, value = data["arg4"].split("~")
        self.Label1_arg4.setCurrentIndex(int(typ))
        self.Label1_arg4_value.setText(value)

        typ, value = data["arg5"].split("~")
        self.Label1_arg5.setCurrentIndex(int(typ))
        self.Label1_arg5_value.setText(value)

        typ, value = data["arg6"].split("~")
        self.Label1_arg6.setCurrentIndex(int(typ))
        self.Label1_arg6_value.setText(value)

        typ, value = data["arg7"].split("~")
        self.Label1_arg7.setCurrentIndex(int(typ))
        self.Label1_arg7_value.setText(value)

        typ, value = data["arg8"].split("~")
        self.Label1_arg8.setCurrentIndex(int(typ))
        self.Label1_arg8_value.setText(value)

        typ, value = data["arg9"].split("~")
        self.Label1_arg9.setCurrentIndex(int(typ))
        self.Label1_arg9_value.setText(value)

        typ, value = data["arg10"].split("~")
        self.Label1_arg10.setCurrentIndex(int(typ))
        self.Label1_arg10_value.setText(value)

        typ, value = data["arg11"].split("~")
        self.Label1_arg11.setCurrentIndex(int(typ))
        self.Label1_arg11_value.setText(value)

        typ, value = data["arg12"].split("~")
        self.Label1_arg12.setCurrentIndex(int(typ))
        self.Label1_arg12_value.setText(value)

        typ, value = data["arg13"].split("~")
        self.Label1_arg13.setCurrentIndex(int(typ))
        self.Label1_arg13_value.setText(value)

        typ, value = data["arg14"].split("~")
        self.Label1_arg14.setCurrentIndex(int(typ))
        self.Label1_arg14_value.setText(value)

        typ, value = data["arg15"].split("~")
        self.Label1_arg15.setCurrentIndex(int(typ))
        self.Label1_arg15_value.setText(value)

        typ, value = data["arg16"].split("~")
        self.Label1_arg16.setCurrentIndex(int(typ))
        self.Label1_arg16_value.setText(value)

    def loadLabel2Data(self, data: dict):
        self.checkBox_3.setChecked(data['enable'])

        print("Load data label 2 start")

        typ, value = data["arg1"].split("~")
        self.Label2_arg1.setCurrentIndex(int(typ))
        self.Label2_arg1_value.setText(value)

        typ, value = data["arg2"].split("~")
        self.Label2_arg2.setCurrentIndex(int(typ))
        self.Label2_arg2_value.setText(value)

        typ, value = data["arg3"].split("~")
        self.Label2_arg3.setCurrentIndex(int(typ))
        self.Label2_arg3_value.setText(value)

        typ, value = data["arg4"].split("~")
        self.Label2_arg4.setCurrentIndex(int(typ))
        self.Label2_arg4_value.setText(value)

        typ, value = data["arg5"].split("~")
        self.Label2_arg5.setCurrentIndex(int(typ))
        self.Label2_arg5_value.setText(value)

        typ, value = data["arg6"].split("~")
        self.Label2_arg6.setCurrentIndex(int(typ))
        self.Label2_arg6_value.setText(value)

        typ, value = data["arg7"].split("~")
        self.Label2_arg7.setCurrentIndex(int(typ))
        self.Label2_arg7_value.setText(value)

        typ, value = data["arg8"].split("~")
        self.Label2_arg8.setCurrentIndex(int(typ))
        self.Label2_arg8_value.setText(value)

        typ, value = data["arg9"].split("~")
        self.Label2_arg9.setCurrentIndex(int(typ))
        self.Label2_arg9_value.setText(value)

        typ, value = data["arg10"].split("~")
        self.Label2_arg10.setCurrentIndex(int(typ))
        self.Label2_arg10_value.setText(value)

        typ, value = data["arg11"].split("~")
        self.Label2_arg11.setCurrentIndex(int(typ))
        self.Label2_arg11_value.setText(value)

        typ, value = data["arg12"].split("~")
        self.Label2_arg12.setCurrentIndex(int(typ))
        self.Label2_arg12_value.setText(value)

        typ, value = data["arg13"].split("~")
        self.Label2_arg13.setCurrentIndex(int(typ))
        self.Label2_arg13_value.setText(value)

        typ, value = data["arg14"].split("~")
        self.Label2_arg14.setCurrentIndex(int(typ))
        self.Label2_arg14_value.setText(value)

        typ, value = data["arg15"].split("~")
        self.Label2_arg15.setCurrentIndex(int(typ))
        self.Label2_arg15_value.setText(value)

        typ, value = data["arg16"].split("~")
        self.Label2_arg16.setCurrentIndex(int(typ))
        self.Label2_arg16_value.setText(value)

    def loadLabel3Data(self, data: dict):
        self.checkBox_4.setChecked(data["enable"])

        print("Load data label 3 start")

        typ, value = data["arg1"].split("~")
        self.Label3_arg1.setCurrentIndex(int(typ))
        self.Label3_arg1_value.setText(value)

        typ, value = data["arg2"].split("~")
        self.Label3_arg2.setCurrentIndex(int(typ))
        self.Label3_arg2_value.setText(value)

        typ, value = data["arg3"].split("~")
        self.Label3_arg3.setCurrentIndex(int(typ))
        self.Label3_arg3_value.setText(value)

        typ, value = data["arg4"].split("~")
        self.Label3_arg4.setCurrentIndex(int(typ))
        self.Label3_arg4_value.setText(value)

        typ, value = data["arg5"].split("~")
        self.Label3_arg5.setCurrentIndex(int(typ))
        self.Label3_arg5_value.setText(value)

        typ, value = data["arg6"].split("~")
        self.Label3_arg6.setCurrentIndex(int(typ))
        self.Label3_arg6_value.setText(value)

        typ, value = data["arg7"].split("~")
        self.Label3_arg7.setCurrentIndex(int(typ))
        self.Label3_arg7_value.setText(value)

        typ, value = data["arg8"].split("~")
        self.Label3_arg8.setCurrentIndex(int(typ))
        self.Label3_arg8_value.setText(value)

        typ, value = data["arg9"].split("~")
        self.Label3_arg9.setCurrentIndex(int(typ))
        self.Label3_arg9_value.setText(value)

        typ, value = data["arg10"].split("~")
        self.Label3_arg10.setCurrentIndex(int(typ))
        self.Label3_arg10_value.setText(value)

        typ, value = data["arg11"].split("~")
        self.Label3_arg11.setCurrentIndex(int(typ))
        self.Label3_arg11_value.setText(value)

        typ, value = data["arg12"].split("~")
        self.Label3_arg12.setCurrentIndex(int(typ))
        self.Label3_arg12_value.setText(value)

        typ, value = data["arg13"].split("~")
        self.Label3_arg13.setCurrentIndex(int(typ))
        self.Label3_arg13_value.setText(value)

        typ, value = data["arg14"].split("~")
        self.Label3_arg14.setCurrentIndex(int(typ))
        self.Label3_arg14_value.setText(value)

        typ, value = data["arg15"].split("~")
        self.Label3_arg15.setCurrentIndex(int(typ))
        self.Label3_arg15_value.setText(value)

        typ, value = data["arg16"].split("~")
        self.Label3_arg16.setCurrentIndex(int(typ))
        self.Label3_arg16_value.setText(value)

    def loadLabel4Data(self, data: dict):
        self.checkBox_5.setChecked(data["enable"])
        print("Load data label 2 start")

        typ, value = data["arg1"].split("~")
        self.Label4_arg1.setCurrentIndex(int(typ))
        self.Label4_arg1_value.setText(value)

        typ, value = data["arg2"].split("~")
        self.Label4_arg2.setCurrentIndex(int(typ))
        self.Label4_arg2_value.setText(value)

        typ, value = data["arg3"].split("~")
        self.Label4_arg3.setCurrentIndex(int(typ))
        self.Label4_arg3_value.setText(value)

        typ, value = data["arg4"].split("~")
        self.Label4_arg4.setCurrentIndex(int(typ))
        self.Label4_arg4_value.setText(value)

        typ, value = data["arg5"].split("~")
        self.Label4_arg5.setCurrentIndex(int(typ))
        self.Label4_arg5_value.setText(value)

        typ, value = data["arg6"].split("~")
        self.Label4_arg6.setCurrentIndex(int(typ))
        self.Label4_arg6_value.setText(value)

        typ, value = data["arg7"].split("~")
        self.Label4_arg7.setCurrentIndex(int(typ))
        self.Label4_arg7_value.setText(value)

        typ, value = data["arg8"].split("~")
        self.Label4_arg8.setCurrentIndex(int(typ))
        self.Label4_arg8_value.setText(value)

        typ, value = data["arg9"].split("~")
        self.Label4_arg9.setCurrentIndex(int(typ))
        self.Label4_arg9_value.setText(value)

        typ, value = data["arg10"].split("~")
        self.Label4_arg10.setCurrentIndex(int(typ))
        self.Label4_arg10_value.setText(value)

        typ, value = data["arg11"].split("~")
        self.Label4_arg11.setCurrentIndex(int(typ))
        self.Label4_arg11_value.setText(value)

        typ, value = data["arg12"].split("~")
        self.Label4_arg12.setCurrentIndex(int(typ))
        self.Label4_arg12_value.setText(value)

        typ, value = data["arg13"].split("~")
        self.Label4_arg13.setCurrentIndex(int(typ))
        self.Label4_arg13_value.setText(value)

        typ, value = data["arg14"].split("~")
        self.Label4_arg14.setCurrentIndex(int(typ))
        self.Label4_arg14_value.setText(value)

        typ, value = data["arg15"].split("~")
        self.Label4_arg15.setCurrentIndex(int(typ))
        self.Label4_arg15_value.setText(value)

        typ, value = data["arg16"].split("~")
        self.Label4_arg16.setCurrentIndex(int(typ))
        self.Label4_arg16_value.setText(value)

    def loadLabelSpec(self, data: dict):
        # Page
        self.doubleSpinBox_6.setValue(data["page"]["height"])
        self.doubleSpinBox_7.setValue(data["page"]["width"])
        self.doubleSpinBox_9.setValue(data["page"]["p_left"])
        self.doubleSpinBox_8.setValue(data["page"]["p_top"])
        # Qr Code
        self.doubleSpinBox_10.setValue(data["img"]["height"])
        self.doubleSpinBox_11.setValue(data["img"]["width"])
        self.doubleSpinBox_13.setValue(data["img"]["p_left"])
        self.doubleSpinBox_12.setValue(data["img"]["p_top"])
        # Label 1
        self.doubleSpinBox_2.setValue(data["label_1"]["font-size"])
        self.comboBox.setCurrentText(data["label_1"]["font-weight"])
        self.doubleSpinBox_14.setValue(data["label_1"]["p_top"])
        self.doubleSpinBox_15.setValue(data["label_1"]["p_left"])
        # Label 2
        self.doubleSpinBox_3.setValue(data["label_2"]["font-size"])
        self.comboBox_2.setCurrentText(data["label_2"]["font-weight"])
        self.doubleSpinBox_16.setValue(data["label_2"]["p_top"])
        self.doubleSpinBox_17.setValue(data["label_2"]["p_left"])
        # Label 3
        self.doubleSpinBox_4.setValue(data["label_3"]["font-size"])
        self.comboBox_3.setCurrentText(data["label_3"]["font-weight"])
        self.doubleSpinBox_19.setValue(data["label_3"]["p_top"])
        self.doubleSpinBox_18.setValue(data["label_3"]["p_left"])
        # Label 4
        self.doubleSpinBox_5.setValue(data["label_4"]["font-size"])
        self.comboBox_4.setCurrentText(data["label_4"]["font-weight"])
        self.doubleSpinBox_20.setValue(data["label_4"]["p_top"])
        self.doubleSpinBox_21.setValue(data["label_4"]["p_left"])
        # SerialNo
        # self.spinBox.setValue(data["serialNo"])

    def saveBarcodeData(self):
        enable = self.checkBox.isChecked()
        arg1 = f"{self.QR_arg1.currentIndex()}~{self.QR_arg1_value.text()}"
        arg2 = f"{self.QR_arg2.currentIndex()}~{self.QR_arg2_value.text()}"
        arg3 = f"{self.QR_arg3.currentIndex()}~{self.QR_arg3_value.text()}"
        arg4 = f"{self.QR_arg4.currentIndex()}~{self.QR_arg4_value.text()}"
        arg5 = f"{self.QR_arg5.currentIndex()}~{self.QR_arg5_value.text()}"
        arg6 = f"{self.QR_arg6.currentIndex()}~{self.QR_arg6_value.text()}"
        arg7 = f"{self.QR_arg7.currentIndex()}~{self.QR_arg7_value.text()}"
        arg8 = f"{self.QR_arg8.currentIndex()}~{self.QR_arg8_value.text()}"
        arg9 = f"{self.QR_arg9.currentIndex()}~{self.QR_arg9_value.text()}"
        arg10 = f"{self.QR_arg10.currentIndex()}~{self.QR_arg10_value.text()}"
        arg11 = f"{self.QR_arg11.currentIndex()}~{self.QR_arg11_value.text()}"
        arg12 = f"{self.QR_arg12.currentIndex()}~{self.QR_arg12_value.text()}"
        arg13 = f"{self.QR_arg13.currentIndex()}~{self.QR_arg13_value.text()}"
        arg14 = f"{self.QR_arg14.currentIndex()}~{self.QR_arg14_value.text()}"
        arg15 = f"{self.QR_arg15.currentIndex()}~{self.QR_arg15_value.text()}"
        arg16 = f"{self.QR_arg16.currentIndex()}~{self.QR_arg16_value.text()}"

        data = {
            "enable": enable,
            "arg1": arg1,
            "arg2": arg2,
            "arg3": arg3,
            "arg4": arg4,
            "arg5": arg5,
            "arg6": arg6,
            "arg7": arg7,
            "arg8": arg8,
            "arg9": arg9,
            "arg10": arg10,
            "arg11": arg11,
            "arg12": arg12,
            "arg13": arg13,
            "arg14": arg14,
            "arg15": arg15,
            "arg16": arg16,
        }
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[0]}", "w+") as file:
                yaml.dump(data, file)
            self.popup.whenCall(heading="Success", mesg="Data Save Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def saveLabel1Data(self):
        enable = self.checkBox_2.isChecked()
        arg1 = f"{self.Label1_arg1.currentIndex()}~{self.Label1_arg1_value.text()}"
        arg2 = f"{self.Label1_arg2.currentIndex()}~{self.Label1_arg2_value.text()}"
        arg3 = f"{self.Label1_arg3.currentIndex()}~{self.Label1_arg3_value.text()}"
        arg4 = f"{self.Label1_arg4.currentIndex()}~{self.Label1_arg4_value.text()}"
        arg5 = f"{self.Label1_arg5.currentIndex()}~{self.Label1_arg5_value.text()}"
        arg6 = f"{self.Label1_arg6.currentIndex()}~{self.Label1_arg6_value.text()}"
        arg7 = f"{self.Label1_arg7.currentIndex()}~{self.Label1_arg7_value.text()}"
        arg8 = f"{self.Label1_arg8.currentIndex()}~{self.Label1_arg8_value.text()}"
        arg9 = f"{self.Label1_arg9.currentIndex()}~{self.Label1_arg9_value.text()}"
        arg10 = f"{self.Label1_arg10.currentIndex()}~{self.Label1_arg10_value.text()}"
        arg11 = f"{self.Label1_arg11.currentIndex()}~{self.Label1_arg11_value.text()}"
        arg12 = f"{self.Label1_arg12.currentIndex()}~{self.Label1_arg12_value.text()}"
        arg13 = f"{self.Label1_arg13.currentIndex()}~{self.Label1_arg13_value.text()}"
        arg14 = f"{self.Label1_arg14.currentIndex()}~{self.Label1_arg14_value.text()}"
        arg15 = f"{self.Label1_arg15.currentIndex()}~{self.Label1_arg15_value.text()}"
        arg16 = f"{self.Label1_arg16.currentIndex()}~{self.Label1_arg16_value.text()}"

        data = {
            "enable": enable,
            "arg1": arg1,
            "arg2": arg2,
            "arg3": arg3,
            "arg4": arg4,
            "arg5": arg5,
            "arg6": arg6,
            "arg7": arg7,
            "arg8": arg8,
            "arg9": arg9,
            "arg10": arg10,
            "arg11": arg11,
            "arg12": arg12,
            "arg13": arg13,
            "arg14": arg14,
            "arg15": arg15,
            "arg16": arg16,
        }
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[1]}", "w+") as file:
                yaml.dump(data, file)
            self.popup.whenCall(heading="Success", mesg="Data Save Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def saveLabel2Data(self):
        enable = self.checkBox_3.isChecked()
        arg1 = f"{self.Label2_arg1.currentIndex()}~{self.Label2_arg1_value.text()}"
        arg2 = f"{self.Label2_arg2.currentIndex()}~{self.Label2_arg2_value.text()}"
        arg3 = f"{self.Label2_arg3.currentIndex()}~{self.Label2_arg3_value.text()}"
        arg4 = f"{self.Label2_arg4.currentIndex()}~{self.Label2_arg4_value.text()}"
        arg5 = f"{self.Label2_arg5.currentIndex()}~{self.Label2_arg5_value.text()}"
        arg6 = f"{self.Label2_arg6.currentIndex()}~{self.Label2_arg6_value.text()}"
        arg7 = f"{self.Label2_arg7.currentIndex()}~{self.Label2_arg7_value.text()}"
        arg8 = f"{self.Label2_arg8.currentIndex()}~{self.Label2_arg8_value.text()}"
        arg9 = f"{self.Label2_arg9.currentIndex()}~{self.Label2_arg9_value.text()}"
        arg10 = f"{self.Label2_arg10.currentIndex()}~{self.Label2_arg10_value.text()}"
        arg11 = f"{self.Label2_arg11.currentIndex()}~{self.Label2_arg11_value.text()}"
        arg12 = f"{self.Label2_arg12.currentIndex()}~{self.Label2_arg12_value.text()}"
        arg13 = f"{self.Label2_arg13.currentIndex()}~{self.Label2_arg13_value.text()}"
        arg14 = f"{self.Label2_arg14.currentIndex()}~{self.Label2_arg14_value.text()}"
        arg15 = f"{self.Label2_arg15.currentIndex()}~{self.Label2_arg15_value.text()}"
        arg16 = f"{self.Label2_arg16.currentIndex()}~{self.Label2_arg16_value.text()}"

        data = {
            "enable": enable,
            "arg1": arg1,
            "arg2": arg2,
            "arg3": arg3,
            "arg4": arg4,
            "arg5": arg5,
            "arg6": arg6,
            "arg7": arg7,
            "arg8": arg8,
            "arg9": arg9,
            "arg10": arg10,
            "arg11": arg11,
            "arg12": arg12,
            "arg13": arg13,
            "arg14": arg14,
            "arg15": arg15,
            "arg16": arg16,
        }
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[2]}", "w+") as file:
                yaml.dump(data, file)
            self.popup.whenCall(heading="Success", mesg="Data Save Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def saveLabel3Data(self):
        enable = self.checkBox_4.isChecked()
        arg1 = f"{self.Label3_arg1.currentIndex()}~{self.Label3_arg1_value.text()}"
        arg2 = f"{self.Label3_arg2.currentIndex()}~{self.Label3_arg2_value.text()}"
        arg3 = f"{self.Label3_arg3.currentIndex()}~{self.Label3_arg3_value.text()}"
        arg4 = f"{self.Label3_arg4.currentIndex()}~{self.Label3_arg4_value.text()}"
        arg5 = f"{self.Label3_arg5.currentIndex()}~{self.Label3_arg5_value.text()}"
        arg6 = f"{self.Label3_arg6.currentIndex()}~{self.Label3_arg6_value.text()}"
        arg7 = f"{self.Label3_arg7.currentIndex()}~{self.Label3_arg7_value.text()}"
        arg8 = f"{self.Label3_arg8.currentIndex()}~{self.Label3_arg8_value.text()}"
        arg9 = f"{self.Label3_arg9.currentIndex()}~{self.Label3_arg9_value.text()}"
        arg10 = f"{self.Label3_arg10.currentIndex()}~{self.Label3_arg10_value.text()}"
        arg11 = f"{self.Label3_arg11.currentIndex()}~{self.Label3_arg11_value.text()}"
        arg12 = f"{self.Label3_arg12.currentIndex()}~{self.Label3_arg12_value.text()}"
        arg13 = f"{self.Label3_arg13.currentIndex()}~{self.Label3_arg13_value.text()}"
        arg14 = f"{self.Label3_arg14.currentIndex()}~{self.Label3_arg14_value.text()}"
        arg15 = f"{self.Label3_arg15.currentIndex()}~{self.Label3_arg15_value.text()}"
        arg16 = f"{self.Label3_arg16.currentIndex()}~{self.Label3_arg16_value.text()}"

        data = {
            "enable": enable,
            "arg1": arg1,
            "arg2": arg2,
            "arg3": arg3,
            "arg4": arg4,
            "arg5": arg5,
            "arg6": arg6,
            "arg7": arg7,
            "arg8": arg8,
            "arg9": arg9,
            "arg10": arg10,
            "arg11": arg11,
            "arg12": arg12,
            "arg13": arg13,
            "arg14": arg14,
            "arg15": arg15,
            "arg16": arg16,
        }
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[3]}", "w+") as file:
                yaml.dump(data, file)
            self.popup.whenCall(heading="Success", mesg="Data Save Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def saveLabel4Data(self):
        enable = self.checkBox_5.isChecked()
        arg1 = f"{self.Label4_arg1.currentIndex()}~{self.Label4_arg1_value.text()}"
        arg2 = f"{self.Label4_arg2.currentIndex()}~{self.Label4_arg2_value.text()}"
        arg3 = f"{self.Label4_arg3.currentIndex()}~{self.Label4_arg3_value.text()}"
        arg4 = f"{self.Label4_arg4.currentIndex()}~{self.Label4_arg4_value.text()}"
        arg5 = f"{self.Label4_arg5.currentIndex()}~{self.Label4_arg5_value.text()}"
        arg6 = f"{self.Label4_arg6.currentIndex()}~{self.Label4_arg6_value.text()}"
        arg7 = f"{self.Label4_arg7.currentIndex()}~{self.Label4_arg7_value.text()}"
        arg8 = f"{self.Label4_arg8.currentIndex()}~{self.Label4_arg8_value.text()}"
        arg9 = f"{self.Label4_arg9.currentIndex()}~{self.Label4_arg9_value.text()}"
        arg10 = f"{self.Label4_arg10.currentIndex()}~{self.Label4_arg10_value.text()}"
        arg11 = f"{self.Label4_arg11.currentIndex()}~{self.Label4_arg11_value.text()}"
        arg12 = f"{self.Label4_arg12.currentIndex()}~{self.Label4_arg12_value.text()}"
        arg13 = f"{self.Label4_arg13.currentIndex()}~{self.Label4_arg13_value.text()}"
        arg14 = f"{self.Label4_arg14.currentIndex()}~{self.Label4_arg14_value.text()}"
        arg15 = f"{self.Label4_arg15.currentIndex()}~{self.Label4_arg15_value.text()}"
        arg16 = f"{self.Label4_arg16.currentIndex()}~{self.Label4_arg16_value.text()}"

        data = {
            "enable": enable,
            "arg1": arg1,
            "arg2": arg2,
            "arg3": arg3,
            "arg4": arg4,
            "arg5": arg5,
            "arg6": arg6,
            "arg7": arg7,
            "arg8": arg8,
            "arg9": arg9,
            "arg10": arg10,
            "arg11": arg11,
            "arg12": arg12,
            "arg13": arg13,
            "arg14": arg14,
            "arg15": arg15,
            "arg16": arg16,
        }
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[4]}", "w+") as file:
                yaml.dump(data, file)
            self.popup.whenCall(heading="Success", mesg="Data Save Successful")
        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")

    def generateBarcodeData(self):
        self.label_149.setText(Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[0]}"))

    def generateLabel1Data(self):
        self.label_151.setText(Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[1]}"))

    def generateLabel2Data(self):
        self.label_153.setText(Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[2]}"))

    def generateLabel3Data(self):
        self.label_155.setText(Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[3]}"))

    def generateLabel4Data(self):
        self.label_157.setText(Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[4]}"))

    def generateLabelPrint(self):
        print("GeneratingBarcode")
        print_count = self.spinBox_2.value()
        counter_increament = self.checkBox_6.isChecked()
        if counter_increament == True:
            start_counter = self.spinBox.value()
            for i in range(print_count):
                print(f"Print Count: {i}")
                barcode = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[0]}", serialNo=start_counter)
                label_1 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[1]}", serialNo=start_counter)
                label_2 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[2]}", serialNo=start_counter)
                label_3 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[3]}", serialNo=start_counter)
                label_4 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[4]}", serialNo=start_counter)
                labels = [label_1, label_2, label_3, label_4]

                label_writer = LabelWriter(f"Recipes/{self.name[0]}/{self.name[1]}/template.html",
                                        default_stylesheets=(f"Recipes/{self.name[0]}/{self.name[1]}/style.css",))
                records = [
                    dict(sample_id=barcode, sample_name=labels)
                ]

                label_writer.write_labels(records, target='testLabel.pdf')

                with open("Config/PrinterData.yaml") as file:
                    data = yaml.load(file, Loader=yaml.SafeLoader)

                if self.name[0] == "Station_01":
                    for i in range(2):
                        os.system(f'PDFtoPrinter.exe testLabel.pdf -p "{data["st_01_printer"]}"')
                if self.name[1] == "Station_02":
                    os.system(f'PDFtoPrinter.exe label.pdf -p "{data["st_02_printer"]}"')
                start_counter += 1

        else:
            barcode = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[0]}", serialNo=self.spinBox.value())
            label_1 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[1]}", serialNo=self.spinBox.value())
            label_2 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[2]}", serialNo=self.spinBox.value())
            label_3 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[3]}", serialNo=self.spinBox.value())
            label_4 = Decoder(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[4]}", serialNo=self.spinBox.value())
            labels = [label_1, label_2, label_3, label_4]

            label_writer = LabelWriter(f"Recipes/{self.name[0]}/{self.name[1]}/template.html",
                                    default_stylesheets=(f"Recipes/{self.name[0]}/{self.name[1]}/style.css",))
            records = [
                dict(sample_id=barcode, sample_name=labels)
            ]

            label_writer.write_labels(records, target='testLabel.pdf')

            with open("Config/PrinterData.yaml") as file:
                data = yaml.load(file, Loader=yaml.SafeLoader)

            if self.name[0] == "Station_01":
                for i in range(print_count):
                    print(f"Print Count: {i}")
                    os.system(f'PDFtoPrinter.exe testLabel.pdf -p "{data["st_01_printer"]}"')
            if self.name[1] == "Station_02":
                os.system(f'PDFtoPrinter.exe label.pdf -p "{data["st_02_printer"]}"')

        self.popup.whenCall(heading="Success !!", mesg="Print Successful")
        

    def saveGenCode(self):
        css = (f"\n"
               "            @page {\n"
               f"                width: {self.doubleSpinBox_7.value()}mm;\n"
               f"                height: {self.doubleSpinBox_6.value()}mm;\n"
               f"                padding-left: {self.doubleSpinBox_9.value()}mm;\n"
               f"                padding-top : {self.doubleSpinBox_8.value()}mm;\n"
               "            }\n"
               f"            \n"
               "            img {\n"
               f"                height: {self.doubleSpinBox_10.value()}mm;\n"
               f"                width: {self.doubleSpinBox_11.value()}mm;\n"
               f"                image-rendering: pixelated;\n"
               f"                padding-left:{self.doubleSpinBox_13.value()}mm;\n"
               f"                padding-top:{self.doubleSpinBox_12.value()}mm;\n"
               "            }\n"
               f"            \n"
               "            .label_1 {\n"
               f"                font-family: Verdana;\n"
               f"                font-weight: {self.comboBox.currentText()};\n"
               f"                font-size:{self.doubleSpinBox_2.value()}mm;\n"
               f"                padding-left:{self.doubleSpinBox_15.value()}mm;\n"
               f"                padding-top:{self.doubleSpinBox_14.value()}mm;\n"
               f"                text-align:center;\n"
               "            }\n"
               f"            \n"
               "            .label_2 {\n"
               f"                font-family: Verdana;\n"
               f"                font-weight: {self.comboBox_2.currentText()};\n"
               f"                font-size:{self.doubleSpinBox_3.value()}mm;\n"
               f"                padding-left:{self.doubleSpinBox_17.value()}mm;\n"
               f"                padding-top:{self.doubleSpinBox_16.value()}mm;\n"
               f"                text-align:center;\n"
               "            }\n"
               "            .label_3 {\n"
               f"                font-family: Verdana;\n"
               f"                font-weight: {self.comboBox_3.currentText()};\n"
               f"                font-size:{self.doubleSpinBox_4.value()}mm;\n"
               f"                padding-left:{self.doubleSpinBox_18.value()}mm;\n"
               f"                padding-top:{self.doubleSpinBox_19.value()}mm;\n"
               f"                text-align:center;\n"
               "            }\n"
               f"            \n"
               "            .label_4 {\n"
               f"                font-family: Verdana;\n"
               f"                font-weight: {self.comboBox_4.currentText()};\n"
               f"                font-size:{self.doubleSpinBox_5.value()}mm;\n"
               f"                padding-left:{self.doubleSpinBox_21.value()}mm;\n"
               f"                padding-top:{self.doubleSpinBox_20.value()}mm;\n"
               f"                text-align:center;\n"
               "            }\n"
               f"       ")
        try:
            with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[6]}", "w+") as file:
                file.writelines(css)

            # width: {self.doubleSpinBox_7.value()}
            # mm;\n
            # "
            # f"                height: {self.doubleSpinBox_6.value()}mm;\n"
            # f"                padding-left: {self.doubleSpinBox_9.value()}mm;\n"
            # f"                padding-top : {self.doubleSpinBox_8.value()}mm;\n"

            data = {
                "page" : {
                    "height" : self.doubleSpinBox_6.value(),
                    "width" : self.doubleSpinBox_7.value(),
                    "p_left": self.doubleSpinBox_9.value(),
                    "p_top": self.doubleSpinBox_8.value()
                },
                "img" : {
                    "height" : self.doubleSpinBox_10.value(),
                    "width" : self.doubleSpinBox_11.value(),
                    "p_left" : self.doubleSpinBox_13.value(),
                    "p_top" : self.doubleSpinBox_12.value()
                },
                "label_1" : {
                    "font-weight" : self.comboBox.currentText(),
                    "font-size" : self.doubleSpinBox_2.value(),
                    "p_left" : self.doubleSpinBox_15.value(),
                    "p_top" : self.doubleSpinBox_14.value()
                },
                "label_2" : {
                    "font-weight" : self.comboBox_2.currentText(),
                    "font-size" : self.doubleSpinBox_3.value(),
                    "p_left" : self.doubleSpinBox_17.value(),
                    "p_top" : self.doubleSpinBox_16.value()
                },
                "label_3" : {
                    "font-weight" : self.comboBox_3.currentText(),
                    "font-size" : self.doubleSpinBox_4.value(),
                    "p_left" : self.doubleSpinBox_18.value(),
                    "p_top" : self.doubleSpinBox_19.value()
                },
                "label_4" : {
                    "font-weight" : self.comboBox_4.currentText(),
                    "font-size" : self.doubleSpinBox_5.value(),
                    "p_left" : self.doubleSpinBox_21.value(),
                    "p_top" : self.doubleSpinBox_20.value()
                },
            }

            try:
                with open(f"Recipes/{self.name[0]}/{self.name[1]}/{self.fileList[7]}", "w+") as file:
                    yaml.dump(data, file)
            except Exception as e:
                print(f"Label Specification not save dua to {e}.")


            self.popup.whenCall(heading="Success !!", mesg="File Saved Successful !!")

        except Exception as e:
            self.popup.whenCall(heading="Error !!", mesg=f"{e}")
