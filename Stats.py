import ui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QLineEdit, QMessageBox, QDialog)


class StatsForm(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("StatGUI.ui", self)

        self.tot_lines_lineEdit = self.findChild(QLineEdit, "tot_lines_lineEdit")
        self.tot_digits_lineEdit = self.findChild(QLineEdit, "tot_digits_lineEdit")
        self.tot_grades_lineEdit = self.findChild(QLineEdit, "tot_grades_lineEdit")
        self.tot_symbol_lineEdit = self.findChild(QLineEdit, "tot_symbol_lineEdit")
        self.show_st_100_pts_lineEdit = self.findChild(QLineEdit, "show_st_100_pts_lineEdit")
        self.show_st_0_grade_lineEdit = self.findChild(QLineEdit, "show_st_0_grade_lineEdit")
        self.show_passed_st_percent_ineEdit = self.findChild(QLineEdit, "show_passed_st_percent_ineEdit")
        self.show_failed_st_percent_lineEdit = self.findChild(QLineEdit, "show_failed_st_percent_lineEdit")
        self.show_average_grade_lineEdit = self.findChild(QLineEdit, "show_average_grade_lineEdit")

    def show_total_lines(self, data):
        try:
            if not data:
                QMessageBox.critical(self, "Error", "No se encuentran datos")
            else:
                counter = 0
                for line in data.splitlines():
                    counter += 1
                self.tot_lines_lineEdit.setText(str(counter))
        except Exception as e:
            QMessageBox.critical(self, "Error en mostrar las lineas", str(e))

    def show_total_digits(self, data):
        try:
            if not data:
                QMessageBox.critical(self, "Error", "No se encuentran datos")
            else:
                digitscount = 0
                for digit in data:
                    if digit.isdigit():
                        digitscount += 1
                self.tot_digits_lineEdit.setText(str(digitscount))
        except Exception as e:
            QMessageBox.critical(self, "Error en mostrar los dígitos", str(e))

    def show_grades_count(self, data):
        try:
            if not data:
                QMessageBox.critical(self, "Error", "No se encuentran datos")
            else:
                total_sum = 0
                hundred_count = 0
                zero_count = 0
                grade_count = 0
                current_number = ""

                for grade in data:
                    if grade.isdigit():
                        current_number += grade
                    else:
                        if current_number:
                            number = float(current_number)
                            grade_count += 1
                            total_sum += number
                            if number == 0:
                                zero_count += 1
                            elif number == 100:
                                hundred_count += 1
                            current_number = ""

                if current_number:
                    number = float(current_number)
                    grade_count += 1
                    total_sum += number
                    if number == 100:
                        hundred_count += 1
                    elif number == 0:
                        zero_count += 1

                if grade_count == 0:
                    average = 0
                else:
                    average = total_sum / grade_count

                passed_percentage = (hundred_count / grade_count) * 100 if grade_count >= 0 else 0

                failed_percentage = (zero_count / grade_count) * 100 if grade_count >= 0 else 0

                self.show_st_100_pts_lineEdit.setText(str(hundred_count))
                self.show_st_0_grade_lineEdit.setText(str(zero_count))
                self.show_passed_st_percent_ineEdit.setText(str(round(passed_percentage, 2)))
                self.show_failed_st_percent_lineEdit.setText(str(round(failed_percentage, 2)))
                self.show_average_grade_lineEdit.setText(str(round(average, 2)))
                self.tot_grades_lineEdit.setText(str(grade_count))
        except Exception as e:
            QMessageBox.critical(self, "Error en mostrar el conteo de notas", str(e))

    def show_total_hyphens(self, data):
        try:
            if not data:
                QMessageBox.critical(self, "Error", "No se encuentran datos")
            else:
                hyphen_count = 0
                for line in data:
                    for digit in line:
                        if digit == '-':
                            hyphen_count += 1
                    self.tot_symbol_lineEdit.setText(str(hyphen_count))
        except Exception as e:
            QMessageBox.critical(self, "Error en mostrar los '-'", str(e))

    # def show_calculations(self, hundred_count, zero_count, passed_percentage, failed_percentage, average,
    #                       grade_count):
    #     try:
    #         self.show_st_100_pnts_lineEdit(str(hundred_count))
    #         self.show_st_0_grade_lineEdit(str(zero_count))
    #         self.show_passed_st_percent_ineEdit(str(passed_percentage))
    #         self.show_failed_st_percent_lineEdit(str(failed_percentage))
    #         self.show_average_grade_lineEdit(str(average))
    #         self.tot_grades_lineEdit.setText(str(grade_count))
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error en mostrar los cálculos", str(e))