# -*- coding: utf-8 -*-

# File generated according to DMatSetup.ui
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DMatSetup(object):
    def setupUi(self, DMatSetup):
        DMatSetup.setObjectName("DMatSetup")
        DMatSetup.resize(388, 451)
        self.verticalLayout = QtWidgets.QVBoxLayout(DMatSetup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_name = QtWidgets.QLabel(DMatSetup)
        self.in_name.setObjectName("in_name")
        self.horizontalLayout.addWidget(self.in_name)
        self.le_name = QtWidgets.QLineEdit(DMatSetup)
        self.le_name.setText("")
        self.le_name.setObjectName("le_name")
        self.horizontalLayout.addWidget(self.le_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.is_isotropic = QtWidgets.QCheckBox(DMatSetup)
        self.is_isotropic.setObjectName("is_isotropic")
        self.verticalLayout.addWidget(self.is_isotropic)
        self.nav_phy = QtWidgets.QTabWidget(DMatSetup)
        self.nav_phy.setMinimumSize(QtCore.QSize(370, 0))
        self.nav_phy.setObjectName("nav_phy")
        self.tab_elec = QtWidgets.QWidget()
        self.tab_elec.setObjectName("tab_elec")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_elec)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lf_rho_elec = FloatEdit(self.tab_elec)
        self.lf_rho_elec.setObjectName("lf_rho_elec")
        self.gridLayout_2.addWidget(self.lf_rho_elec, 0, 1, 1, 1)
        self.lf_epsr = FloatEdit(self.tab_elec)
        self.lf_epsr.setObjectName("lf_epsr")
        self.gridLayout_2.addWidget(self.lf_epsr, 1, 1, 1, 1)
        self.unit_rho_elec = QtWidgets.QLabel(self.tab_elec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.unit_rho_elec.setFont(font)
        self.unit_rho_elec.setObjectName("unit_rho_elec")
        self.gridLayout_2.addWidget(self.unit_rho_elec, 0, 2, 1, 1)
        self.in_epsr = QtWidgets.QLabel(self.tab_elec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_epsr.setFont(font)
        self.in_epsr.setObjectName("in_epsr")
        self.gridLayout_2.addWidget(self.in_epsr, 1, 0, 1, 1)
        self.in_rho_elec = QtWidgets.QLabel(self.tab_elec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_rho_elec.setFont(font)
        self.in_rho_elec.setObjectName("in_rho_elec")
        self.gridLayout_2.addWidget(self.in_rho_elec, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.nav_phy.addTab(self.tab_elec, "")
        self.tab_mag = QtWidgets.QWidget()
        self.tab_mag.setObjectName("tab_mag")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_mag)
        self.gridLayout.setObjectName("gridLayout")
        self.unit_Brm20 = QtWidgets.QLabel(self.tab_mag)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.unit_Brm20.setFont(font)
        self.unit_Brm20.setObjectName("unit_Brm20")
        self.gridLayout.addWidget(self.unit_Brm20, 1, 2, 1, 1)
        self.lf_alpha_Br = FloatEdit(self.tab_mag)
        self.lf_alpha_Br.setObjectName("lf_alpha_Br")
        self.gridLayout.addWidget(self.lf_alpha_Br, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.in_Wlam = QtWidgets.QLabel(self.tab_mag)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Wlam.setFont(font)
        self.in_Wlam.setObjectName("in_Wlam")
        self.gridLayout.addWidget(self.in_Wlam, 3, 0, 1, 1)
        self.lf_Brm20 = FloatEdit(self.tab_mag)
        self.lf_Brm20.setObjectName("lf_Brm20")
        self.gridLayout.addWidget(self.lf_Brm20, 1, 1, 1, 1)
        self.in_mur_lin = QtWidgets.QLabel(self.tab_mag)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_mur_lin.setFont(font)
        self.in_mur_lin.setObjectName("in_mur_lin")
        self.gridLayout.addWidget(self.in_mur_lin, 0, 0, 1, 1)
        self.lf_mur_lin = FloatEdit(self.tab_mag)
        self.lf_mur_lin.setObjectName("lf_mur_lin")
        self.gridLayout.addWidget(self.lf_mur_lin, 0, 1, 1, 1)
        self.in_alpha_Br = QtWidgets.QLabel(self.tab_mag)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_alpha_Br.setFont(font)
        self.in_alpha_Br.setObjectName("in_alpha_Br")
        self.gridLayout.addWidget(self.in_alpha_Br, 2, 0, 1, 1)
        self.lf_Wlam = FloatEdit(self.tab_mag)
        self.lf_Wlam.setObjectName("lf_Wlam")
        self.gridLayout.addWidget(self.lf_Wlam, 3, 1, 1, 1)
        self.unit_Wlam = QtWidgets.QLabel(self.tab_mag)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.unit_Wlam.setFont(font)
        self.unit_Wlam.setObjectName("unit_Wlam")
        self.gridLayout.addWidget(self.unit_Wlam, 3, 2, 1, 1)
        self.in_Brm20 = QtWidgets.QLabel(self.tab_mag)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Brm20.setFont(font)
        self.in_Brm20.setObjectName("in_Brm20")
        self.gridLayout.addWidget(self.in_Brm20, 1, 0, 1, 1)
        self.group_BH = QtWidgets.QGroupBox(self.tab_mag)
        self.group_BH.setObjectName("group_BH")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.group_BH)
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.in_BH_file = QtWidgets.QLabel(self.group_BH)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_BH_file.sizePolicy().hasHeightForWidth())
        self.in_BH_file.setSizePolicy(sizePolicy)
        self.in_BH_file.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.in_BH_file.setObjectName("in_BH_file")
        self.gridLayout_4.addWidget(self.in_BH_file, 0, 1, 1, 1)
        self.in_file = QtWidgets.QLabel(self.group_BH)
        self.in_file.setObjectName("in_file")
        self.gridLayout_4.addWidget(self.in_file, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.b_new = QtWidgets.QPushButton(self.group_BH)
        self.b_new.setEnabled(False)
        self.b_new.setObjectName("b_new")
        self.horizontalLayout_8.addWidget(self.b_new)
        self.b_edit = QtWidgets.QPushButton(self.group_BH)
        self.b_edit.setEnabled(False)
        self.b_edit.setObjectName("b_edit")
        self.horizontalLayout_8.addWidget(self.b_edit)
        self.b_plot = QtWidgets.QPushButton(self.group_BH)
        self.b_plot.setEnabled(False)
        self.b_plot.setObjectName("b_plot")
        self.horizontalLayout_8.addWidget(self.b_plot)
        self.b_xls = QtWidgets.QPushButton(self.group_BH)
        self.b_xls.setObjectName("b_xls")
        self.horizontalLayout_8.addWidget(self.b_xls)
        self.b_csv = QtWidgets.QPushButton(self.group_BH)
        self.b_csv.setEnabled(False)
        self.b_csv.setObjectName("b_csv")
        self.horizontalLayout_8.addWidget(self.b_csv)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.group_BH, 4, 0, 1, 3)
        self.nav_phy.addTab(self.tab_mag, "")
        self.tab_mec = QtWidgets.QWidget()
        self.tab_mec.setObjectName("tab_mec")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_mec)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.in_rho_meca = QtWidgets.QLabel(self.tab_mec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_rho_meca.setFont(font)
        self.in_rho_meca.setObjectName("in_rho_meca")
        self.horizontalLayout_41.addWidget(self.in_rho_meca)
        self.lf_rho_meca = FloatEdit(self.tab_mec)
        self.lf_rho_meca.setObjectName("lf_rho_meca")
        self.horizontalLayout_41.addWidget(self.lf_rho_meca)
        self.unit_rho_meca = QtWidgets.QLabel(self.tab_mec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.unit_rho_meca.setFont(font)
        self.unit_rho_meca.setObjectName("unit_rho_meca")
        self.horizontalLayout_41.addWidget(self.unit_rho_meca)
        self.verticalLayout_12.addLayout(self.horizontalLayout_41)
        self.nav_meca = QtWidgets.QStackedWidget(self.tab_mec)
        self.nav_meca.setObjectName("nav_meca")
        self.page_niso_mec = QtWidgets.QWidget()
        self.page_niso_mec.setObjectName("page_niso_mec")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_niso_mec)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.g_young = QtWidgets.QGroupBox(self.page_niso_mec)
        self.g_young.setObjectName("g_young")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.g_young)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.in_Ex = QtWidgets.QLabel(self.g_young)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Ex.setFont(font)
        self.in_Ex.setObjectName("in_Ex")
        self.horizontalLayout_2.addWidget(self.in_Ex)
        self.lf_Ex = FloatEdit(self.g_young)
        self.lf_Ex.setObjectName("lf_Ex")
        self.horizontalLayout_2.addWidget(self.lf_Ex)
        self.in_Ey = QtWidgets.QLabel(self.g_young)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Ey.setFont(font)
        self.in_Ey.setObjectName("in_Ey")
        self.horizontalLayout_2.addWidget(self.in_Ey)
        self.lf_Ey = FloatEdit(self.g_young)
        self.lf_Ey.setObjectName("lf_Ey")
        self.horizontalLayout_2.addWidget(self.lf_Ey)
        self.in_Ez = QtWidgets.QLabel(self.g_young)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Ez.setFont(font)
        self.in_Ez.setObjectName("in_Ez")
        self.horizontalLayout_2.addWidget(self.in_Ez)
        self.lf_Ez = FloatEdit(self.g_young)
        self.lf_Ez.setObjectName("lf_Ez")
        self.horizontalLayout_2.addWidget(self.lf_Ez)
        self.verticalLayout_4.addWidget(self.g_young)
        self.g_poisson = QtWidgets.QGroupBox(self.page_niso_mec)
        self.g_poisson.setObjectName("g_poisson")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.g_poisson)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.in_nu_xy = QtWidgets.QLabel(self.g_poisson)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_nu_xy.setFont(font)
        self.in_nu_xy.setObjectName("in_nu_xy")
        self.horizontalLayout_3.addWidget(self.in_nu_xy)
        self.lf_nu_xy = FloatEdit(self.g_poisson)
        self.lf_nu_xy.setObjectName("lf_nu_xy")
        self.horizontalLayout_3.addWidget(self.lf_nu_xy)
        self.in_nu_xz = QtWidgets.QLabel(self.g_poisson)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_nu_xz.setFont(font)
        self.in_nu_xz.setObjectName("in_nu_xz")
        self.horizontalLayout_3.addWidget(self.in_nu_xz)
        self.lf_nu_xz = FloatEdit(self.g_poisson)
        self.lf_nu_xz.setObjectName("lf_nu_xz")
        self.horizontalLayout_3.addWidget(self.lf_nu_xz)
        self.in_nu_yz = QtWidgets.QLabel(self.g_poisson)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_nu_yz.setFont(font)
        self.in_nu_yz.setObjectName("in_nu_yz")
        self.horizontalLayout_3.addWidget(self.in_nu_yz)
        self.lf_nu_yz = FloatEdit(self.g_poisson)
        self.lf_nu_yz.setObjectName("lf_nu_yz")
        self.horizontalLayout_3.addWidget(self.lf_nu_yz)
        self.verticalLayout_4.addWidget(self.g_poisson)
        self.g_shear = QtWidgets.QGroupBox(self.page_niso_mec)
        self.g_shear.setObjectName("g_shear")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.g_shear)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.in_Gxy = QtWidgets.QLabel(self.g_shear)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Gxy.setFont(font)
        self.in_Gxy.setObjectName("in_Gxy")
        self.horizontalLayout_4.addWidget(self.in_Gxy)
        self.lf_Gxy = FloatEdit(self.g_shear)
        self.lf_Gxy.setObjectName("lf_Gxy")
        self.horizontalLayout_4.addWidget(self.lf_Gxy)
        self.in_Gxz = QtWidgets.QLabel(self.g_shear)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Gxz.setFont(font)
        self.in_Gxz.setObjectName("in_Gxz")
        self.horizontalLayout_4.addWidget(self.in_Gxz)
        self.lf_Gxz = FloatEdit(self.g_shear)
        self.lf_Gxz.setObjectName("lf_Gxz")
        self.horizontalLayout_4.addWidget(self.lf_Gxz)
        self.in_Gyz = QtWidgets.QLabel(self.g_shear)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Gyz.setFont(font)
        self.in_Gyz.setObjectName("in_Gyz")
        self.horizontalLayout_4.addWidget(self.in_Gyz)
        self.lf_Gyz = FloatEdit(self.g_shear)
        self.lf_Gyz.setObjectName("lf_Gyz")
        self.horizontalLayout_4.addWidget(self.lf_Gyz)
        self.verticalLayout_4.addWidget(self.g_shear)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.nav_meca.addWidget(self.page_niso_mec)
        self.page_iso_mec = QtWidgets.QWidget()
        self.page_iso_mec.setObjectName("page_iso_mec")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_iso_mec)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.in_E = QtWidgets.QLabel(self.page_iso_mec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_E.setFont(font)
        self.in_E.setObjectName("in_E")
        self.gridLayout_6.addWidget(self.in_E, 0, 0, 1, 1)
        self.lf_G = FloatEdit(self.page_iso_mec)
        self.lf_G.setObjectName("lf_G")
        self.gridLayout_6.addWidget(self.lf_G, 2, 2, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem4, 4, 3, 1, 1)
        self.unit_G = QtWidgets.QLabel(self.page_iso_mec)
        self.unit_G.setObjectName("unit_G")
        self.gridLayout_6.addWidget(self.unit_G, 2, 4, 1, 1)
        self.lf_E = FloatEdit(self.page_iso_mec)
        self.lf_E.setObjectName("lf_E")
        self.gridLayout_6.addWidget(self.lf_E, 0, 1, 1, 3)
        self.in_G = QtWidgets.QLabel(self.page_iso_mec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_G.setFont(font)
        self.in_G.setObjectName("in_G")
        self.gridLayout_6.addWidget(self.in_G, 2, 0, 1, 2)
        self.in_nu = QtWidgets.QLabel(self.page_iso_mec)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_nu.setFont(font)
        self.in_nu.setObjectName("in_nu")
        self.gridLayout_6.addWidget(self.in_nu, 1, 0, 1, 3)
        self.lf_nu = FloatEdit(self.page_iso_mec)
        self.lf_nu.setObjectName("lf_nu")
        self.gridLayout_6.addWidget(self.lf_nu, 1, 3, 1, 1)
        self.unit_E = QtWidgets.QLabel(self.page_iso_mec)
        self.unit_E.setObjectName("unit_E")
        self.gridLayout_6.addWidget(self.unit_E, 0, 4, 1, 1)
        self.nav_meca.addWidget(self.page_iso_mec)
        self.verticalLayout_12.addWidget(self.nav_meca)
        self.nav_phy.addTab(self.tab_mec, "")
        self.tab_ther = QtWidgets.QWidget()
        self.tab_ther.setObjectName("tab_ther")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_ther)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.g_lambda = QtWidgets.QGroupBox(self.tab_ther)
        self.g_lambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.g_lambda.setObjectName("g_lambda")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.g_lambda)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.nav_ther = QtWidgets.QStackedWidget(self.g_lambda)
        self.nav_ther.setObjectName("nav_ther")
        self.page_niso_ther = QtWidgets.QWidget()
        self.page_niso_ther.setObjectName("page_niso_ther")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_niso_ther)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.in_Lx = QtWidgets.QLabel(self.page_niso_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Lx.setFont(font)
        self.in_Lx.setObjectName("in_Lx")
        self.horizontalLayout_5.addWidget(self.in_Lx)
        self.lf_Lx = FloatEdit(self.page_niso_ther)
        self.lf_Lx.setObjectName("lf_Lx")
        self.horizontalLayout_5.addWidget(self.lf_Lx)
        self.in_Ly = QtWidgets.QLabel(self.page_niso_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Ly.setFont(font)
        self.in_Ly.setObjectName("in_Ly")
        self.horizontalLayout_5.addWidget(self.in_Ly)
        self.lf_Ly = FloatEdit(self.page_niso_ther)
        self.lf_Ly.setObjectName("lf_Ly")
        self.horizontalLayout_5.addWidget(self.lf_Ly)
        self.in_Lz = QtWidgets.QLabel(self.page_niso_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Lz.setFont(font)
        self.in_Lz.setObjectName("in_Lz")
        self.horizontalLayout_5.addWidget(self.in_Lz)
        self.lf_Lz = FloatEdit(self.page_niso_ther)
        self.lf_Lz.setObjectName("lf_Lz")
        self.horizontalLayout_5.addWidget(self.lf_Lz)
        self.nav_ther.addWidget(self.page_niso_ther)
        self.page_iso_ther = QtWidgets.QWidget()
        self.page_iso_ther.setObjectName("page_iso_ther")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_iso_ther)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.in_L = QtWidgets.QLabel(self.page_iso_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_L.setFont(font)
        self.in_L.setObjectName("in_L")
        self.horizontalLayout_7.addWidget(self.in_L)
        self.lf_L = FloatEdit(self.page_iso_ther)
        self.lf_L.setObjectName("lf_L")
        self.horizontalLayout_7.addWidget(self.lf_L)
        self.unit_L = QtWidgets.QLabel(self.page_iso_ther)
        self.unit_L.setObjectName("unit_L")
        self.horizontalLayout_7.addWidget(self.unit_L)
        self.nav_ther.addWidget(self.page_iso_ther)
        self.verticalLayout_11.addWidget(self.nav_ther)
        self.verticalLayout_2.addWidget(self.g_lambda)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_alpha = QtWidgets.QLabel(self.tab_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_alpha.setFont(font)
        self.in_alpha.setObjectName("in_alpha")
        self.gridLayout_3.addWidget(self.in_alpha, 1, 0, 1, 1)
        self.in_Cp = QtWidgets.QLabel(self.tab_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_Cp.setFont(font)
        self.in_Cp.setObjectName("in_Cp")
        self.gridLayout_3.addWidget(self.in_Cp, 0, 0, 1, 1)
        self.lf_alpha = FloatEdit(self.tab_ther)
        self.lf_alpha.setObjectName("lf_alpha")
        self.gridLayout_3.addWidget(self.lf_alpha, 1, 1, 1, 1)
        self.unit_Cp = QtWidgets.QLabel(self.tab_ther)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.unit_Cp.setFont(font)
        self.unit_Cp.setObjectName("unit_Cp")
        self.gridLayout_3.addWidget(self.unit_Cp, 0, 2, 1, 1)
        self.lf_Cp = FloatEdit(self.tab_ther)
        self.lf_Cp.setObjectName("lf_Cp")
        self.gridLayout_3.addWidget(self.lf_Cp, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.nav_phy.addTab(self.tab_ther, "")
        self.tab_eco = QtWidgets.QWidget()
        self.tab_eco.setObjectName("tab_eco")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_eco)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.in_cost_unit = QtWidgets.QLabel(self.tab_eco)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.in_cost_unit.setFont(font)
        self.in_cost_unit.setObjectName("in_cost_unit")
        self.horizontalLayout_6.addWidget(self.in_cost_unit)
        self.lf_cost_unit = FloatEdit(self.tab_eco)
        self.lf_cost_unit.setObjectName("lf_cost_unit")
        self.horizontalLayout_6.addWidget(self.lf_cost_unit)
        self.unit_cost_unit = QtWidgets.QLabel(self.tab_eco)
        self.unit_cost_unit.setObjectName("unit_cost_unit")
        self.horizontalLayout_6.addWidget(self.unit_cost_unit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.nav_phy.addTab(self.tab_eco, "")
        self.verticalLayout.addWidget(self.nav_phy)
        self.b_close = QtWidgets.QDialogButtonBox(DMatSetup)
        self.b_close.setOrientation(QtCore.Qt.Horizontal)
        self.b_close.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.b_close.setObjectName("b_close")
        self.verticalLayout.addWidget(self.b_close)

        self.retranslateUi(DMatSetup)
        self.nav_phy.setCurrentIndex(1)
        self.nav_meca.setCurrentIndex(1)
        self.nav_ther.setCurrentIndex(1)
        self.b_close.accepted.connect(DMatSetup.accept)
        self.b_close.rejected.connect(DMatSetup.reject)
        QtCore.QMetaObject.connectSlotsByName(DMatSetup)

    def retranslateUi(self, DMatSetup):
        _translate = QtCore.QCoreApplication.translate
        DMatSetup.setWindowTitle(_translate("DMatSetup", "Edit Material"))
        self.in_name.setText(_translate("DMatSetup", "name"))
        self.is_isotropic.setText(_translate("DMatSetup", "is_isotropic"))
        self.unit_rho_elec.setText(_translate("DMatSetup", "ohm.m"))
        self.in_epsr.setText(_translate("DMatSetup", "epsr"))
        self.in_rho_elec.setText(_translate("DMatSetup", "rho"))
        self.nav_phy.setTabText(self.nav_phy.indexOf(self.tab_elec), _translate("DMatSetup", "Electrical"))
        self.unit_Brm20.setText(_translate("DMatSetup", "T"))
        self.in_Wlam.setText(_translate("DMatSetup", "Wlam"))
        self.in_mur_lin.setText(_translate("DMatSetup", "mur_lin"))
        self.in_alpha_Br.setText(_translate("DMatSetup", "alphaBr"))
        self.unit_Wlam.setText(_translate("DMatSetup", "m"))
        self.in_Brm20.setText(_translate("DMatSetup", "Brm20"))
        self.group_BH.setTitle(_translate("DMatSetup", "BH curve"))
        self.in_BH_file.setText(_translate("DMatSetup", "-"))
        self.in_file.setText(_translate("DMatSetup", "File:"))
        self.b_new.setText(_translate("DMatSetup", "New"))
        self.b_edit.setText(_translate("DMatSetup", "Edit"))
        self.b_plot.setText(_translate("DMatSetup", "Plot"))
        self.b_xls.setText(_translate("DMatSetup", "XLS Import"))
        self.b_csv.setText(_translate("DMatSetup", "CSV Import"))
        self.nav_phy.setTabText(self.nav_phy.indexOf(self.tab_mag), _translate("DMatSetup", "Magnetics"))
        self.in_rho_meca.setText(_translate("DMatSetup", "rho"))
        self.unit_rho_meca.setText(_translate("DMatSetup", "kg/m^3"))
        self.g_young.setTitle(_translate("DMatSetup", "Equivalent Yong Modulus [Pa]"))
        self.in_Ex.setText(_translate("DMatSetup", "Ex"))
        self.in_Ey.setText(_translate("DMatSetup", "Ey"))
        self.in_Ez.setText(_translate("DMatSetup", "Ez"))
        self.g_poisson.setTitle(_translate("DMatSetup", "Equivalent Poisson ratio [ ]"))
        self.in_nu_xy.setText(_translate("DMatSetup", "nu_xy"))
        self.in_nu_xz.setText(_translate("DMatSetup", "nu_xz"))
        self.in_nu_yz.setText(_translate("DMatSetup", "nu_yz"))
        self.g_shear.setTitle(_translate("DMatSetup", "Shear modulus [Pa]"))
        self.in_Gxy.setText(_translate("DMatSetup", "Gxy"))
        self.in_Gxz.setText(_translate("DMatSetup", "Gxz"))
        self.in_Gyz.setText(_translate("DMatSetup", "Gyz"))
        self.in_E.setText(_translate("DMatSetup", "E"))
        self.unit_G.setText(_translate("DMatSetup", "Pa"))
        self.in_G.setText(_translate("DMatSetup", "G"))
        self.in_nu.setText(_translate("DMatSetup", "nu"))
        self.unit_E.setText(_translate("DMatSetup", "Pa"))
        self.nav_phy.setTabText(self.nav_phy.indexOf(self.tab_mec), _translate("DMatSetup", "Mechanics"))
        self.g_lambda.setTitle(_translate("DMatSetup", "Lambda [W/K]"))
        self.in_Lx.setText(_translate("DMatSetup", "X"))
        self.in_Ly.setText(_translate("DMatSetup", "Y"))
        self.in_Lz.setText(_translate("DMatSetup", "Z"))
        self.in_L.setText(_translate("DMatSetup", "Lambda"))
        self.unit_L.setText(_translate("DMatSetup", "W / K"))
        self.in_alpha.setText(_translate("DMatSetup", "alpha"))
        self.in_Cp.setText(_translate("DMatSetup", "Cp"))
        self.unit_Cp.setText(_translate("DMatSetup", "W / kg / K"))
        self.nav_phy.setTabText(self.nav_phy.indexOf(self.tab_ther), _translate("DMatSetup", "Thermics"))
        self.in_cost_unit.setText(_translate("DMatSetup", "cost_unit"))
        self.unit_cost_unit.setText(_translate("DMatSetup", "€ / kg"))
        self.nav_phy.setTabText(self.nav_phy.indexOf(self.tab_eco), _translate("DMatSetup", "Economical"))
from pyleecan.GUI.Tools.FloatEdit import FloatEdit
from pyleecan.GUI.Resources import pyleecan_rc
