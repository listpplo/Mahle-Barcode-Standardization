import os
import threading

from pymelsec import Type3E
from pymelsec.constants import DT
from PySide6.QtCore import QThread, Signal, Slot
from Decoder import Decoder
import yaml
from blabel import LabelWriter


# self.keys = {"command_st01": self.lineEdit_3,
#              "printCount_st01": self.lineEdit_4,
#              "serialNo_st01": self.lineEdit_18,
#              "barcode_st01": self.lineEdit_14,
#              "respReg_st01": self.lineEdit_23,
#              "command_st02": self.lineEdit_9,
#              "printCount_st02": self.lineEdit_11,
#              "serialNo_st02": self.lineEdit_20,
#              "barcode_st02": self.lineEdit_22,
#              "respReg_st02": self.lineEdit_15,
#              "heartBeat": self.lineEdit_13,
#              "scanTime": self.lineEdit_7,
#              "plcTimeOut": self.lineEdit_8,
#              }

class nameHelper:
    command_st01 = "command_st01"
    printCount_st01 = "printCount_st01"
    printRecipe_st01 = "printRecipe_st01"
    serialNo_st01 = "serialNo_st01"
    barcode_st01 = "barcode_st01"
    respReg_st01 = "respReg_st01"
    command_st02 = "command_st02"
    printCount_st02 = "printCount_st02"
    printRecipe_st02 = "printRecipe_st02"
    serialNo_st02 = "serialNo_st02"
    barcode_st02 = "barcode_st02"
    respReg_st02 = "respReg_st02"
    heartBeat = "heartBeat"
    scanTime = "scanTime"
    plcTimeOut = "plcTimeOut"


