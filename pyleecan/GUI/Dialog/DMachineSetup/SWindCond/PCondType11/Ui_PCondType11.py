# -*- coding: utf-8 -*-

# File generated according to PCondType11.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from ......GUI.Tools.FloatEdit import FloatEdit
from ......GUI.Dialog.DMachineSetup.SWindCond.WCondOut.WCondOut import WCondOut
from ......GUI.Dialog.DMatLib.WMatSelect.WMatSelectV import WMatSelectV

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_PCondType11(object):
    def setupUi(self, PCondType11):
        if not PCondType11.objectName():
            PCondType11.setObjectName("PCondType11")
        PCondType11.resize(1019, 583)
        self.horizontalLayout = QHBoxLayout(PCondType11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_cond = QLabel(PCondType11)
        self.img_cond.setObjectName("img_cond")
        self.img_cond.setMinimumSize(QSize(0, 0))
        self.img_cond.setMaximumSize(QSize(16777215, 16777215))
        self.img_cond.setPixmap(
            QPixmap(":/images/images/MachineSetup/WindParam/CondType11.png")
        )
        self.img_cond.setScaledContents(False)
        self.img_cond.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_cond)

        self.scrollArea = QScrollArea(PCondType11)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(350, 0))
        self.scrollArea.setMaximumSize(QSize(350, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 348, 559))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lf_Wwire = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Wwire.setObjectName("lf_Wwire")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lf_Wwire.sizePolicy().hasHeightForWidth())
        self.lf_Wwire.setSizePolicy(sizePolicy)
        self.lf_Wwire.setMinimumSize(QSize(0, 0))
        self.lf_Wwire.setMaximumSize(QSize(50, 100))

        self.gridLayout_2.addWidget(self.lf_Wwire, 2, 1, 1, 1)

        self.in_Wwire = QLabel(self.scrollAreaWidgetContents)
        self.in_Wwire.setObjectName("in_Wwire")
        self.in_Wwire.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.in_Wwire, 2, 0, 1, 1)

        self.in_Nwpc1_tan = QLabel(self.scrollAreaWidgetContents)
        self.in_Nwpc1_tan.setObjectName("in_Nwpc1_tan")
        self.in_Nwpc1_tan.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.in_Nwpc1_tan, 1, 0, 1, 1)

        self.si_Nwpc1_tan = QSpinBox(self.scrollAreaWidgetContents)
        self.si_Nwpc1_tan.setObjectName("si_Nwpc1_tan")
        sizePolicy.setHeightForWidth(self.si_Nwpc1_tan.sizePolicy().hasHeightForWidth())
        self.si_Nwpc1_tan.setSizePolicy(sizePolicy)
        self.si_Nwpc1_tan.setMinimumSize(QSize(0, 0))
        self.si_Nwpc1_tan.setMaximumSize(QSize(50, 16777215))
        self.si_Nwpc1_tan.setValue(99)

        self.gridLayout_2.addWidget(self.si_Nwpc1_tan, 1, 1, 1, 1)

        self.si_Nwpc1_rad = QSpinBox(self.scrollAreaWidgetContents)
        self.si_Nwpc1_rad.setObjectName("si_Nwpc1_rad")
        sizePolicy.setHeightForWidth(self.si_Nwpc1_rad.sizePolicy().hasHeightForWidth())
        self.si_Nwpc1_rad.setSizePolicy(sizePolicy)
        self.si_Nwpc1_rad.setMaximumSize(QSize(50, 16777215))
        self.si_Nwpc1_rad.setValue(99)

        self.gridLayout_2.addWidget(self.si_Nwpc1_rad, 0, 1, 1, 1)

        self.unit_Wwire = QLabel(self.scrollAreaWidgetContents)
        self.unit_Wwire.setObjectName("unit_Wwire")
        self.unit_Wwire.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.unit_Wwire, 2, 2, 1, 1)

        self.in_Hwire = QLabel(self.scrollAreaWidgetContents)
        self.in_Hwire.setObjectName("in_Hwire")
        self.in_Hwire.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.in_Hwire, 3, 0, 1, 1)

        self.in_Nwpc1_rad = QLabel(self.scrollAreaWidgetContents)
        self.in_Nwpc1_rad.setObjectName("in_Nwpc1_rad")
        self.in_Nwpc1_rad.setMinimumSize(QSize(200, 0))

        self.gridLayout_2.addWidget(self.in_Nwpc1_rad, 0, 0, 1, 1)

        self.unit_Hwire = QLabel(self.scrollAreaWidgetContents)
        self.unit_Hwire.setObjectName("unit_Hwire")
        self.unit_Hwire.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.unit_Hwire, 3, 2, 1, 1)

        self.lf_Hwire = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Hwire.setObjectName("lf_Hwire")
        sizePolicy.setHeightForWidth(self.lf_Hwire.sizePolicy().hasHeightForWidth())
        self.lf_Hwire.setSizePolicy(sizePolicy)
        self.lf_Hwire.setMinimumSize(QSize(0, 0))
        self.lf_Hwire.setMaximumSize(QSize(50, 100))

        self.gridLayout_2.addWidget(self.lf_Hwire, 3, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.w_mat_0 = WMatSelectV(self.scrollAreaWidgetContents)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))
        self.w_mat_0.setMaximumSize(QSize(328, 16777215))

        self.verticalLayout.addWidget(self.w_mat_0)

        self.g_ins = QGroupBox(self.scrollAreaWidgetContents)
        self.g_ins.setObjectName("g_ins")
        self.g_ins.setMaximumSize(QSize(328, 16777215))
        self.g_ins.setCheckable(True)
        self.g_ins.setChecked(False)
        self.gridLayout = QGridLayout(self.g_ins)
        self.gridLayout.setObjectName("gridLayout")
        self.in_Wins_wire = QLabel(self.g_ins)
        self.in_Wins_wire.setObjectName("in_Wins_wire")
        self.in_Wins_wire.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.in_Wins_wire, 0, 0, 1, 1)

        self.lf_Wins_wire = FloatEdit(self.g_ins)
        self.lf_Wins_wire.setObjectName("lf_Wins_wire")
        sizePolicy.setHeightForWidth(self.lf_Wins_wire.sizePolicy().hasHeightForWidth())
        self.lf_Wins_wire.setSizePolicy(sizePolicy)
        self.lf_Wins_wire.setMinimumSize(QSize(0, 0))
        self.lf_Wins_wire.setMaximumSize(QSize(50, 100))

        self.gridLayout.addWidget(self.lf_Wins_wire, 0, 1, 1, 1)

        self.unit_Wins_wire = QLabel(self.g_ins)
        self.unit_Wins_wire.setObjectName("unit_Wins_wire")
        self.unit_Wins_wire.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Wins_wire, 0, 2, 1, 1)

        self.w_mat_1 = WMatSelectV(self.g_ins)
        self.w_mat_1.setObjectName("w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))
        self.w_mat_1.setMaximumSize(QSize(306, 16777215))

        self.gridLayout.addWidget(self.w_mat_1, 1, 0, 1, 3)

        self.verticalLayout.addWidget(self.g_ins)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_Lewout = QLabel(self.scrollAreaWidgetContents)
        self.in_Lewout.setObjectName("in_Lewout")
        self.in_Lewout.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.in_Lewout)

        self.lf_Lewout = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Lewout.setObjectName("lf_Lewout")
        sizePolicy.setHeightForWidth(self.lf_Lewout.sizePolicy().hasHeightForWidth())
        self.lf_Lewout.setSizePolicy(sizePolicy)
        self.lf_Lewout.setMinimumSize(QSize(0, 0))
        self.lf_Lewout.setMaximumSize(QSize(50, 100))

        self.horizontalLayout_2.addWidget(self.lf_Lewout)

        self.unit_Lewout = QLabel(self.scrollAreaWidgetContents)
        self.unit_Lewout.setObjectName("unit_Lewout")
        self.unit_Lewout.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.unit_Lewout)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.w_out = WCondOut(self.scrollAreaWidgetContents)
        self.w_out.setObjectName("w_out")
        self.w_out.setMinimumSize(QSize(0, 0))
        self.w_out.setMaximumSize(QSize(328, 16777215))

        self.verticalLayout.addWidget(self.w_out)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.si_Nwpc1_tan, self.si_Nwpc1_rad)
        QWidget.setTabOrder(self.si_Nwpc1_rad, self.lf_Wwire)
        QWidget.setTabOrder(self.lf_Wwire, self.lf_Hwire)
        QWidget.setTabOrder(self.lf_Hwire, self.lf_Wins_wire)

        self.retranslateUi(PCondType11)

        QMetaObject.connectSlotsByName(PCondType11)

    # setupUi

    def retranslateUi(self, PCondType11):
        PCondType11.setWindowTitle(
            QCoreApplication.translate("PCondType11", "Form", None)
        )
        self.img_cond.setText("")
        self.in_Wwire.setText(
            QCoreApplication.translate("PCondType11", "Conductor width", None)
        )
        self.in_Nwpc1_tan.setText(
            QCoreApplication.translate(
                "PCondType11", "Strands in tangential direction", None
            )
        )
        self.unit_Wwire.setText(QCoreApplication.translate("PCondType11", "m", None))
        self.in_Hwire.setText(
            QCoreApplication.translate("PCondType11", "Conductor height", None)
        )
        self.in_Nwpc1_rad.setText(
            QCoreApplication.translate(
                "PCondType11", "Strands in radial direction", None
            )
        )
        self.unit_Hwire.setText(QCoreApplication.translate("PCondType11", "m", None))
        self.g_ins.setTitle(
            QCoreApplication.translate("PCondType11", "Insulation", None)
        )
        self.in_Wins_wire.setText(
            QCoreApplication.translate("PCondType11", "Insulator thickness", None)
        )
        self.unit_Wins_wire.setText(
            QCoreApplication.translate("PCondType11", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType11", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.in_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType11",
                "End-winding length on one side for a half-turn (only used in voltage driven simulations)",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Lewout.setText(
            QCoreApplication.translate("PCondType11", "End winding length", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType11", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lf_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType11", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.unit_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType11", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.unit_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType11", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.unit_Lewout.setText(QCoreApplication.translate("PCondType11", "m", None))

    # retranslateUi
