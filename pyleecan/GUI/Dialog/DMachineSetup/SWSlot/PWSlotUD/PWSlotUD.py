from numpy import pi
from qtpy.QtCore import Signal
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QWidget, QDialog
from qtpy.QtWidgets import QMessageBox
from qtpy.QtCore import Qt

from ......Functions.GUI.log_error import log_error
from ......Functions.load import load
from ......Classes.SlotUD import SlotUD
from ......Classes.SlotUD2 import SlotUD2
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlotUD.Ui_PWSlotUD import Ui_PWSlotUD
from ......Methods.Slot.Slot import SlotCheckError
from ......GUI.Dxf.DXF_Slot import DXF_Slot


class PWSlotUD(Ui_PWSlotUD, QWidget):
    """Page to set the slot from DXF"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    ZsChanged = Signal()  # Signal to update the slot number after loading a slot

    # Information for WslotMag
    slot_name = "Import from DXF"
    notch_name = "Import from DXF"
    slot_type = SlotUD

    def __init__(self, lamination=None, material_dict=None, notch_obj=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : PWSlotUD
            A PWSlotUD widget
        lamination : Lamination
            current lamination to edit
        material_dict: dict
            Materials dictionary (library + machine)
        notch_obj : notch
            current notch to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Set properties
        self.lamination = lamination
        self.slot = lamination.slot
        self.u = gui_option.unit
        self.material_dict = material_dict
        self.dxf_gui = None  # Link to the popup
        self.is_notch = notch_obj is not None
        self.notch_obj = notch_obj
        self.test_err_msg = None  # To store error message for tests

        # Setup Path selector for Json files
        self.w_path_json.obj = None
        self.w_path_json.param_name = None
        self.w_path_json.verbose_name = "Load from json"
        self.w_path_json.extension = "JSON file (*.json)"
        self.w_path_json.update()

        # Wedge setup
        if self.is_notch:
            self.g_wedge.hide()
            self.b_dxf.setText("Define Notch from DXF")
        else:
            self.g_wedge.setChecked(self.slot.wedge_mat is not None)
            self.w_wedge_mat.setText("Wedge Material")
            if lamination.mat_type is not None and lamination.mat_type.name not in [
                "",
                None,
            ]:
                self.w_wedge_mat.def_mat = lamination.mat_type.name
            else:
                self.w_wedge_mat.def_mat = "M400-50A"
            self.set_wedge()

        # Update the GUI according to the current slot
        self.update_graph()
        self.w_out.comp_output()

        # Connect the signals
        self.b_dxf.clicked.connect(self.open_DXF_Slot)
        self.w_path_json.pathChanged.connect(self.load_slot)
        self.g_wedge.toggled.connect(self.set_wedge)

    def set_wedge(self):
        """Setup the slot wedge according to the GUI"""
        if self.g_wedge.isChecked():
            if isinstance(self.slot, SlotUD2) and self.slot.wedge_surf_list in [
                None,
                list(),
            ]:
                self.test_err_msg = "To add wedges on imported slot, please select wedges surface during the import"
                log_error(self, self.test_err_msg)
                self.g_wedge.setChecked(False)
                return
            self.w_wedge_mat.update(self.slot, "wedge_mat", self.material_dict)
        else:
            self.slot.wedge_mat = None
        self.update_graph()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def update_graph(self):
        """Plot the lamination with/without the slot"""
        # Use a copy to avoid changing the main object
        lam = self.lamination.copy()
        try:
            self.slot.check()
            lam.slot = self.slot
        except Exception:
            # Plot only the lamination
            lam.slot = None
        # Plot the lamination in the viewer fig
        lam.plot(fig=self.w_viewer.fig, is_show_fig=False)

        # Update the Graph
        self.w_viewer.axes.set_title("")
        self.w_viewer.axes.set_axis_off()
        self.w_viewer.axes.axis("equal")
        if self.w_viewer.axes.get_legend() is not None:
            self.w_viewer.axes.get_legend().remove()
        self.w_viewer.draw()

    def load_slot(self):
        """Load the selected json file and display the slot"""
        # Check that the json file is correct
        try:
            slot = load(self.w_path_json.get_path())
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error when loading file:\n" + str(e)),
            )
            return
        # Check that the json file contain a SlotUD
        if not isinstance(slot, (SlotUD, SlotUD2)):
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr(
                    "The choosen file is not a SlotUD file (" + str(type(slot)) + ")"
                ),
            )
            return

        # Update the slot object
        self.lamination.slot = slot
        self.slot = self.lamination.slot
        self.ZsChanged.emit()
        self.set_wedge()

        try:
            # Update the new GUI according to the slot
            self.update_graph()
            self.w_out.comp_output()
        except:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("An error occured while updating the plot."),
            )

    def open_DXF_Slot(self):
        """Open the GUI to define the SlotUD"""
        # Init GUI with lamination parameters
        self.dxf_gui = DXF_Slot(
            Zs=self.slot.Zs, lam=self.lamination, is_notch=self.is_notch
        )
        self.dxf_gui.setWindowFlags(Qt.Window)  # To maximize the GUI
        self.dxf_gui.show()
        # Update the slot when saving
        self.dxf_gui.accepted.connect(self.set_dxf_path)

    def set_dxf_path(self):
        """Update the slot according to the file defined by DXF_Slot"""
        # Get the saving path from DXF_Slot
        self.w_path_json.set_path_txt(self.dxf_gui.save_path)
        # Update slot and GUI
        self.load_slot()
        self.dxf_gui = None

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return "Unable to compute yoke height:" + str(error)

        if yoke_height <= 0:
            return "The slot height is greater than the lamination !"

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