def lst_to_str(lst):
    str1 = ""
    for item in lst:
        my_int = int(bin(item.value), base=2)
        string = my_int.to_bytes((my_int.bit_length() + 7) // 8, "big").decode()[::-1]
        if string != " ":
            str1 = str1 + string
    return str1

class PLC(QThread):
    logSignal = Signal(str)
    fendSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.runThread = True
        self.plc = None
        self.fileList = ["barcode.yaml", "label1.yaml", "label2.yaml", "label3.yaml", "label4.yaml", "template.html",
                         "style.css"]

    def run(self):
        self.runThread = True
        
        try:
            self.logSignal.emit("Sequence:File Loading:Loading PLC File")
            with open("Config/PLC.yaml") as file:
                plcData = yaml.load(file, Loader=yaml.SafeLoader)
        except Exception as e:
            self.logSignal.emit(f"Error:PLC Thread Error:{e}")

        # Loading the PLC DataReg
        try:
            self.logSignal.emit("Sequence:File Loading:Loading the DataReg File")
            with open("Config/PLCDataReg.yaml") as file:
                dataReg = yaml.load(file, Loader=yaml.SafeLoader)
        except Exception as e:
            self.logSignal.emit(f"Error:PLC Thread Error:{e}")

        # Loading the Mapping ST01
        try:
            self.logSignal.emit("Sequence:File Loading:Loading Mapping Data St-01")
            with open("Config/Mapping-Station_01.yaml") as file:
                map_st01 = yaml.load(file, Loader=yaml.SafeLoader)
        except Exception as e:
            self.logSignal.emit(f"Error:PLC Thread Error:{e}")

            # Loading the Mapping ST02
            try:
                self.logSignal.emit("Sequence:File Loading:Loading Mapping Data St-02")
                with open("Config/Mapping-Station_02.yaml") as file:
                    map_st02 = yaml.load(file, Loader=yaml.SafeLoader)
            except Exception as e:
                self.logSignal.emit(f"Error:PLC Thread Error:{e}")

            # Loading printers
            try:
                self.logSignal.emit("Sequence:File Loading:Loading Printer Data")
                with open("Config/PrinterData.yaml") as file:
                    printerData = yaml.load(file, Loader=yaml.SafeLoader)
            except Exception as e:
                self.logSignal.emit(f"Error:PLC Thread Error:{e}")

        while self.runThread:
            if self.plc is None:
                try:
                    self.logSignal.emit("Sequence:Connection:Connecting to PLC")
                    self.plc = Type3E(host=plcData["ip"], port=plcData["port"], plc_type="Q")
                    self.plc.connect(port=plcData["port"], ip=plcData["ip"])
                except Exception as e:
                    self.logSignal.emit(f"Error:PLC Thread Error:{e}")
                    self.plc = None
                    QThread.sleep(3)
                    print(e)
            else:
                try:
                    command_st01 = self.plc.batch_read(ref_device=dataReg[nameHelper.command_st01], data_type=DT.UWORD, read_size=1)[0].value
                    match command_st01:
                        case 0:
                            pass
                       
                        case 1:
                            try:
                                # Print Command From the PLC
                                self.logSignal.emit("Sequence:Barcode Generation:Generating the Required Barcode")
                                ntp = self.plc.batch_read(ref_device=dataReg[nameHelper.printCount_st01], read_size=1, data_type=DT.UWORD)[0].value  # Number of labels to print
                                serialNo = self.plc.batch_read(ref_device=dataReg[nameHelper.serialNo_st01], read_size=1, data_type=DT.UWORD)[0].value  # Serial Number of the label
                                recipeNo = self.plc.batch_read(ref_device=dataReg[nameHelper.printRecipe_st01], read_size=1, data_type=DT.UWORD)[0].value  # recipe selection
                                
                                # Sending the values to the front end
                                self.fendSignal.emit(f"ST-01:recipe:{map_st01[f'{recipeNo}']}")
                                self.fendSignal.emit(f"ST-01:serialNo:{serialNo}")

                                # now decoding the values
                                barcode = Decoder(f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[0]}", serialNo)
                                label1 = Decoder(f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[1]}", serialNo)
                                label2 = Decoder(f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[2]}", serialNo)
                                label3 = Decoder(f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[3]}", serialNo)
                                label4 = Decoder(f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[4]}", serialNo)

                                labels = [label1, label2, label3, label4]

                                labelGen = LabelWriter(
                                    item_template_path=f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[5]}",
                                    default_stylesheets=f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[6]}")

                                records = [
                                    dict(sample_id=barcode, sample_name=labels)
                                ]

                                labelGen.write_labels(records, target="St01.pdf")

                                for i in range(ntp):
                                    try:
                                        threading.Thread(target=lambda _: os.system(
                                            f"PDFtoPrinter.exe St01.pdf -p '{printerData['st_01_printer']}'")).start()
                                    except Exception as e:
                                        self.logSignal.emit(f"Error:PLC Printing Thread:{e}")

                                # Printing Conform Signal
                                self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st01], values=[1])
                                QThread.sleep(1)
                                self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st01], values=[0])
                            
                            except Exception as e:
                                self.logSignal.emit(f"Error:PLC Gen:{e}")

                        case 2:
                            try:
                                # Barcode Validation
                                serialNo = self.plc.batch_read(ref_device=dataReg[nameHelper.serialNo_st01], read_size=1, data_type=DT.UWORD)[0].value  # Serial Number of the label
                                recipeNo = self.plc.batch_read(ref_device=dataReg[nameHelper.printRecipe_st01], read_size=1, data_type=DT.UWORD)[0].value  # recipe selection

                                # now decoding the values
                                barcode = Decoder(f"Recipes/Station_01/{map_st01[f'{recipeNo}']}/{self.fileList[0]}", serialNo)

                                # getting barcode from plc
                                barcode_plc = lst_to_str(
                                    self.plc.batch_read(ref_device=dataReg[nameHelper.barcode_st01], read_size=20, data_type=DT.UWORD)
                                ).split(" ")[0]

                                # Sending barcode to front end
                                self.fendSignal.emit(f"ST-01:Barcode:{barcode}")

                                if barcode == barcode_plc:
                                    self.logSignal.emit("Sequence: Barcode Check: Barcode Check Successful")
                                    self.fendSignal.emit("ST-01:Barcode Check:OK")
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st01], values=[2], data_type=Dt.UWORD)
                                    QThread.sleep(1)
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st01], values=[0], data_type=Dt.UWORD)
                                else:
                                    self.fendSignal.emit("ST-01:Barcode Check:NG")
                                    self.logSignal.emit("Sequence:Validation Error: Generated and Printed Barcode Falied")
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st01], values=[3], data_type=Dt.UWORD)
                                    QThread.sleep(1)
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st01], values=[0], data_type=Dt.UWORD)
                            except Exception as e:
                                self.logSignal.emit(f"Error:Barcode Validation Error:{e}")

                    command_st02 = self.plc.batch_read(ref_device=dataReg[nameHelper.command_st02], data_type=DT.UWORD, read_size=1)[0].value
                    match command_st02:
                        case 0:
                            pass
                       
                        case 1:
                            try:
                                # Print Command From the PLC
                                self.logSignal.emit("Sequence:Barcode Generation:Generating the Required Barcode St02")
                                ntp = self.plc.batch_read(ref_device=dataReg[nameHelper.printCount_st02], read_size=1, data_type=DT.UWORD)[0].value  # Number of labels to print
                                serialNo = self.plc.batch_read(ref_device=dataReg[nameHelper.serialNo_st02], read_size=1, data_type=DT.UWORD)[0].value  # Serial Number of the label
                                recipeNo = self.plc.batch_read(ref_device=dataReg[nameHelper.printRecipe_st02], read_size=1, data_type=DT.UWORD)[0].value  # recipe selection
                                
                                # Sending the values to the front end
                                self.fendSignal.emit(f"ST-02:recipe:{map_st02[f'{recipeNo}']}")
                                self.fendSignal.emit(f"ST-02:serialNo:{serialNo}")

                                # now decoding the values
                                barcode = Decoder(f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[0]}", serialNo)
                                label1 = Decoder(f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[1]}", serialNo)
                                label2 = Decoder(f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[2]}", serialNo)
                                label3 = Decoder(f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[3]}", serialNo)
                                label4 = Decoder(f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[4]}", serialNo)

                                labels = [label1, label2, label3, label4]

                                labelGen = LabelWriter(
                                    item_template_path=f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[5]}",
                                    default_stylesheets=f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[6]}")

                                records = [
                                    dict(sample_id=barcode, sample_name=labels)
                                ]

                                labelGen.write_labels(records, target="St02.pdf")

                                for i in range(ntp):
                                    try:
                                        threading.Thread(target=lambda _: os.system(
                                            f"PDFtoPrinter.exe St02.pdf -p '{printerData['st_02_printer']}'")).start()
                                    except Exception as e:
                                        self.logSignal.emit(f"Error:PLC Printing Thread ST-02:{e}")

                                # Printing Conform Signal
                                self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st02], values=[1])
                                QThread.sleep(1)
                                self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st02], values=[0])
                            
                            except Exception as e:
                                self.logSignal.emit(f"Error:PLC Gen:{e}")

                        case 2:
                            try:
                                # Barcode Validation
                                serialNo = self.plc.batch_read(ref_device=dataReg[nameHelper.serialNo_st02], read_size=1, data_type=DT.UWORD)[0].value  # Serial Number of the label
                                recipeNo = self.plc.batch_read(ref_device=dataReg[nameHelper.printRecipe_st02], read_size=1, data_type=DT.UWORD)[0].value  # recipe selection

                                # now decoding the values
                                barcode = Decoder(f"Recipes/Station_02/{map_st02[f'{recipeNo}']}/{self.fileList[0]}", serialNo)

                                # getting barcode from plc
                                barcode_plc = lst_to_str(
                                    self.plc.batch_read(ref_device=dataReg[nameHelper.barcode_st02], read_size=20, data_type=DT.UWORD)
                                ).split(" ")[0]

                                # Sending barcode to front end
                                self.fendSignal.emit(f"ST-02:Barcode:{barcode}")

                                if barcode == barcode_plc:
                                    self.logSignal.emit("Sequence: Barcode Check: Barcode Check Successful ST-02")
                                    self.fendSignal.emit("ST-02:Barcode Check:OK")
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st02], values=[2], data_type=Dt.UWORD)
                                    QThread.sleep(1)
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st02], values=[0], data_type=Dt.UWORD)
                                else:
                                    self.fendSignal.emit("ST-02:Barcode Check:NG")
                                    self.logSignal.emit("Sequence: Validation Error: Generated and Printed Barcode Falied on St-02")
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st02], values=[3], data_type=Dt.UWORD)
                                    QThread.sleep(1)
                                    self.plc.batch_write(ref_device=dataReg[nameHelper.respReg_st02], values=[0], data_type=Dt.UWORD)
                            except Exception as e:
                                self.logSignal.emit(f"Error:Barcode Validation Error ST02:{e}")

                except Exception as e:
                    self.logSignal.emit(f"Error:PLC Thread Error:{e}")
                    self.plc = None

    def terminate(self):
        self.logSignal.emit("Sequence:PLC Server Shutdown")
        self.runThread = False
        del self.plc
        self.plc = None
        super().terminate()

    @Slot(str)
    def commandHandler(self, command: str):
        command_split = command.split(":")
        match command_split[0]:
            case "Stop":
                self.runThread = False
            case "run":
                self.runThread = True
