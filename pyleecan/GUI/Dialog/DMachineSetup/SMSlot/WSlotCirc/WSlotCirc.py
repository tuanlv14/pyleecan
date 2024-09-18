# -*- coding: utf-8 -*-

import qtpy.QtCore
from numpy import pi
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget
from qtpy.QtGui import QPixmap
from ......Classes.SlotCirc import SlotCirc
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMSlot.WSlotCirc.Gen_WSlotCirc import Gen_WSlotCirc
from ......Methods.Slot.Slot import SlotCheckError

translate = qtpy.QtCore.QCoreApplication.translate
from ......GUI.Resources import pixmap_dict


class WSlotCirc(Gen_WSlotCirc, QWidget):
    """Page to set the Slot Magnet Type 10"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Circular Slot"
    notch_name = "Circular"
    slot_type = SlotCirc

    def __init__(self, lamination=None, notch_obj=None, material_dict=None):
        """Initialize the widget according to lamination

        Parameters
        ----------
        self : SlotCirc
            A SlotCirc widget
        lamination : Lamination
            current lamination to edit
        notch_obj : notch
            current notch to edit
        material_dict: dict
            Materials dictionary (library + machine)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)
        self.lamination = lamination
        self.slot = lamination.slot
        self.is_notch = notch_obj is not None
        self.notch_obj = notch_obj
        self.material_dict = material_dict

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_H0.unit = "m"
        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_H0,
        ]
        for wid in wid_list:
            wid.setText("[" + gui_option.unit.get_m_name() + "]")

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_H0.setValue(self.slot.H0)
        if self.slot.is_H0_bore is None:
            self.slot.is_H0_bore = True  # Default to new schematics
        if self.slot.is_H0_bore:
            self.c_H0_bore.setCurrentIndex(0)
        else:
            self.c_H0_bore.setCurrentIndex(1)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.c_H0_bore.currentIndexChanged.connect(self.set_H0_bore)
        self.set_correct_schematics()

    def set_correct_schematics(self):
        """Update the schematics according to the current lamination/slot"""
        # Selecting the right image
        if not self.lamination.is_internal:
            # Use schematics on the external without magnet
            if not self.slot.is_H0_bore:
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotCirc_empty_ext_sta_old"])
                )
            else:
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotCirc_empty_ext_stator"])
                )
        else:
            # Use schematics on the inner without magnet
            if not self.slot.is_H0_bore:
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotCirc_empty_int_rot_old"])
                )
            else:
                self.img_slot.setPixmap(
                    QPixmap(pixmap_dict["SlotCirc_empty_int_rotor"])
                )

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : SlotCirc
            A SlotCirc object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : SlotCirc
            A SlotCirc object
        """
        self.slot.H0 = self.lf_H0.value()
        if self.check(self.lamination) is None:
            self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0_bore(self):
        """Change the definition of H0"""
        self.slot.is_H0_bore = self.c_H0_bore.currentIndex() == 0
        self.set_correct_schematics()
        if self.check(self.lamination) is None:
            self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lam: LamSlotMag
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.W0 is None:
            return "You must set W0 !"
        elif lam.slot.H0 is None:
            return "You must set H0 !"
        elif lam.slot.W0 <= 0:
            return "W0 must be higher than 0"
        elif lam.slot.H0 <= 0:
            return "H0 must be higher than 0"

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
