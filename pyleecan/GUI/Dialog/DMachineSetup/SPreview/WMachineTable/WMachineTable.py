# -*- coding: utf-8 -*-

from logging import getLogger
from os.path import join

import matplotlib.pyplot as plt
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QWidget, QMessageBox

from ......Classes._FEMMHandler import _FEMMHandler
from ......Classes.Output import Output
from ......Classes.Simu1 import Simu1
from ......definitions import config_dict
from ......loggers import GUI_LOG_NAME
from ......Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ......Functions.FEMM.draw_FEMM import draw_FEMM
from ......Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from ......GUI.Dialog.DMachineSetup.SPreview.WMachineTable.Ui_WMachineTable import (
    Ui_WMachineTable,
)
from SciDataTool import DataLinspace
from ......Methods.Simulation.MagElmer import (
    boundary_prop,
    boundary_list,
    surface_label,
)

try:
    from ......Functions.GMSH.draw_GMSH import draw_GMSH
except:
    draw_GMSH = ImportError
try:
    from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
except:
    gen_3D_mesh = ImportError


class WMachineTable(Ui_WMachineTable, QWidget):
    """Table to display the main paramaters of the machine"""

    def __init__(self, parent=None):
        """Initialize the GUI

        Parameters
        ----------
        self : SWindCond
            A SWindCond widget
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.machine = None

        # Connect the widget
        self.b_mmf.clicked.connect(self.plot_mmf)
        self.b_FEMM.clicked.connect(self.draw_FEMM)
        if isinstance(draw_FEMM, ImportError):
            self.b_GMSH.setEnabled(False)
            self.b_GMSH_3D.setEnabled(False)
        else:
            self.b_GMSH.clicked.connect(self.draw_GMSH)
            self.b_GMSH_3D.clicked.connect(self.draw_GMSH_3D)
        self.b_plot_machine.clicked.connect(self.plot_machine)

    def update_tab(self, machine):
        """Update the table to match the machine

        Parameters
        ----------
        self : WMachineTable
            A WMachineTable object
        """

        self.machine = machine
        desc_dict = self.machine.comp_desc_dict()

        self.tab_param.clear()
        # Set header
        self.tab_param.setColumnCount(2)
        item = QTableWidgetItem("Name")
        self.tab_param.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("Value")
        self.tab_param.setHorizontalHeaderItem(1, item)
        # Set containt
        for ii, desc in enumerate(desc_dict):
            if desc["value"] is not None:
                self.tab_param.insertRow(ii)
                self.tab_param.setItem(ii, 0, QTableWidgetItem(desc["verbose"]))
                if desc["type"] is float:
                    txt = format(desc["value"], ".4g")
                else:
                    txt = str(desc["value"])
                if desc["unit"] not in ["", None]:
                    txt += " " + desc["unit"]
                self.tab_param.setItem(ii, 1, QTableWidgetItem(txt))

    def plot_mmf(self):
        """Plot the unit mmf of the stator"""
        if self.machine is not None:
            self.machine.stator.plot_mmf_unit(is_show_fig=True)
        set_plot_gui_icon()

    def plot_machine(self):
        """Plot the machine"""
        if self.machine is not None:
            self.machine.plot()
        set_plot_gui_icon()

    def draw_FEMM(self):
        """Draw the Machine in FEMM"""

        save_file_path = self.get_save_path(ext=".fem", file_type="FEMM (*.fem)")
        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path is [None, ""]:
            return

        femm = _FEMMHandler()
        output = Output(simu=Simu1(machine=self.machine))
        # Periodicity
        sym, is_antiper, _, _ = self.machine.comp_periodicity()
        if is_antiper:
            sym *= 2
        # Set Current (constant J in a layer)
        S_slot = self.machine.stator.slot.comp_surface_active()
        (Nrad, Ntan) = self.machine.stator.winding.get_dim_wind()
        Sphase = S_slot / (Nrad * Ntan)
        J = 5e6
        output.elec.Id_ref = J * Sphase
        output.elec.Iq_ref = 0
        output.elec.felec = 60
        output.elec.Time = DataLinspace(
            name="time",
            unit="s",
            initial=0,
            final=60,
            number=20,
            include_endpoint=False,
        )
        time = output.elec.Time.get_values(
            is_oneperiod=False,
            is_antiperiod=False,
        )
        Is = output.elec.comp_I_mag(time, is_stator=True)
        try:
            # Draw the machine
            FEMM_dict = draw_FEMM(
                femm,
                output,
                is_mmfr=True,
                is_mmfs=True,
                sym=sym,
                is_antiper=is_antiper,
                type_calc_leakage=0,
                path_save=None,
                is_sliding_band=True,
            )
            # Set the current
            update_FEMM_simulation(
                femm=femm,
                circuits=FEMM_dict["circuits"],
                is_sliding_band=True,
                is_internal_rotor=self.machine.rotor.is_internal,
                angle_rotor=[0],
                Is=Is,
                Ir=None,
                ii=0,
            )
            femm.mi_saveas(save_file_path)  # Save
        except Exception as e:
            err_msg = (
                "Error while drawing machine "
                + self.machine.name
                + " in FEMM:\n"
                + str(e)
            )
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(err_msg),
            )
        femm.closefemm()

    def draw_GMSH(self):
        save_file_path = self.get_save_path(ext=".msh", file_type="GMSH (*.msh)")
        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path is [None, ""]:
            return
        # Create the Simulation
        mySimu = Simu1(name="test_gmsh_ipm", machine=self.machine)
        myResults = Output(simu=mySimu)
        sym, is_antiper, _, _ = self.machine.comp_periodicity()
        if is_antiper:
            sym *= 2
        try:
            draw_GMSH(
                output=myResults,
                sym=sym,
                boundary_prop=boundary_prop,
                boundary_list=boundary_list,
                surface_label=surface_label,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=None,
                is_sliding_band=True,
                is_airbox=True,
                path_save=save_file_path,
            )
        except Exception as e:
            err_msg = (
                "Error while drawing machine "
                + self.machine.name
                + " in GMSH:\n"
                + str(e)
            )
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(err_msg),
            )

    def draw_GMSH_3D(self):
        save_file_path = self.get_save_path(ext="_stator.msh", file_type="GMSH (*.msh)")
        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path is [None, ""]:
            return
        try:
            gen_3D_mesh(
                lamination=self.machine.stator,
                save_path=save_file_path,
                mesh_size=(self.machine.stator.Rext - self.machine.stator.Rint) / 20,
                Nlayer=20,
                display=False,
            )
        except Exception as e:
            err_msg = (
                "Error while drawing machine "
                + self.machine.name
                + " in GMSH:\n"
                + str(e)
            )
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(err_msg),
            )

    def get_save_path(self, ext=".fem", file_type="FEMM (*.fem)"):
        machine_path = config_dict["MAIN"]["MACHINE_DIR"]
        # Ask the user to select a .fem file to save
        if self.machine.name in ["", None]:
            return QFileDialog.getSaveFileName(
                self, self.tr("Save file"), machine_path, file_type
            )[0]
        else:
            def_path = join(machine_path, self.machine.name + ext)
            return QFileDialog.getSaveFileName(
                self, self.tr("Save file"), def_path, file_type
            )[0]
