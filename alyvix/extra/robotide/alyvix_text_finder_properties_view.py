# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alyvix_text_finder_properties_view.ui'
#
# Created: Sat Apr 25 23:03:41 2015
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(560, 326)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(9, 10, 543, 307))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_design = QtGui.QWidget()
        self.tab_design.setObjectName(_fromUtf8("tab_design"))
        self.widget = QtGui.QWidget(self.tab_design)
        self.widget.setGeometry(QtCore.QRect(149, 9, 381, 268))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 380, 263))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_10 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout.addWidget(self.line_10, 7, 0, 1, 4)
        self.text_label = QtGui.QLabel(self.gridLayoutWidget)
        self.text_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_label.setObjectName(_fromUtf8("text_label"))
        self.gridLayout.addWidget(self.text_label, 2, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 4)
        self.timeout_label = QtGui.QLabel(self.gridLayoutWidget)
        self.timeout_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeout_label.setObjectName(_fromUtf8("timeout_label"))
        self.gridLayout.addWidget(self.timeout_label, 6, 2, 1, 1)
        self.dontclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.dontclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio.setChecked(True)
        self.dontclickRadio.setObjectName(_fromUtf8("dontclickRadio"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.dontclickRadio)
        self.gridLayout.addWidget(self.dontclickRadio, 8, 3, 1, 1)
        self.lineEditText = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditText.setObjectName(_fromUtf8("lineEditText"))
        self.gridLayout.addWidget(self.lineEditText, 2, 1, 1, 2)
        self.doubleclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.doubleclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.doubleclickRadio.setObjectName(_fromUtf8("doubleclickRadio"))
        self.buttonGroup_2.addButton(self.doubleclickRadio)
        self.gridLayout.addWidget(self.doubleclickRadio, 8, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.lineEditLang = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditLang.setObjectName(_fromUtf8("lineEditLang"))
        self.gridLayout.addWidget(self.lineEditLang, 3, 1, 1, 1)
        self.find_radio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.find_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.find_radio.setObjectName(_fromUtf8("find_radio"))
        self.buttonGroup_5 = QtGui.QButtonGroup(Form)
        self.buttonGroup_5.setObjectName(_fromUtf8("buttonGroup_5"))
        self.buttonGroup_5.addButton(self.find_radio)
        self.gridLayout.addWidget(self.find_radio, 6, 0, 1, 1)
        self.wait_radio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.wait_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wait_radio.setChecked(True)
        self.wait_radio.setObjectName(_fromUtf8("wait_radio"))
        self.buttonGroup_5.addButton(self.wait_radio)
        self.gridLayout.addWidget(self.wait_radio, 6, 1, 1, 1)
        self.clickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.clickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio.setObjectName(_fromUtf8("clickRadio"))
        self.buttonGroup_2.addButton(self.clickRadio)
        self.gridLayout.addWidget(self.clickRadio, 8, 0, 1, 2)
        self.line_8 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 5, 0, 1, 4)
        self.lang_label = QtGui.QLabel(self.gridLayoutWidget)
        self.lang_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lang_label.setObjectName(_fromUtf8("lang_label"))
        self.gridLayout.addWidget(self.lang_label, 3, 0, 1, 1)
        self.timeout_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.timeout_spinbox.setMaximum(999999)
        self.timeout_spinbox.setObjectName(_fromUtf8("timeout_spinbox"))
        self.gridLayout.addWidget(self.timeout_spinbox, 6, 3, 1, 1)
        self.namelineedit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.namelineedit.setObjectName(_fromUtf8("namelineedit"))
        self.gridLayout.addWidget(self.namelineedit, 0, 0, 1, 4)
        self.pushButtonCheck = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonCheck.setObjectName(_fromUtf8("pushButtonCheck"))
        self.gridLayout.addWidget(self.pushButtonCheck, 2, 3, 1, 1)
        self.lineEditWhiteList = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditWhiteList.setObjectName(_fromUtf8("lineEditWhiteList"))
        self.gridLayout.addWidget(self.lineEditWhiteList, 4, 1, 1, 3)
        self.inserttext = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.inserttext.setObjectName(_fromUtf8("inserttext"))
        self.gridLayout.addWidget(self.inserttext, 9, 0, 1, 4)
        self.listWidget = QtGui.QListWidget(self.tab_design)
        self.listWidget.setGeometry(QtCore.QRect(8, 9, 131, 263))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        self.widget_2 = QtGui.QWidget(self.tab_design)
        self.widget_2.setGeometry(QtCore.QRect(150, 380, 381, 272))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.widget_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 380, 266))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEditLang_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditLang_2.setObjectName(_fromUtf8("lineEditLang_2"))
        self.gridLayout_2.addWidget(self.lineEditLang_2, 2, 1, 1, 1)
        self.roi_y_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_y_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_y_label.setObjectName(_fromUtf8("roi_y_label"))
        self.gridLayout_2.addWidget(self.roi_y_label, 5, 2, 1, 1)
        self.roi_height_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_height_label.setObjectName(_fromUtf8("roi_height_label"))
        self.gridLayout_2.addWidget(self.roi_height_label, 6, 2, 1, 1)
        self.doubleclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.doubleclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.doubleclickRadio_2.setObjectName(_fromUtf8("doubleclickRadio_2"))
        self.buttonGroup_4 = QtGui.QButtonGroup(Form)
        self.buttonGroup_4.setObjectName(_fromUtf8("buttonGroup_4"))
        self.buttonGroup_4.addButton(self.doubleclickRadio_2)
        self.gridLayout_2.addWidget(self.doubleclickRadio_2, 8, 2, 1, 1)
        self.clickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.clickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio_2.setObjectName(_fromUtf8("clickRadio_2"))
        self.buttonGroup_4.addButton(self.clickRadio_2)
        self.gridLayout_2.addWidget(self.clickRadio_2, 8, 0, 1, 2)
        self.pushButtonCheck_2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonCheck_2.setObjectName(_fromUtf8("pushButtonCheck_2"))
        self.gridLayout_2.addWidget(self.pushButtonCheck_2, 1, 3, 1, 1)
        self.roi_x_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_x_label.setObjectName(_fromUtf8("roi_x_label"))
        self.gridLayout_2.addWidget(self.roi_x_label, 5, 0, 1, 1)
        self.text_label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.text_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_label_2.setObjectName(_fromUtf8("text_label_2"))
        self.gridLayout_2.addWidget(self.text_label_2, 1, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 4, 0, 1, 4)
        self.roi_width_label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.roi_width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_width_label.setObjectName(_fromUtf8("roi_width_label"))
        self.gridLayout_2.addWidget(self.roi_width_label, 6, 0, 1, 1)
        self.roi_width_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_width_spinbox.setMaximum(9999)
        self.roi_width_spinbox.setObjectName(_fromUtf8("roi_width_spinbox"))
        self.gridLayout_2.addWidget(self.roi_width_spinbox, 6, 1, 1, 1)
        self.lang_label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lang_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lang_label_2.setObjectName(_fromUtf8("lang_label_2"))
        self.gridLayout_2.addWidget(self.lang_label_2, 2, 0, 1, 1)
        self.roi_y_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_y_spinbox.setMinimum(-9999)
        self.roi_y_spinbox.setMaximum(9999)
        self.roi_y_spinbox.setObjectName(_fromUtf8("roi_y_spinbox"))
        self.gridLayout_2.addWidget(self.roi_y_spinbox, 5, 3, 1, 1)
        self.roi_x_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_x_spinbox.setMinimum(-9999)
        self.roi_x_spinbox.setMaximum(9999)
        self.roi_x_spinbox.setObjectName(_fromUtf8("roi_x_spinbox"))
        self.gridLayout_2.addWidget(self.roi_x_spinbox, 5, 1, 1, 1)
        self.roi_height_spinbox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.roi_height_spinbox.setMaximum(9999)
        self.roi_height_spinbox.setObjectName(_fromUtf8("roi_height_spinbox"))
        self.gridLayout_2.addWidget(self.roi_height_spinbox, 6, 3, 1, 1)
        self.lineEditText_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditText_2.setObjectName(_fromUtf8("lineEditText_2"))
        self.gridLayout_2.addWidget(self.lineEditText_2, 1, 1, 1, 2)
        self.line_7 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_2.addWidget(self.line_7, 0, 0, 1, 4)
        self.dontclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.dontclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio_2.setChecked(True)
        self.dontclickRadio_2.setObjectName(_fromUtf8("dontclickRadio_2"))
        self.buttonGroup_4.addButton(self.dontclickRadio_2)
        self.gridLayout_2.addWidget(self.dontclickRadio_2, 8, 3, 1, 1)
        self.line_9 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout_2.addWidget(self.line_9, 7, 0, 1, 4)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEditWhiteList_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditWhiteList_2.setObjectName(_fromUtf8("lineEditWhiteList_2"))
        self.gridLayout_2.addWidget(self.lineEditWhiteList_2, 3, 1, 1, 3)
        self.inserttext_2 = QtGui.QPlainTextEdit(self.gridLayoutWidget_2)
        self.inserttext_2.setObjectName(_fromUtf8("inserttext_2"))
        self.gridLayout_2.addWidget(self.inserttext_2, 9, 0, 1, 4)
        self.tabWidget.addTab(self.tab_design, _fromUtf8(""))
        self.tab_code = QtGui.QWidget()
        self.tab_code.setObjectName(_fromUtf8("tab_code"))
        self.spinBoxArgs = QtGui.QSpinBox(self.tab_code)
        self.spinBoxArgs.setGeometry(QtCore.QRect(68, 245, 60, 22))
        self.spinBoxArgs.setObjectName(_fromUtf8("spinBoxArgs"))
        self.labelArgs = QtGui.QLabel(self.tab_code)
        self.labelArgs.setGeometry(QtCore.QRect(10, 250, 46, 13))
        self.labelArgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelArgs.setObjectName(_fromUtf8("labelArgs"))
        self.tabWidget.addTab(self.tab_code, _fromUtf8(""))
        self.tab_customlines = QtGui.QWidget()
        self.tab_customlines.setObjectName(_fromUtf8("tab_customlines"))
        self.listWidgetBlocks = QtGui.QListWidget(self.tab_customlines)
        self.listWidgetBlocks.setGeometry(QtCore.QRect(448, 9, 81, 261))
        self.listWidgetBlocks.setObjectName(_fromUtf8("listWidgetBlocks"))
        self.textEditCustomLines = QtGui.QTextEdit(self.tab_customlines)
        self.textEditCustomLines.setGeometry(QtCore.QRect(8, 9, 431, 221))
        self.textEditCustomLines.setTabStopWidth(80)
        self.textEditCustomLines.setAcceptRichText(False)
        self.textEditCustomLines.setObjectName(_fromUtf8("textEditCustomLines"))
        self.pushButtonAddBlock = QtGui.QPushButton(self.tab_customlines)
        self.pushButtonAddBlock.setGeometry(QtCore.QRect(260, 243, 71, 23))
        self.pushButtonAddBlock.setObjectName(_fromUtf8("pushButtonAddBlock"))
        self.spinBoxLine = QtGui.QSpinBox(self.tab_customlines)
        self.spinBoxLine.setGeometry(QtCore.QRect(130, 243, 121, 22))
        self.spinBoxLine.setMinimum(1)
        self.spinBoxLine.setMaximum(99999)
        self.spinBoxLine.setObjectName(_fromUtf8("spinBoxLine"))
        self.label_line = QtGui.QLabel(self.tab_customlines)
        self.label_line.setGeometry(QtCore.QRect(59, 244, 61, 21))
        self.label_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_line.setObjectName(_fromUtf8("label_line"))
        self.pushButtonRemoveBlock = QtGui.QPushButton(self.tab_customlines)
        self.pushButtonRemoveBlock.setGeometry(QtCore.QRect(340, 243, 91, 23))
        self.pushButtonRemoveBlock.setObjectName(_fromUtf8("pushButtonRemoveBlock"))
        self.tabWidget.addTab(self.tab_customlines, _fromUtf8(""))
        self.tab_perfdata = QtGui.QWidget()
        self.tab_perfdata.setObjectName(_fromUtf8("tab_perfdata"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tab_perfdata)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(19, 30, 497, 22))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBoxEnablePerformance = QtGui.QCheckBox(self.gridLayoutWidget_3)
        self.checkBoxEnablePerformance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxEnablePerformance.setChecked(True)
        self.checkBoxEnablePerformance.setObjectName(_fromUtf8("checkBoxEnablePerformance"))
        self.gridLayout_3.addWidget(self.checkBoxEnablePerformance, 0, 0, 1, 1)
        self.labelCritical = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelCritical.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCritical.setObjectName(_fromUtf8("labelCritical"))
        self.gridLayout_3.addWidget(self.labelCritical, 0, 3, 1, 1)
        self.doubleSpinBoxWarning = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBoxWarning.setMaximum(9999.99)
        self.doubleSpinBoxWarning.setSingleStep(0.05)
        self.doubleSpinBoxWarning.setObjectName(_fromUtf8("doubleSpinBoxWarning"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxWarning, 0, 2, 1, 1)
        self.labelWarning = QtGui.QLabel(self.gridLayoutWidget_3)
        self.labelWarning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelWarning.setObjectName(_fromUtf8("labelWarning"))
        self.gridLayout_3.addWidget(self.labelWarning, 0, 1, 1, 1)
        self.doubleSpinBoxCritical = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBoxCritical.setMaximum(9999.99)
        self.doubleSpinBoxCritical.setSingleStep(0.05)
        self.doubleSpinBoxCritical.setObjectName(_fromUtf8("doubleSpinBoxCritical"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxCritical, 0, 4, 1, 1)
        self.tabWidget.addTab(self.tab_perfdata, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.text_label.setText(_translate("Form", "Text", None))
        self.timeout_label.setText(_translate("Form", "Timeout", None))
        self.dontclickRadio.setText(_translate("Form", "Don\'t Click", None))
        self.lineEditText.setText(_translate("Form", "Type here the Text to find", None))
        self.doubleclickRadio.setText(_translate("Form", "Double Click", None))
        self.label.setText(_translate("Form", "WhiteList", None))
        self.find_radio.setText(_translate("Form", "Find", None))
        self.wait_radio.setText(_translate("Form", "Wait", None))
        self.clickRadio.setText(_translate("Form", "Click", None))
        self.lang_label.setText(_translate("Form", "Lang", None))
        self.namelineedit.setText(_translate("Form", "Type here the name of the object", None))
        self.pushButtonCheck.setText(_translate("Form", "Check", None))
        self.inserttext.setPlainText(_translate("Form", "Type here the Keyboard macro", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "main_text", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.roi_y_label.setText(_translate("Form", "Roi Y", None))
        self.roi_height_label.setText(_translate("Form", "Roi Height", None))
        self.doubleclickRadio_2.setText(_translate("Form", "Double Click", None))
        self.clickRadio_2.setText(_translate("Form", "Click", None))
        self.pushButtonCheck_2.setText(_translate("Form", "Check", None))
        self.roi_x_label.setText(_translate("Form", "Roi X", None))
        self.text_label_2.setText(_translate("Form", "Text", None))
        self.roi_width_label.setText(_translate("Form", "Roi Width", None))
        self.lang_label_2.setText(_translate("Form", "Lang", None))
        self.lineEditText_2.setText(_translate("Form", "Type here the Text to find", None))
        self.dontclickRadio_2.setText(_translate("Form", "Don\'t Click", None))
        self.label_2.setText(_translate("Form", "WhiteList", None))
        self.inserttext_2.setPlainText(_translate("Form", "Type here the Keyboard macro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_design), _translate("Form", "Graphic Design", None))
        self.labelArgs.setText(_translate("Form", "Args", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_code), _translate("Form", "Source Code", None))
        self.pushButtonAddBlock.setText(_translate("Form", "Add Block", None))
        self.label_line.setText(_translate("Form", "Begin Line", None))
        self.pushButtonRemoveBlock.setText(_translate("Form", "Remove Block", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_customlines), _translate("Form", "Custom Lines", None))
        self.checkBoxEnablePerformance.setText(_translate("Form", "Enable Performance", None))
        self.labelCritical.setText(_translate("Form", "Critical", None))
        self.labelWarning.setText(_translate("Form", "Warning", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_perfdata), _translate("Form", "Performance Data", None))

