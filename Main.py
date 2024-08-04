import sys
from PyQt5.QtWidgets import (QMainWindow, QLineEdit,QPushButton, QMessageBox,                             QLabel, QPlainTextEdit, QApplication, QFileDialog)
from PyQt5.uic import loadUi
from Stats import StatsForm


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("GUI.ui", self)

        # Definiendo los widgets
        self.save_button = self.findChild(QPushButton, "save_btn")
        self.open_button = self.findChild(QPushButton, "open_btn")
        self.statistics_button = self.findChild(QPushButton, "statistics_btn")

        self.path_label = self.findChild(QLabel, "path_label")
        self.path_line_edit = self.findChild(QLineEdit, "path_line_edit")
        self.txt_content_TextEdit = self.findChild(QPlainTextEdit, "txt_content_TextEdit")

        # Acciones de los botones
        self.save_button.clicked.connect(self.save_button_clicked)
        self.open_button.clicked.connect(self.open_button_clicked)
        self.statistics_button.clicked.connect(self.statistics_button_clicked)
        self.statistics_button.setEnabled(False)

        self.data = ""

    def save_button_clicked(self):
        save_file, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if save_file:
            f = open(save_file, "w")

            with f:
                try:
                    text = self.txt_content_TextEdit.toPlainText()
                    f.write(text)

                    QMessageBox.about(self, "Save File", "Archivo guardado exitosamente")
                    clear_field = self.txt_content_TextEdit
                    clear_field.clear()
                except Exception as e:
                    QMessageBox.Critical(self, "Save File", f"Ocurrió un error al guardar el archivo {e}")

    def open_button_clicked(self):
        # Open file dialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_name:
            try:
                with open(file_name, "r") as f:
                    self.data = f.read()
                    self.path_line_edit.setText(file_name)
                    self.txt_content_TextEdit.setPlainText(self.data)
                    self.statistics_button.setEnabled(True)
            except Exception as e:
                QMessageBox.critical(self, "Open File", f"Failed to open file: {e}")

    def statistics_button_clicked(self):
        try:
            stats = StatsForm()
            stats.show_total_lines(self.data)
            stats.show_total_digits(self.data)
            stats.show_grades_count(self.data)
            stats.show_total_hyphens(self.data)
            stats.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Statistics", f"Failed to load {e}")


# Run the app
app = QApplication(sys.argv)
UIWindow = UI()
# stats = StatsForm()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(UIWindow)
# widget.addWidget(stats)
UIWindow.show()

try:
    app.exec_()
except Exception as e:
    QMessageBox.critical("Error", f"Failed to run the application: {e}")
