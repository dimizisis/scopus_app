
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import os
import sys
sys.path.append('../../')

class Ui_exportDialog(object):
    def setupUi(self, exportDialog, from_db=True, df=None):
        self.exportDialog = exportDialog
        self.exportDialog.setObjectName("exportDialog")
        self.exportDialog.resize(329, 467)
        self.exportDialog.setMaximumSize(QtCore.QSize(329, 467))
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.exportDialog.setWindowIcon(QIcon(scriptDir + os.path.sep + '../style/images/favicon.ico')) 
        self.export_grpbox = QtWidgets.QGroupBox(exportDialog)
        self.export_grpbox.setGeometry(QtCore.QRect(10, 10, 311, 391))
        self.export_grpbox.setObjectName("export_grpbox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.export_grpbox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 291, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.export_settings_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.export_settings_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.export_settings_verticalLayout.setObjectName("export_settings_verticalLayout")
        self.time_period_grpbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.time_period_grpbox.setMaximumSize(QtCore.QSize(289, 110))
        self.time_period_grpbox.setObjectName("time_period_grpbox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.time_period_grpbox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 171, 63))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.time_period_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.time_period_verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.time_period_verticalLayout.setSpacing(16)
        self.time_period_verticalLayout.setObjectName("time_period_verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.from_lbl = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.from_lbl.setMaximumSize(QtCore.QSize(50, 20))
        self.from_lbl.setObjectName("from_lbl")
        self.horizontalLayout_3.addWidget(self.from_lbl)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.from_year_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.from_year_combobox.setObjectName("from_year_combobox")
        self.horizontalLayout_3.addWidget(self.from_year_combobox)
        self.time_period_verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.to_lbl = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.to_lbl.setMaximumSize(QtCore.QSize(50, 20))
        self.to_lbl.setObjectName("to_lbl")
        self.horizontalLayout_4.addWidget(self.to_lbl)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.to_year_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.to_year_combobox.setObjectName("to_year_combobox")
        self.horizontalLayout_4.addWidget(self.to_year_combobox)
        self.time_period_verticalLayout.addLayout(self.horizontalLayout_4)
        self.export_settings_verticalLayout.addWidget(self.time_period_grpbox)
        self.inclusions_grpbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.inclusions_grpbox.setObjectName("inclusions_grpbox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.inclusions_grpbox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 171, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.inclusions_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.inclusions_verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.inclusions_verticalLayout.setSpacing(10)
        self.inclusions_verticalLayout.setObjectName("inclusions_verticalLayout")
        self.aggregated_data_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.aggregated_data_checkbox.setChecked(True)
        self.aggregated_data_checkbox.setObjectName("aggregated_data_checkbox")
        self.inclusions_verticalLayout.addWidget(self.aggregated_data_checkbox)
        self.diagrams_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.diagrams_checkbox.setChecked(True)
        self.diagrams_checkbox.setObjectName("diagrams_checkbox")
        self.inclusions_verticalLayout.addWidget(self.diagrams_checkbox)
        self.department_stats_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.department_stats_checkbox.setChecked(True)
        self.department_stats_checkbox.setObjectName("department_stats_checkbox")
        self.inclusions_verticalLayout.addWidget(self.department_stats_checkbox)
        self.professor_stats_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.professor_stats_checkbox.setObjectName("professor_stats_checkbox")
        self.inclusions_verticalLayout.addWidget(self.professor_stats_checkbox)
        self.export_settings_verticalLayout.addWidget(self.inclusions_grpbox)
        self.output_grpbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.output_grpbox.setMaximumSize(QtCore.QSize(289, 85))
        self.output_grpbox.setObjectName("output_grpbox")
        self.layoutWidget = QtWidgets.QWidget(self.output_grpbox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 271, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.output_verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.output_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.output_verticalLayout.setObjectName("output_verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.select_path_label = QtWidgets.QLabel(self.layoutWidget)
        self.select_path_label.setObjectName("select_path_label")
        self.horizontalLayout_9.addWidget(self.select_path_label)
        spacerItem2 = QtWidgets.QSpacerItem(14, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.export_path_textedit = QtWidgets.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.export_path_textedit.setFont(font)
        self.export_path_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_path_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_path_textedit.setReadOnly(True)
        self.export_path_textedit.setObjectName("export_path_textedit")
        self.horizontalLayout_9.addWidget(self.export_path_textedit)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.path_select_toolbtn = QtWidgets.QToolButton(self.layoutWidget)
        self.path_select_toolbtn.setStyleSheet("")
        self.path_select_toolbtn.setObjectName("path_select_toolbtn")
        self.path_select_toolbtn.clicked.connect(self.open_directory_dialog)
        self.horizontalLayout_8.addWidget(self.path_select_toolbtn)
        self.output_verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.export_filename_label = QtWidgets.QLabel(self.layoutWidget)
        self.export_filename_label.setObjectName("export_filename_label")
        self.horizontalLayout_10.addWidget(self.export_filename_label)
        self.export_filename_textedit = QtWidgets.QTextEdit(self.layoutWidget)
        self.export_filename_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_filename_textedit.setObjectName("export_filename_textedit")
        self.horizontalLayout_10.addWidget(self.export_filename_textedit)
        self.output_verticalLayout.addLayout(self.horizontalLayout_10)
        self.export_settings_verticalLayout.addWidget(self.output_grpbox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(exportDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 410, 312, 43))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.button_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.button_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_horizontalLayout.setSpacing(10)
        self.button_horizontalLayout.setObjectName("button_horizontalLayout")
        self.cancel_command_link_btn = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.cancel_command_link_btn.setMaximumSize(QtCore.QSize(150, 41))
        self.cancel_command_link_btn.setAutoRepeat(False)
        self.cancel_command_link_btn.setObjectName("cancel_command_link_btn")
        self.cancel_command_link_btn.clicked.connect(self.exportDialog.close)
        self.cancel_command_link_btn.setIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/delete.png'))
        self.button_horizontalLayout.addWidget(self.cancel_command_link_btn)
        self.export_command_link_btn = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.export_command_link_btn.setMaximumSize(QtCore.QSize(150, 41))
        self.export_command_link_btn.setObjectName("export_command_link_btn")
        self.export_command_link_btn.setIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/export.png'))
        self.button_horizontalLayout.addWidget(self.export_command_link_btn)

        self.verticalLayoutWidget.setStyleSheet("background-color: transparent;")
        self.verticalLayoutWidget_2.setStyleSheet("background-color: transparent;")
        self.verticalLayoutWidget_4.setStyleSheet("background-color: transparent;")
        self.horizontalLayoutWidget.setStyleSheet("background-color: transparent;")

        self.df = None

        ###### Fetch years from DB or Dataframe ######
        if from_db:
            self.to_year_combobox.addItems(self.fetch_years_from_db('DESC'))
            self.from_year_combobox.addItems(self.fetch_years_from_db('ASC'))
        else:
            self.df = df
            years = list(self.df['Year'].unique())
            years = [str(year) for year in years]
            years.sort(reverse=True)
            self.to_year_combobox.addItems(years)
            years.sort()
            self.from_year_combobox.addItems(years)

        ###### Set default export settings ######
        self.export_filename_textedit.setText(f'''STAT_EXPORT_{self.from_year_combobox.currentText()}-{self.to_year_combobox.currentText()}''' 
                                                if self.from_year_combobox.currentText() != self.to_year_combobox.currentText() else f'''STAT_EXPORT_{self.from_year_combobox.currentText()}''')
        self.export_path_textedit.setText(scriptDir + os.path.sep)

        self.from_year_combobox.currentTextChanged.connect(self.change_filename)
        self.to_year_combobox.currentTextChanged.connect(self.change_filename)

        self.export_command_link_btn.clicked.connect(self.export)
        self.professor_stats_checkbox.clicked.connect(self.open_professors_dialog)
        self.selected_professors = None

        self.retranslateUi(exportDialog)
        QtCore.QMetaObject.connectSlotsByName(exportDialog)

    def retranslateUi(self, exportDialog):
        _translate = QtCore.QCoreApplication.translate
        exportDialog.setWindowTitle(_translate("exportDialog", "ScopusAnalyzer - Export Statistics"))
        self.export_grpbox.setTitle(_translate("exportDialog", "Export Settings"))
        self.time_period_grpbox.setTitle(_translate("exportDialog", "Time Period"))
        self.from_lbl.setText(_translate("exportDialog", "From:"))
        self.to_lbl.setText(_translate("exportDialog", "To:"))
        self.inclusions_grpbox.setTitle(_translate("exportDialog", "Inclusions"))
        self.aggregated_data_checkbox.setText(_translate("exportDialog", "Aggregated Data"))
        self.diagrams_checkbox.setText(_translate("exportDialog", "Statistical Diagrams"))
        self.department_stats_checkbox.setText(_translate("exportDialog", "Department Statistics"))
        self.professor_stats_checkbox.setText(_translate("exportDialog", "Professor Statistics"))
        self.output_grpbox.setTitle(_translate("exportDialog", "Output File"))
        self.select_path_label.setText(_translate("exportDialog", "Select Export Path:"))
        self.path_select_toolbtn.setToolTip(_translate("exportDialog", "Select export path for Excel"))
        self.path_select_toolbtn.setText(_translate("exportDialog", "..."))
        self.export_filename_label.setText(_translate("exportDialog", "Select Excel Filename:"))
        self.cancel_command_link_btn.setText(_translate("exportDialog", "Cancel"))
        self.export_command_link_btn.setText(_translate("exportDialog", "Export"))

    def export(self):
        if not self.years_are_correct():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/favicon.ico'))
            msg.setText('Please enter valid from/to years.')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
            msg.setWindowTitle('Failed to connect')
            reply = msg.exec_()
            return

        from export.statistics import StatisticsExportation

        self.outpath = self.export_path_textedit.toPlainText() + '/' + (self.export_filename_textedit.toPlainText() 
                            if '.xlsx' in self.export_filename_textedit.toPlainText() else self.export_filename_textedit.toPlainText() + '.xlsx')
        
        stats = StatisticsExportation(from_year=self.from_year_combobox.currentText(), to_year=self.to_year_combobox.currentText(), 
                                        agg_data=self.aggregated_data_checkbox.isChecked(), stat_diagrams=self.diagrams_checkbox.isChecked(), 
                                            department_stats=self.department_stats_checkbox.isChecked(), outpath=self.outpath, professors=self.selected_professors, df=self.df)
        success = stats.write_to_excel()

        if success:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Successfully written to excel.')
            msg.setWindowTitle('Success!')
            msg.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/favicon.ico'))
            msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText('Something went wrong. Please try again.')
            msg.setWindowTitle('Error')
            msg.setWindowIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/favicon.ico'))
            msg.exec_()

    def open_professors_dialog(self):
        if self.professor_stats_checkbox.isChecked():
            from .professors_dialog import Ui_Professors_Dialog
            self.professors_dialog = QtWidgets.QDialog()
            self.professors_dialog.professors_ui = Ui_Professors_Dialog()
            self.professors_dialog.professors_ui.setupUi(Dialog=self.professors_dialog)
            self.professors_dialog.exec_()
            try:
                self.selected_professors = self.professors_dialog.professors_ui.selected_professors
            except:
                self.selected_professors = None

            if not self.selected_professors:
                self.professor_stats_checkbox.setChecked(False)
        else:
            self.professor_stats_checkbox.setChecked(False)
    def change_filename(self):
        ###### Set default export settings ######
        if self.years_are_correct():
            self.export_filename_textedit.setText(f'''STAT_EXPORT_{self.from_year_combobox.currentText()}-{self.to_year_combobox.currentText()}''' 
                                                    if self.from_year_combobox.currentText() != self.to_year_combobox.currentText() else f'''STAT_EXPORT_{self.from_year_combobox.currentText()}''')

    def years_are_correct(self):
        if int(self.from_year_combobox.currentText()) <= int(self.to_year_combobox.currentText()):
            return True
        return False

    def fetch_years_from_db(self, order='DESC'):
        import database.db as db
        return [str(year[0]) for year in db.get_distinct_years(order)]

    def open_directory_dialog(self):
        '''
        When user hits the tool button,
        a dialog appears, in order the user to choose the folder
        in which the excel will be exported after the completion of search
        '''
        from PyQt5.QtWidgets import QFileDialog
        try:
            self.dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.export_path_textedit.toPlainText(), QFileDialog.ShowDirsOnly)
        except:
            self.dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:/', QFileDialog.ShowDirsOnly)
        self.export_path_textedit.setText(self.dir_)