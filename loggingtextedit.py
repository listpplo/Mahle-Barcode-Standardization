from PySide6.QtWidgets import  QTextEdit
from datetime import datetime

class LoggingTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.count = 0

    def log(self, command:str):
        self.count +=1
        logger = f"{self.count:05d}->{datetime.now()} -> {command}"
        self.append(logger)
        self.append("************************************************************************************")