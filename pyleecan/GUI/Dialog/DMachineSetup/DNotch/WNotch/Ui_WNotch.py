# -*- coding: utf-8 -*-

# File generated according to WNotch.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit


class Ui_WNotch(object):
    def setupUi(self, WNotch):
        if not WNotch.objectName():
            WNotch.setObjectName(u"WNotch")
        WNotch.resize(760, 490)
        WNotch.setMinimumSize(QSize(760, 490))
        self.main_layout = QVBoxLayout(WNotch)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.c_notch_type = QComboBox(WNotch)
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.addItem("")
        self.c_notch_type.setObjectName(u"c_notch_type")

        self.horizontalLayout.addWidget(self.c_notch_type)

        self.in_Zs = QLabel(WNotch)
        self.in_Zs.setObjectName(u"in_Zs")

        self.horizontalLayout.addWidget(self.in_Zs)

        self.si_Zs = QSpinBox(WNotch)
        self.si_Zs.setObjectName(u"si_Zs")

        self.horizontalLayout.addWidget(self.si_Zs)

        self.in_alpha = QLabel(WNotch)
        self.in_alpha.setObjectName(u"in_alpha")

        self.horizontalLayout.addWidget(self.in_alpha)

        self.lf_alpha = FloatEdit(WNotch)
        self.lf_alpha.setObjectName(u"lf_alpha")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lf_alpha.sizePolicy().hasHeightForWidth())
        self.lf_alpha.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lf_alpha)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_notch = QWidget(WNotch)
        self.w_notch.setObjectName(u"w_notch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.w_notch.sizePolicy().hasHeightForWidth())
        self.w_notch.setSizePolicy(sizePolicy1)
        self.w_notch.setMinimumSize(QSize(750, 450))

        self.main_layout.addWidget(self.w_notch)

        self.retranslateUi(WNotch)

        QMetaObject.connectSlotsByName(WNotch)

    # setupUi

    def retranslateUi(self, WNotch):
        WNotch.setWindowTitle(QCoreApplication.translate("WNotch", u"Form", None))
        self.c_notch_type.setItemText(
            0, QCoreApplication.translate("WNotch", u"Slot Type 50", None)
        )
        self.c_notch_type.setItemText(
            1, QCoreApplication.translate("WNotch", u"Slot Type 51", None)
        )
        self.c_notch_type.setItemText(
            2, QCoreApplication.translate("WNotch", u"Slot Type 52", None)
        )
        self.c_notch_type.setItemText(
            3, QCoreApplication.translate("WNotch", u"Slot Type 53", None)
        )
        self.c_notch_type.setItemText(
            4, QCoreApplication.translate("WNotch", u"Slot Type 54", None)
        )
        self.c_notch_type.setItemText(
            5, QCoreApplication.translate("WNotch", u"Slot Type 55", None)
        )
        self.c_notch_type.setItemText(
            6, QCoreApplication.translate("WNotch", u"Slot Type 56", None)
        )

        self.in_Zs.setText(QCoreApplication.translate("WNotch", u"Zs:", None))
        self.in_alpha.setText(QCoreApplication.translate("WNotch", u"Alpha:", None))

    # retranslateUi
