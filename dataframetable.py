from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
import pandas as pd
import datetime


class DataFrameTable(QTableWidget):
    df = None

    def __init__(self, parent):
        super().__init__()
        self.setAlternatingRowColors(True)

    def getDataFrame(self) -> pd.DataFrame:
        if self.df is None:
            raise ValueError("No dataframe found")
        else:
            return self.df

    def makeTable(self, df: pd.DataFrame) -> None:
        self.clear()
        self.setRowCount(0)
        self.df = df
        if self.df is None:
            raise ValueError("Please initialize the datatable with setDataFrame")
        else:
            count = 0
            header = self.df.keys()
            self.setColumnCount(len(self.df.keys()))
            self.setHorizontalHeaderLabels(header)
            row = 0
            for items in self.df.iterrows():
                col = 0
                self.setRowCount(row + 1)
                for item in items[1]:
                    i = QTableWidgetItem(f"{item}")
                    if item == "OK":
                        i.setBackground(QColor(0, 255, 0))
                    if item == "NG":
                        i.setBackground(QColor(255, 0, 0))
                    if item == "N/A" or item == None:
                        i.setBackground(QColor(255, 255, 0))
                    if item == "TESTING":
                        i.setBackground(QColor(255, 130, 130))

                    i.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.setItem(row, col, i)
                    col += 1
                self.setRowHeight(row, 80)
                row += 1

        self.resizeColumn()

    def resizeColumn(self):
        for i in range(self.columnCount()):
            self.setColumnWidth(i, 200)
        self.resizeRowsToContents()