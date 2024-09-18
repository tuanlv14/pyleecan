# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/CondType21.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/CondType21
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Conductor import Conductor

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.CondType21.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Machine.CondType21.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Machine.CondType21.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.CondType21.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from ..Methods.Machine.CondType21.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.CondType21.comp_width_wire import comp_width_wire
except ImportError as error:
    comp_width_wire = error

try:
    from ..Methods.Machine.CondType21.comp_height_wire import comp_height_wire
except ImportError as error:
    comp_height_wire = error

try:
    from ..Methods.Machine.CondType21.comp_nb_circumferential_wire import (
        comp_nb_circumferential_wire,
    )
except ImportError as error:
    comp_nb_circumferential_wire = error

try:
    from ..Methods.Machine.CondType21.comp_nb_radial_wire import comp_nb_radial_wire
except ImportError as error:
    comp_nb_radial_wire = error

try:
    from ..Methods.Machine.CondType21.is_round_wire import is_round_wire
except ImportError as error:
    is_round_wire = error


from numpy import isnan
from ._check import InitUnKnowClassError


class CondType21(Conductor):
    """single rectangular conductor \nhas to be used for LamSquirrelCages's conductor"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType21.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType21.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.CondType21.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.CondType21.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_width: " + str(comp_width)
                )
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Machine.CondType21.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType21 method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.CondType21.comp_width_wire
    if isinstance(comp_width_wire, ImportError):
        comp_width_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_width_wire: "
                    + str(comp_width_wire)
                )
            )
        )
    else:
        comp_width_wire = comp_width_wire
    # cf Methods.Machine.CondType21.comp_height_wire
    if isinstance(comp_height_wire, ImportError):
        comp_height_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_height_wire: "
                    + str(comp_height_wire)
                )
            )
        )
    else:
        comp_height_wire = comp_height_wire
    # cf Methods.Machine.CondType21.comp_nb_circumferential_wire
    if isinstance(comp_nb_circumferential_wire, ImportError):
        comp_nb_circumferential_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_nb_circumferential_wire: "
                    + str(comp_nb_circumferential_wire)
                )
            )
        )
    else:
        comp_nb_circumferential_wire = comp_nb_circumferential_wire
    # cf Methods.Machine.CondType21.comp_nb_radial_wire
    if isinstance(comp_nb_radial_wire, ImportError):
        comp_nb_radial_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method comp_nb_radial_wire: "
                    + str(comp_nb_radial_wire)
                )
            )
        )
    else:
        comp_nb_radial_wire = comp_nb_radial_wire
    # cf Methods.Machine.CondType21.is_round_wire
    if isinstance(is_round_wire, ImportError):
        is_round_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType21 method is_round_wire: " + str(is_round_wire)
                )
            )
        )
    else:
        is_round_wire = is_round_wire
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Hbar=0.01,
        Wbar=0.01,
        Wins=0,
        cond_mat=-1,
        ins_mat=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Hbar" in list(init_dict.keys()):
                Hbar = init_dict["Hbar"]
            if "Wbar" in list(init_dict.keys()):
                Wbar = init_dict["Wbar"]
            if "Wins" in list(init_dict.keys()):
                Wins = init_dict["Wins"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.Hbar = Hbar
        self.Wbar = Wbar
        self.Wins = Wins
        # Call Conductor init
        super(CondType21, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CondType21_str = ""
        # Get the properties inherited from Conductor
        CondType21_str += super(CondType21, self).__str__()
        CondType21_str += "Hbar = " + str(self.Hbar) + linesep
        CondType21_str += "Wbar = " + str(self.Wbar) + linesep
        CondType21_str += "Wins = " + str(self.Wins) + linesep
        return CondType21_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType21, self).__eq__(other):
            return False
        if other.Hbar != self.Hbar:
            return False
        if other.Wbar != self.Wbar:
            return False
        if other.Wins != self.Wins:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Conductor
        diff_list.extend(
            super(CondType21, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Hbar is not None
            and self._Hbar is not None
            and isnan(other._Hbar)
            and isnan(self._Hbar)
        ):
            pass
        elif other._Hbar != self._Hbar:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Hbar) + ", other=" + str(other._Hbar) + ")"
                )
                diff_list.append(name + ".Hbar" + val_str)
            else:
                diff_list.append(name + ".Hbar")
        if (
            other._Wbar is not None
            and self._Wbar is not None
            and isnan(other._Wbar)
            and isnan(self._Wbar)
        ):
            pass
        elif other._Wbar != self._Wbar:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Wbar) + ", other=" + str(other._Wbar) + ")"
                )
                diff_list.append(name + ".Wbar" + val_str)
            else:
                diff_list.append(name + ".Wbar")
        if (
            other._Wins is not None
            and self._Wins is not None
            and isnan(other._Wins)
            and isnan(self._Wins)
        ):
            pass
        elif other._Wins != self._Wins:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Wins) + ", other=" + str(other._Wins) + ")"
                )
                diff_list.append(name + ".Wins" + val_str)
            else:
                diff_list.append(name + ".Wins")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Conductor
        S += super(CondType21, self).__sizeof__()
        S += getsizeof(self.Hbar)
        S += getsizeof(self.Wbar)
        S += getsizeof(self.Wins)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Conductor
        CondType21_dict = super(CondType21, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        CondType21_dict["Hbar"] = self.Hbar
        CondType21_dict["Wbar"] = self.Wbar
        CondType21_dict["Wins"] = self.Wins
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        CondType21_dict["__class__"] = "CondType21"
        return CondType21_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        Hbar_val = self.Hbar
        Wbar_val = self.Wbar
        Wins_val = self.Wins
        if self.cond_mat is None:
            cond_mat_val = None
        else:
            cond_mat_val = self.cond_mat.copy()
        if self.ins_mat is None:
            ins_mat_val = None
        else:
            ins_mat_val = self.ins_mat.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            Hbar=Hbar_val,
            Wbar=Wbar_val,
            Wins=Wins_val,
            cond_mat=cond_mat_val,
            ins_mat=ins_mat_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Hbar = None
        self.Wbar = None
        self.Wins = None
        # Set to None the properties inherited from Conductor
        super(CondType21, self)._set_None()

    def _get_Hbar(self):
        """getter of Hbar"""
        return self._Hbar

    def _set_Hbar(self, value):
        """setter of Hbar"""
        check_var("Hbar", value, "float", Vmin=0)
        self._Hbar = value

    Hbar = property(
        fget=_get_Hbar,
        fset=_set_Hbar,
        doc="""Bar height

        :Type: float
        :min: 0
        """,
    )

    def _get_Wbar(self):
        """getter of Wbar"""
        return self._Wbar

    def _set_Wbar(self, value):
        """setter of Wbar"""
        check_var("Wbar", value, "float", Vmin=0)
        self._Wbar = value

    Wbar = property(
        fget=_get_Wbar,
        fset=_set_Wbar,
        doc="""Bar width

        :Type: float
        :min: 0
        """,
    )

    def _get_Wins(self):
        """getter of Wins"""
        return self._Wins

    def _set_Wins(self, value):
        """setter of Wins"""
        check_var("Wins", value, "float", Vmin=0)
        self._Wins = value

    Wins = property(
        fget=_get_Wins,
        fset=_set_Wins,
        doc="""Width of insulation

        :Type: float
        :min: 0
        """,
    )
