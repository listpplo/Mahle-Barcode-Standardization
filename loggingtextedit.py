from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot
from datetime import datetime

class LoggingTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.max_lines = 1000
        self.count = 0

    @Slot(str)
    def log(self, command:str):
        self.count +=1
        logger = f"{self.count:05d}->{datetime.now()} -> {command}"
        self.append(logger)
        self.check_line_count()
        self.append("************************************************************************************")

    def check_line_count(self):
        # Get the document text and split into lines
        text = self.toPlainText()
        lines = text.split('\n')

        # If the number of lines is greater than max_lines, remove the first lines
        if len(lines) > self.max_lines:
            excess_lines = len(lines) - self.max_lines
            # Join the remaining lines and set the text
            new_text = '\n'.join(lines[excess_lines:])
            self.setPlainText(new_text)
            # Move the cursor to the end of the text
            self.moveCursor(QTextCursor.End)