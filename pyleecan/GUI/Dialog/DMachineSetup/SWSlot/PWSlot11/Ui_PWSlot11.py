# -*- coding: utf-8 -*-

# File generated according to PWSlot11.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWSlot.WWSlotOut.WWSlotOut import WWSlotOut
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PWSlot11(object):
    def setupUi(self, PWSlot11):
        if not PWSlot11.objectName():
            PWSlot11.setObjectName("PWSlot11")
        PWSlot11.resize(924, 515)
        PWSlot11.setMinimumSize(QSize(630, 470))
        PWSlot11.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PWSlot11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.img_slot = QLabel(PWSlot11)
        self.img_slot.setObjectName("img_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_slot.sizePolicy().hasHeightForWidth())
        self.img_slot.setSizePolicy(sizePolicy)
        self.img_slot.setMaximumSize(QSize(16777215, 16777215))
        self.img_slot.setPixmap(
            QPixmap(":/images/images/MachineSetup/WSlot/SlotW11_wind_ext_stator.png")
        )
        self.img_slot.setScaledContents(False)
        self.img_slot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.img_slot)

        self.txt_constraint = QTextEdit(PWSlot11)
        self.txt_constraint.setObjectName("txt_constraint")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.txt_constraint.sizePolicy().hasHeightForWidth()
        )
        self.txt_constraint.setSizePolicy(sizePolicy1)
        self.txt_constraint.setMaximumSize(QSize(16777215, 100))
        self.txt_constraint.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_constraint.setUndoRedoEnabled(True)
        self.txt_constraint.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_2.addWidget(self.txt_constraint)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.scrollArea = QScrollArea(PWSlot11)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(270, 0))
        self.scrollArea.setMaximumSize(QSize(270, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 491))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.is_cst_tooth = QCheckBox(self.scrollAreaWidgetContents)
        self.is_cst_tooth.setObjectName("is_cst_tooth")

        self.verticalLayout_3.addWidget(self.is_cst_tooth)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.lf_H1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H1.setObjectName("lf_H1")

        self.gridLayout.addWidget(self.lf_H1, 5, 1, 1, 1)

        self.in_H1 = QLabel(self.scrollAreaWidgetContents)
        self.in_H1.setObjectName("in_H1")

        self.gridLayout.addWidget(self.in_H1, 5, 0, 1, 1)

        self.c_H1_unit = QComboBox(self.scrollAreaWidgetContents)
        self.c_H1_unit.setObjectName("c_H1_unit")
        self.c_H1_unit.setEditable(True)

        self.gridLayout.addWidget(self.c_H1_unit, 5, 4, 1, 1)

        self.lf_H0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H0.setObjectName("lf_H0")

        self.gridLayout.addWidget(self.lf_H0, 4, 1, 1, 1)

        self.in_W1 = QLabel(self.scrollAreaWidgetContents)
        self.in_W1.setObjectName("in_W1")

        self.gridLayout.addWidget(self.in_W1, 1, 0, 1, 1)

        self.in_W3 = QLabel(self.scrollAreaWidgetContents)
        self.in_W3.setObjectName("in_W3")

        self.gridLayout.addWidget(self.in_W3, 3, 0, 1, 1)

        self.in_H2 = QLabel(self.scrollAreaWidgetContents)
        self.in_H2.setObjectName("in_H2")

        self.gridLayout.addWidget(self.in_H2, 6, 0, 1, 1)

        self.in_W2 = QLabel(self.scrollAreaWidgetContents)
        self.in_W2.setObjectName("in_W2")

        self.gridLayout.addWidget(self.in_W2, 2, 0, 1, 1)

        self.lf_W0 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W0.setObjectName("lf_W0")

        self.gridLayout.addWidget(self.lf_W0, 0, 1, 1, 1)

        self.lf_W2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W2.setObjectName("lf_W2")

        self.gridLayout.addWidget(self.lf_W2, 2, 1, 1, 1)

        self.unit_W1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W1.setObjectName("unit_W1")

        self.gridLayout.addWidget(self.unit_W1, 1, 4, 1, 1)

        self.lf_W1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W1.setObjectName("lf_W1")

        self.gridLayout.addWidget(self.lf_W1, 1, 1, 1, 1)

        self.in_H0 = QLabel(self.scrollAreaWidgetContents)
        self.in_H0.setObjectName("in_H0")

        self.gridLayout.addWidget(self.in_H0, 4, 0, 1, 1)

        self.unit_H2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H2.setObjectName("unit_H2")

        self.gridLayout.addWidget(self.unit_H2, 6, 4, 1, 1)

        self.in_W0 = QLabel(self.scrollAreaWidgetContents)
        self.in_W0.setObjectName("in_W0")

        self.gridLayout.addWidget(self.in_W0, 0, 0, 1, 1)

        self.lf_W3 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_W3.setObjectName("lf_W3")

        self.gridLayout.addWidget(self.lf_W3, 3, 1, 1, 1)

        self.unit_W0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W0.setObjectName("unit_W0")

        self.gridLayout.addWidget(self.unit_W0, 0, 4, 1, 1)

        self.unit_W2 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W2.setObjectName("unit_W2")

        self.gridLayout.addWidget(self.unit_W2, 2, 4, 1, 1)

        self.unit_H0 = QLabel(self.scrollAreaWidgetContents)
        self.unit_H0.setObjectName("unit_H0")

        self.gridLayout.addWidget(self.unit_H0, 4, 4, 1, 1)

        self.lf_H2 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_H2.setObjectName("lf_H2")

        self.gridLayout.addWidget(self.lf_H2, 6, 1, 1, 1)

        self.unit_W3 = QLabel(self.scrollAreaWidgetContents)
        self.unit_W3.setObjectName("unit_W3")

        self.gridLayout.addWidget(self.unit_W3, 3, 4, 1, 1)

        self.in_R1 = QLabel(self.scrollAreaWidgetContents)
        self.in_R1.setObjectName("in_R1")

        self.gridLayout.addWidget(self.in_R1, 7, 0, 1, 1)

        self.lf_R1 = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_R1.setObjectName("lf_R1")

        self.gridLayout.addWidget(self.lf_R1, 7, 1, 1, 1)

        self.unit_R1 = QLabel(self.scrollAreaWidgetContents)
        self.unit_R1.setObjectName("unit_R1")

        self.gridLayout.addWidget(self.unit_R1, 7, 4, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.g_wedge = QGroupBox(self.scrollAreaWidgetContents)
        self.g_wedge.setObjectName("g_wedge")
        self.g_wedge.setCheckable(True)
        self.g_wedge.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.g_wedge)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_wedge_mat = WMatSelectV(self.g_wedge)
        self.w_wedge_mat.setObjectName("w_wedge_mat")
        self.w_wedge_mat.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.w_wedge_mat)

        self.verticalLayout_3.addWidget(self.g_wedge)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.w_out = WWSlotOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout_3.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.lf_W0, self.lf_W1)
        QWidget.setTabOrder(self.lf_W1, self.lf_W2)
        QWidget.setTabOrder(self.lf_W2, self.lf_W3)
        QWidget.setTabOrder(self.lf_W3, self.lf_H0)
        QWidget.setTabOrder(self.lf_H0, self.lf_H1)
        QWidget.setTabOrder(self.lf_H1, self.lf_H2)
        QWidget.setTabOrder(self.lf_H2, self.lf_R1)
        QWidget.setTabOrder(self.lf_R1, self.g_wedge)
        QWidget.setTabOrder(self.g_wedge, self.c_H1_unit)
        QWidget.setTabOrder(self.c_H1_unit, self.is_cst_tooth)
        QWidget.setTabOrder(self.is_cst_tooth, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.txt_constraint)

        self.retranslateUi(PWSlot11)

        QMetaObject.connectSlotsByName(PWSlot11)

    # setupUi

    def retranslateUi(self, PWSlot11):
        PWSlot11.setWindowTitle(QCoreApplication.translate("PWSlot11", "Form", None))
        self.img_slot.setText("")
        self.txt_constraint.setHtml(
            QCoreApplication.translate(
                "PWSlot11",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'DejaVu Sans'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:600; text-decoration: underline;">Constraints :</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">2 \u00d7 R1 \u2264 W2</span></p>\n'
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">W0 \u2264 W1</span></p>\n'
                '<p align="center" style=" m'
                'argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'DejaVu Sans\'; font-size:10pt;">R1 \u2264 H2</span></p></body></html>',
                None,
            )
        )
        self.is_cst_tooth.setText(
            QCoreApplication.translate("PWSlot11", "Constant Tooth Width", None)
        )
        self.in_H1.setText(QCoreApplication.translate("PWSlot11", "H1", None))
        self.c_H1_unit.setCurrentText(
            QCoreApplication.translate("PWSlot11", "[m]", None)
        )
        self.in_W1.setText(QCoreApplication.translate("PWSlot11", "W1", None))
        self.in_W3.setText(QCoreApplication.translate("PWSlot11", "W3", None))
        self.in_H2.setText(QCoreApplication.translate("PWSlot11", "H2", None))
        self.in_W2.setText(QCoreApplication.translate("PWSlot11", "W2", None))
        self.unit_W1.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.in_H0.setText(QCoreApplication.translate("PWSlot11", "H0", None))
        self.unit_H2.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.in_W0.setText(QCoreApplication.translate("PWSlot11", "W0", None))
        self.unit_W0.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.unit_W2.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.unit_H0.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.unit_W3.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.in_R1.setText(QCoreApplication.translate("PWSlot11", "R1", None))
        self.unit_R1.setText(QCoreApplication.translate("PWSlot11", "m", None))
        self.g_wedge.setTitle(QCoreApplication.translate("PWSlot11", "Wedge", None))

    # retranslateUi
