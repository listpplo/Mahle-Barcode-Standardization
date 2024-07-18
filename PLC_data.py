from pymelsec import Type3E
from pymelsec.constants import DT
from PySide6.QtCore import QThread, Signal, Slot
import yaml


class PLC(QThread):
    fendSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.runThread = True
        self.plc = None

    def run(self):
        try:
            with open("Config/PLC.yaml") as file:
                plcData = yaml.load(file, Loader=yaml.SafeLoader)
        except Exception as e:
            self.fendSignal.emit(f"Error:PLC Thread Error:{e}")

        try:
            with open("Config/PLCDataReg.yaml") as file:
                dataReg = yaml.load(file, Loader=yaml.SafeLoader)
        except Exception as e:
            self.fendSignal.emit(f"Error:PLC Thread Error:{e}")

        while self.runThread:
            if self.plc is None:
                try:
                    self.plc = Type3E(host=plcData["ip"], port=plcData["port"], plc_type="Q")
                    self.plc.connect(port=plcData["port"], ip=plcData["ip"])
                except Exception as e:
                    self.fendSignal.emit(f"Error:PLC Thread Error:{e}")
            else:
                try:
                    command = self.plc.batch_read(ref_device=dataReg["data1"], data_type=DT.UWORD, read_size=1)
                    match command:
                        case 0:
                            pass
                        case 1:
                            ntp = self.plc.batch_read(ref_device=dataReg["data2"], read_size=1, data_type=DT.UWORD)
                except Exception as e:
                    self.fendSignal.emit(f"Error:PLC Thread Error:{e}")


    def terminate(self):
        self.runThread = False
        super().terminate()

    @Slot(str)
    def commandHandler(self, command:str):
        command_split = command.split(":")
        match command_split[0]:
            case "Stop":
                self.runThread = False
            case "run":
                self.runThread = True
