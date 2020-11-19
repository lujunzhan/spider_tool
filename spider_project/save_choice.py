# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_choice.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

""" 这个是QT5图形界面直接生成的代码 """
class Ui_export_form(object):
    def setupUi(self, export_form):
        export_form.setObjectName("export_form")
        export_form.resize(418, 294)
        self.save_form_2 = QtWidgets.QGroupBox(export_form)
        self.save_form_2.setGeometry(QtCore.QRect(20, 20, 391, 261))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.save_form_2.setFont(font)
        self.save_form_2.setObjectName("save_form_2")
        self.cancel_btn = QtWidgets.QPushButton(self.save_form_2)
        self.cancel_btn.setGeometry(QtCore.QRect(200, 200, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.ok_btn = QtWidgets.QPushButton(self.save_form_2)
        self.ok_btn.setGeometry(QtCore.QRect(80, 200, 93, 28))
        self.ok_btn.setObjectName("ok_btn")
        self.save_txt = QtWidgets.QRadioButton(self.save_form_2)
        self.save_txt.setGeometry(QtCore.QRect(70, 60, 115, 19))
        self.save_txt.setObjectName("save_txt")
        self.save_csv = QtWidgets.QRadioButton(self.save_form_2)
        self.save_csv.setGeometry(QtCore.QRect(220, 60, 115, 19))
        self.save_csv.setObjectName("save_csv")
        self.save_excel = QtWidgets.QRadioButton(self.save_form_2)
        self.save_excel.setGeometry(QtCore.QRect(70, 100, 115, 19))
        self.save_excel.setObjectName("save_excel")
        self.save_json = QtWidgets.QRadioButton(self.save_form_2)
        self.save_json.setGeometry(QtCore.QRect(220, 100, 115, 19))
        self.save_json.setObjectName("save_json")
        self.dir_show = QtWidgets.QLineEdit(self.save_form_2)
        self.dir_show.setGeometry(QtCore.QRect(30, 150, 251, 27))
        self.dir_show.setObjectName("dir_show")
        self.choose_dir = QtWidgets.QPushButton(self.save_form_2)
        self.choose_dir.setGeometry(QtCore.QRect(280, 150, 81, 27))
        self.choose_dir.setObjectName("choose_dir")

        self.retranslateUi(export_form)
        QtCore.QMetaObject.connectSlotsByName(export_form)

    def retranslateUi(self, export_form):
        _translate = QtCore.QCoreApplication.translate
        export_form.setWindowTitle(_translate("export_form", "Dialog"))
        self.save_form_2.setTitle(_translate("export_form", "设置保存格式"))
        self.cancel_btn.setText(_translate("export_form", "取消"))
        self.ok_btn.setText(_translate("export_form", "保存"))
        self.save_txt.setText(_translate("export_form", ".txt"))
        self.save_csv.setText(_translate("export_form", ".csv"))
        self.save_excel.setText(_translate("export_form", ".excel"))
        self.save_json.setText(_translate("export_form", ".json"))
        self.choose_dir.setText(_translate("export_form", "选择目录"))
