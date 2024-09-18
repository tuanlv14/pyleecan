# -*- coding: utf-8 -*-

# File generated according to PCondType12.ui
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


class Ui_PCondType12(object):
    def setupUi(self, PCondType12):
        if not PCondType12.objectName():
            PCondType12.setObjectName("PCondType12")
        PCondType12.resize(1189, 672)
        self.horizontalLayout = QHBoxLayout(PCondType12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_cond = QLabel(PCondType12)
        self.img_cond.setObjectName("img_cond")
        self.img_cond.setMinimumSize(QSize(0, 0))
        self.img_cond.setMaximumSize(QSize(16777215, 16777215))
        self.img_cond.setPixmap(
            QPixmap(":/images/images/MachineSetup/WindParam/CondType12.png")
        )
        self.img_cond.setScaledContents(False)
        self.img_cond.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_cond)

        self.scrollArea = QScrollArea(PCondType12)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setMinimumSize(QSize(350, 0))
        self.scrollArea.setMaximumSize(QSize(350, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 348, 648))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_Nwpc1 = QLabel(self.scrollAreaWidgetContents)
        self.in_Nwpc1.setObjectName("in_Nwpc1")
        self.in_Nwpc1.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.in_Nwpc1, 0, 0, 1, 1)

        self.si_Nwpc1 = QSpinBox(self.scrollAreaWidgetContents)
        self.si_Nwpc1.setObjectName("si_Nwpc1")
        self.si_Nwpc1.setMinimumSize(QSize(0, 0))
        self.si_Nwpc1.setMaximumSize(QSize(100, 16777215))
        self.si_Nwpc1.setValue(99)

        self.gridLayout_3.addWidget(self.si_Nwpc1, 0, 1, 1, 1)

        self.in_Wwire = QLabel(self.scrollAreaWidgetContents)
        self.in_Wwire.setObjectName("in_Wwire")
        self.in_Wwire.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.in_Wwire, 1, 0, 1, 1)

        self.lf_Wwire = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Wwire.setObjectName("lf_Wwire")
        self.lf_Wwire.setMinimumSize(QSize(0, 0))
        self.lf_Wwire.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.lf_Wwire, 1, 1, 1, 1)

        self.unit_Wwire = QLabel(self.scrollAreaWidgetContents)
        self.unit_Wwire.setObjectName("unit_Wwire")
        self.unit_Wwire.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.unit_Wwire, 1, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.w_mat_0 = WMatSelectV(self.scrollAreaWidgetContents)
        self.w_mat_0.setObjectName("w_mat_0")
        self.w_mat_0.setMinimumSize(QSize(100, 0))
        self.w_mat_0.setMaximumSize(QSize(328, 16777215))

        self.verticalLayout.addWidget(self.w_mat_0)

        self.g_ins = QGroupBox(self.scrollAreaWidgetContents)
        self.g_ins.setObjectName("g_ins")
        self.g_ins.setCheckable(True)
        self.g_ins.setChecked(False)
        self.gridLayout_2 = QGridLayout(self.g_ins)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.in_Wins_wire = QLabel(self.g_ins)
        self.in_Wins_wire.setObjectName("in_Wins_wire")
        self.in_Wins_wire.setMinimumSize(QSize(90, 0))

        self.gridLayout.addWidget(self.in_Wins_wire, 0, 0, 1, 1)

        self.lf_Wins_wire = FloatEdit(self.g_ins)
        self.lf_Wins_wire.setObjectName("lf_Wins_wire")
        self.lf_Wins_wire.setMinimumSize(QSize(0, 0))
        self.lf_Wins_wire.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Wins_wire, 0, 1, 1, 1)

        self.unit_Wins_wire = QLabel(self.g_ins)
        self.unit_Wins_wire.setObjectName("unit_Wins_wire")

        self.gridLayout.addWidget(self.unit_Wins_wire, 0, 2, 1, 1)

        self.in_Wins_cond = QLabel(self.g_ins)
        self.in_Wins_cond.setObjectName("in_Wins_cond")
        self.in_Wins_cond.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.in_Wins_cond, 1, 0, 1, 1)

        self.lf_Wins_cond = FloatEdit(self.g_ins)
        self.lf_Wins_cond.setObjectName("lf_Wins_cond")
        self.lf_Wins_cond.setMinimumSize(QSize(0, 0))
        self.lf_Wins_cond.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.lf_Wins_cond, 1, 1, 1, 1)

        self.unit_Wins_cond = QLabel(self.g_ins)
        self.unit_Wins_cond.setObjectName("unit_Wins_cond")
        self.unit_Wins_cond.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.unit_Wins_cond, 1, 2, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.w_mat_1 = WMatSelectV(self.g_ins)
        self.w_mat_1.setObjectName("w_mat_1")
        self.w_mat_1.setMinimumSize(QSize(100, 0))
        self.w_mat_1.setMaximumSize(QSize(306, 16777215))

        self.gridLayout_2.addWidget(self.w_mat_1, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.g_ins)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_Lewout = QLabel(self.scrollAreaWidgetContents)
        self.in_Lewout.setObjectName("in_Lewout")
        self.in_Lewout.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.in_Lewout)

        self.lf_Lewout = FloatEdit(self.scrollAreaWidgetContents)
        self.lf_Lewout.setObjectName("lf_Lewout")
        self.lf_Lewout.setMinimumSize(QSize(0, 0))
        self.lf_Lewout.setMaximumSize(QSize(100, 16777215))

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

        QWidget.setTabOrder(self.si_Nwpc1, self.lf_Wwire)
        QWidget.setTabOrder(self.lf_Wwire, self.lf_Wins_cond)

        self.retranslateUi(PCondType12)

        QMetaObject.connectSlotsByName(PCondType12)

    # setupUi

    def retranslateUi(self, PCondType12):
        PCondType12.setWindowTitle(
            QCoreApplication.translate("PCondType12", "Form", None)
        )
        self.img_cond.setText("")
        self.in_Nwpc1.setText(
            QCoreApplication.translate("PCondType12", "Strands in hand", None)
        )
        self.in_Wwire.setText(
            QCoreApplication.translate("PCondType12", "Conductor diameter", None)
        )
        self.unit_Wwire.setText(QCoreApplication.translate("PCondType12", "m", None))
        self.g_ins.setTitle(
            QCoreApplication.translate("PCondType12", "Insulation", None)
        )
        self.in_Wins_wire.setText(
            QCoreApplication.translate("PCondType12", "Insulator thickness", None)
        )
        self.unit_Wins_wire.setText(
            QCoreApplication.translate("PCondType12", "m", None)
        )
        self.in_Wins_cond.setText(
            QCoreApplication.translate("PCondType12", "Overall diameter", None)
        )
        self.unit_Wins_cond.setText(
            QCoreApplication.translate("PCondType12", "m", None)
        )
        # if QT_CONFIG(tooltip)
        self.in_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType12", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.in_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType12",
                "End-winding length on one side for a half-turn (only used in voltage driven simulations)",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.in_Lewout.setText(
            QCoreApplication.translate("PCondType12", "End winding length", None)
        )
        # if QT_CONFIG(tooltip)
        self.lf_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType12", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lf_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType12", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.unit_Lewout.setToolTip(
            QCoreApplication.translate(
                "PCondType12", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.unit_Lewout.setWhatsThis(
            QCoreApplication.translate(
                "PCondType12", "End-winding length on one side for a half-turn", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.unit_Lewout.setText(QCoreApplication.translate("PCondType12", "m", None))

    # retranslateUi
