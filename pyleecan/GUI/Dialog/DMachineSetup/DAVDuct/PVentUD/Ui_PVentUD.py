# -*- coding: utf-8 -*-

# File generated according to PVentUD.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Dialog.DMachineSetup.DAVDuct.WVentOut.WVentOut import WVentOut
from ......GUI.Tools.SpinBox import SpinBox
from ......GUI.Tools.WPathSelector.WPathSelectorV import WPathSelectorV
from ......GUI.Tools.MPLCanvas import MPLCanvas

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PVentUD(object):
    def setupUi(self, PVentUD):
        if not PVentUD.objectName():
            PVentUD.setObjectName("PVentUD")
        PVentUD.resize(641, 440)
        PVentUD.setMinimumSize(QSize(0, 440))
        PVentUD.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(PVentUD)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.w_viewer = MPLCanvas(PVentUD)
        self.w_viewer.setObjectName("w_viewer")

        self.horizontalLayout.addWidget(self.w_viewer)

        self.scrollArea = QScrollArea(PVentUD)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(300, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 416))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b_dxf = QPushButton(self.scrollAreaWidgetContents)
        self.b_dxf.setObjectName("b_dxf")

        self.verticalLayout.addWidget(self.b_dxf)

        self.w_path_json = WPathSelectorV(self.scrollAreaWidgetContents)
        self.w_path_json.setObjectName("w_path_json")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_path_json.sizePolicy().hasHeightForWidth())
        self.w_path_json.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.w_path_json)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_Zh = QLabel(self.scrollAreaWidgetContents)
        self.in_Zh.setObjectName("in_Zh")

        self.gridLayout.addWidget(self.in_Zh, 0, 0, 1, 1)

        self.si_Zh = SpinBox(self.scrollAreaWidgetContents)
        self.si_Zh.setObjectName("si_Zh")
        self.si_Zh.setMaximum(999999999)

        self.gridLayout.addWidget(self.si_Zh, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WVentOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(PVentUD)

        QMetaObject.connectSlotsByName(PVentUD)

    # setupUi

    def retranslateUi(self, PVentUD):
        PVentUD.setWindowTitle(QCoreApplication.translate("PVentUD", "Form", None))
        self.b_dxf.setText(
            QCoreApplication.translate("PVentUD", "Define Duct from DXF", None)
        )
        self.in_Zh.setText(QCoreApplication.translate("PVentUD", "Zh :", None))

    # retranslateUi
