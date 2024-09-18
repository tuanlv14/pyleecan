# -*- coding: utf-8 -*-

# File generated according to SWSlot.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from pyleecan.GUI.Tools.HelpButton import HelpButton

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_SWSlot(object):
    def setupUi(self, SWSlot):
        if not SWSlot.objectName():
            SWSlot.setObjectName("SWSlot")
        SWSlot.resize(650, 550)
        SWSlot.setMinimumSize(QSize(650, 550))
        self.main_layout = QVBoxLayout(SWSlot)
        self.main_layout.setObjectName("main_layout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_help = HelpButton(SWSlot)
        self.b_help.setObjectName("b_help")
        self.b_help.setPixmap(QPixmap(":/images/images/icon/help_16.png"))

        self.horizontalLayout_2.addWidget(self.b_help)

        self.c_slot_type = QComboBox(SWSlot)
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.addItem("")
        self.c_slot_type.setObjectName("c_slot_type")

        self.horizontalLayout_2.addWidget(self.c_slot_type)

        self.in_Zs = QLabel(SWSlot)
        self.in_Zs.setObjectName("in_Zs")

        self.horizontalLayout_2.addWidget(self.in_Zs)

        self.si_Zs = QSpinBox(SWSlot)
        self.si_Zs.setObjectName("si_Zs")
        self.si_Zs.setMaximum(20)

        self.horizontalLayout_2.addWidget(self.si_Zs)

        self.out_Slot_pitch = QLabel(SWSlot)
        self.out_Slot_pitch.setObjectName("out_Slot_pitch")

        self.horizontalLayout_2.addWidget(self.out_Slot_pitch)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.main_layout.addLayout(self.horizontalLayout_2)

        self.w_slot = QWidget(SWSlot)
        self.w_slot.setObjectName("w_slot")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_slot.sizePolicy().hasHeightForWidth())
        self.w_slot.setSizePolicy(sizePolicy)

        self.main_layout.addWidget(self.w_slot)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_plot = QPushButton(SWSlot)
        self.b_plot.setObjectName("b_plot")

        self.horizontalLayout.addWidget(self.b_plot)

        self.b_previous = QPushButton(SWSlot)
        self.b_previous.setObjectName("b_previous")

        self.horizontalLayout.addWidget(self.b_previous)

        self.b_next = QPushButton(SWSlot)
        self.b_next.setObjectName("b_next")

        self.horizontalLayout.addWidget(self.b_next)

        self.main_layout.addLayout(self.horizontalLayout)

        self.retranslateUi(SWSlot)

        QMetaObject.connectSlotsByName(SWSlot)

    # setupUi

    def retranslateUi(self, SWSlot):
        SWSlot.setWindowTitle(QCoreApplication.translate("SWSlot", "Form", None))
        self.b_help.setText("")
        self.c_slot_type.setItemText(
            0, QCoreApplication.translate("SWSlot", "Slot Type 10", None)
        )
        self.c_slot_type.setItemText(
            1, QCoreApplication.translate("SWSlot", "Slot Type 11", None)
        )
        self.c_slot_type.setItemText(
            2, QCoreApplication.translate("SWSlot", "Slot Type 12", None)
        )

        self.in_Zs.setText(QCoreApplication.translate("SWSlot", "Zs :", None))
        self.out_Slot_pitch.setText(
            QCoreApplication.translate("SWSlot", "Slot pitch = 2*Pi / Zs = ", None)
        )
        self.b_plot.setText(QCoreApplication.translate("SWSlot", "Preview", None))
        self.b_previous.setText(QCoreApplication.translate("SWSlot", "Previous", None))
        self.b_next.setText(QCoreApplication.translate("SWSlot", "Next", None))

    # retranslateUi
