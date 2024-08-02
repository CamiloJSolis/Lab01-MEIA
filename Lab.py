import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QLineEdit, QApplication, QPushButton, QFileDialog, QMessageBox,
QLabel, QPlainTextEdit, QApplication, QDialog, QFileDialog)
from PyQt5.uic import loadUi

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        loadUi("Lab.ui",self)

        # Definiendo los widgets
        self.save_button = self.findChild(QPushButton, "save_btn")
        self.open_button = self.findChild(QPushButton, "open_btn")
        self.statistics_button = self.findChild(QPushButton, "statistics_btn")
        self.path_label = self.findChild(QLabel, "path_label")
        self.path_line_edit = self.findChild(QLineEdit, "path_line_edit")
        self.statistics_text_edit = self.findChild(QPlainTextEdit,"statistics_TextEdit")

        # Acciones de los botones
        self.save_button.clicked.connect(self.save_button_clicked)
        self.open_button.clicked.connect(self.open_button_clicked)
        self.statistics_button.clicked.connect(self.statistics_button_clicked)
    def save_button_clicked(self):
        save_file = QFileDialog.saveFileContent(self, "Save File", "*")
    def open_button_clicked(self):
        # Open file dialog
        file_name = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*.txt)")
        # Output file name to the screen
        if file_name:
            self.path_line_edit.setText(str(file_name))
            self.statistics_text_edit.show()
            self.statistics_text_edit.QPlainTextEdit.appendPlainText(self.path_line_edit.text())


    def statistics_button_clicked(self):
        self.window().setWindowTitle("Stat")

# Run the app
app = QApplication(sys.argv)
UIWindow = UI()
UIWindow.show()
app.exec_()