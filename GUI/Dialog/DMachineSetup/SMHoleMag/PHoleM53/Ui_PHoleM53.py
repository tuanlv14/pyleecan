# -*- coding: utf-8 -*-

# File generated according to PHoleM53.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PHoleM53(object):
    def setupUi(self, PHoleM53):
        PHoleM53.setObjectName("PHoleM53")
        PHoleM53.resize(740, 440)
        PHoleM53.setMinimumSize(QtCore.QSize(740, 440))
        PHoleM53.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(PHoleM53)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.img_slot = QtWidgets.QLabel(PHoleM53)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMinimumSize(QtCore.QSize(500, 191))
        self.img_slot.setMaximumSize(QtCore.QSize(500, 191))
        self.img_slot.setText("")
        self.img_slot.setPixmap(
            QtGui.QPixmap(":/images/images/MachineSetup/WSlot/Slot_53.PNG")
        )
        self.img_slot.setScaledContents(True)
        self.img_slot.setObjectName("img_slot")
        self.verticalLayout_3.addWidget(self.img_slot)
        self.txt_constraint = QtWidgets.QTextEdit(PHoleM53)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy)
        self.txt_constraint.setMinimumSize(QtCore.QSize(200, 0))
        self.txt_constraint.setMaximumSize(QtCore.QSize(16777215, 100))
        self.txt_constraint.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse
        )
        self.txt_constraint.setObjectName("txt_constraint")
        self.verticalLayout_3.addWidget(self.txt_constraint)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_H0 = QtWidgets.QLabel(PHoleM53)
        self.in_H0.setObjectName("in_H0")
        self.gridLayout.addWidget(self.in_H0, 0, 0, 1, 1)
        self.lf_H0 = FloatEdit(PHoleM53)
        self.lf_H0.setObjectName("lf_H0")
        self.gridLayout.addWidget(self.lf_H0, 0, 1, 1, 1)
        self.unit_H0 = QtWidgets.QLabel(PHoleM53)
        self.unit_H0.setObjectName("unit_H0")
        self.gridLayout.addWidget(self.unit_H0, 0, 2, 1, 1)
        self.in_H1 = QtWidgets.QLabel(PHoleM53)
        self.in_H1.setObjectName("in_H1")
        self.gridLayout.addWidget(self.in_H1, 1, 0, 1, 1)
        self.lf_H1 = FloatEdit(PHoleM53)
        self.lf_H1.setObjectName("lf_H1")
        self.gridLayout.addWidget(self.lf_H1, 1, 1, 1, 1)
        self.unit_H1 = QtWidgets.QLabel(PHoleM53)
        self.unit_H1.setObjectName("unit_H1")
        self.gridLayout.addWidget(self.unit_H1, 1, 2, 1, 1)
        self.in_H2 = QtWidgets.QLabel(PHoleM53)
        self.in_H2.setObjectName("in_H2")
        self.gridLayout.addWidget(self.in_H2, 2, 0, 1, 1)
        self.lf_H2 = FloatEdit(PHoleM53)
        self.lf_H2.setObjectName("lf_H2")
        self.gridLayout.addWidget(self.lf_H2, 2, 1, 1, 1)
        self.unit_H2 = QtWidgets.QLabel(PHoleM53)
        self.unit_H2.setObjectName("unit_H2")
        self.gridLayout.addWidget(self.unit_H2, 2, 2, 1, 1)
        self.in_H3 = QtWidgets.QLabel(PHoleM53)
        self.in_H3.setObjectName("in_H3")
        self.gridLayout.addWidget(self.in_H3, 3, 0, 1, 1)
        self.lf_H3 = FloatEdit(PHoleM53)
        self.lf_H3.setObjectName("lf_H3")
        self.gridLayout.addWidget(self.lf_H3, 3, 1, 1, 1)
        self.unit_H3 = QtWidgets.QLabel(PHoleM53)
        self.unit_H3.setObjectName("unit_H3")
        self.gridLayout.addWidget(self.unit_H3, 3, 2, 1, 1)
        self.in_W1 = QtWidgets.QLabel(PHoleM53)
        self.in_W1.setObjectName("in_W1")
        self.gridLayout.addWidget(self.in_W1, 4, 0, 1, 1)
        self.lf_W1 = FloatEdit(PHoleM53)
        self.lf_W1.setObjectName("lf_W1")
        self.gridLayout.addWidget(self.lf_W1, 4, 1, 1, 1)
        self.unit_W1 = QtWidgets.QLabel(PHoleM53)
        self.unit_W1.setObjectName("unit_W1")
        self.gridLayout.addWidget(self.unit_W1, 4, 2, 1, 1)
        self.in_W2 = QtWidgets.QLabel(PHoleM53)
        self.in_W2.setObjectName("in_W2")
        self.gridLayout.addWidget(self.in_W2, 5, 0, 1, 1)
        self.lf_W2 = FloatEdit(PHoleM53)
        self.lf_W2.setObjectName("lf_W2")
        self.gridLayout.addWidget(self.lf_W2, 5, 1, 1, 1)
        self.unit_W2 = QtWidgets.QLabel(PHoleM53)
        self.unit_W2.setObjectName("unit_W2")
        self.gridLayout.addWidget(self.unit_W2, 5, 2, 1, 1)
        self.in_W3 = QtWidgets.QLabel(PHoleM53)
        self.in_W3.setObjectName("in_W3")
        self.gridLayout.addWidget(self.in_W3, 6, 0, 1, 1)
        self.lf_W3 = FloatEdit(PHoleM53)
        self.lf_W3.setObjectName("lf_W3")
        self.gridLayout.addWidget(self.lf_W3, 6, 1, 1, 1)
        self.unit_W3 = QtWidgets.QLabel(PHoleM53)
        self.unit_W3.setObjectName("unit_W3")
        self.gridLayout.addWidget(self.unit_W3, 6, 2, 1, 1)
        self.in_W4 = QtWidgets.QLabel(PHoleM53)
        self.in_W4.setObjectName("in_W4")
        self.gridLayout.addWidget(self.in_W4, 7, 0, 1, 1)
        self.lf_W4 = FloatEdit(PHoleM53)
        self.lf_W4.setText("")
        self.lf_W4.setObjectName("lf_W4")
        self.gridLayout.addWidget(self.lf_W4, 7, 1, 1, 1)
        self.unit_W4 = QtWidgets.QLabel(PHoleM53)
        self.unit_W4.setObjectName("unit_W4")
        self.gridLayout.addWidget(self.unit_W4, 7, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.g_output = QtWidgets.QGroupBox(PHoleM53)
        self.g_output.setMinimumSize(QtCore.QSize(200, 0))
        self.g_output.setObjectName("g_output")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.g_output)
        self.verticalLayout.setObjectName("verticalLayout")
        self.out_slot_surface = QtWidgets.QLabel(self.g_output)
        self.out_slot_surface.setObjectName("out_slot_surface")
        self.verticalLayout.addWidget(self.out_slot_surface)
        self.out_magnet_surface = QtWidgets.QLabel(self.g_output)
        self.out_magnet_surface.setObjectName("out_magnet_surface")
        self.verticalLayout.addWidget(self.out_magnet_surface)
        self.out_W5 = QtWidgets.QLabel(self.g_output)
        self.out_W5.setObjectName("out_W5")
        self.verticalLayout.addWidget(self.out_W5)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.g_output)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(PHoleM53)
        QtCore.QMetaObject.connectSlotsByName(PHoleM53)
        PHoleM53.setTabOrder(self.lf_H0, self.lf_H1)
        PHoleM53.setTabOrder(self.lf_H1, self.lf_H2)
        PHoleM53.setTabOrder(self.lf_H2, self.lf_H3)
        PHoleM53.setTabOrder(self.lf_H3, self.lf_W1)
        PHoleM53.setTabOrder(self.lf_W1, self.lf_W2)
        PHoleM53.setTabOrder(self.lf_W2, self.lf_W3)
        PHoleM53.setTabOrder(self.lf_W3, self.lf_W4)
        PHoleM53.setTabOrder(self.lf_W4, self.txt_constraint)

    def retranslateUi(self, PHoleM53):
        _translate = QtCore.QCoreApplication.translate
        PHoleM53.setWindowTitle(_translate("PHoleM53", "Form"))
        self.txt_constraint.setHtml(
            _translate(
                "PHoleM53",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">H2 &lt; H3</span></p></body></html>',
            )
        )
        self.in_H0.setText(_translate("PHoleM53", "H0 :"))
        self.unit_H0.setText(_translate("PHoleM53", "m"))
        self.in_H1.setText(_translate("PHoleM53", "H1 :"))
        self.unit_H1.setText(_translate("PHoleM53", "m"))
        self.in_H2.setText(_translate("PHoleM53", "H2 :"))
        self.unit_H2.setText(_translate("PHoleM53", "m"))
        self.in_H3.setText(_translate("PHoleM53", "H3 :"))
        self.unit_H3.setText(_translate("PHoleM53", "m"))
        self.in_W1.setText(_translate("PHoleM53", "W1 :"))
        self.unit_W1.setText(_translate("PHoleM53", "m"))
        self.in_W2.setText(_translate("PHoleM53", "W2 :"))
        self.unit_W2.setText(_translate("PHoleM53", "m"))
        self.in_W3.setText(_translate("PHoleM53", "W3 :"))
        self.unit_W3.setText(_translate("PHoleM53", "m"))
        self.in_W4.setText(_translate("PHoleM53", "W4 :"))
        self.unit_W4.setText(_translate("PHoleM53", "rad"))
        self.g_output.setTitle(_translate("PHoleM53", "Output"))
        self.out_slot_surface.setText(
            _translate("PHoleM53", "Slot suface (2 part) : ?")
        )
        self.out_magnet_surface.setText(
            _translate("PHoleM53", "Single Magnet surface : ?")
        )
        self.out_W5.setText(_translate("PHoleM53", "W5 : ?"))


from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
