# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/EndWindingCirc.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/EndWindingCirc
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
from .EndWinding import EndWinding

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.EndWindingCirc.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Machine.EndWindingCirc.comp_inductance import comp_inductance
except ImportError as error:
    comp_inductance = error


from numpy import isnan
from ._check import InitUnKnowClassError


class EndWindingCirc(EndWinding):
    """Class of the machine's end winding assuming a circular shape"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.EndWindingCirc.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EndWindingCirc method comp_length: " + str(comp_length)
                )
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Machine.EndWindingCirc.comp_inductance
    if isinstance(comp_inductance, ImportError):
        comp_inductance = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EndWindingCirc method comp_inductance: "
                    + str(comp_inductance)
                )
            )
        )
    else:
        comp_inductance = comp_inductance
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, coil_pitch=None, Lew_enforced=0, init_dict=None, init_str=None):
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
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "Lew_enforced" in list(init_dict.keys()):
                Lew_enforced = init_dict["Lew_enforced"]
        # Set the properties (value check and convertion are done in setter)
        self.coil_pitch = coil_pitch
        # Call EndWinding init
        super(EndWindingCirc, self).__init__(Lew_enforced=Lew_enforced)
        # The class is frozen (in EndWinding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EndWindingCirc_str = ""
        # Get the properties inherited from EndWinding
        EndWindingCirc_str += super(EndWindingCirc, self).__str__()
        EndWindingCirc_str += "coil_pitch = " + str(self.coil_pitch) + linesep
        return EndWindingCirc_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EndWinding
        if not super(EndWindingCirc, self).__eq__(other):
            return False
        if other.coil_pitch != self.coil_pitch:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from EndWinding
        diff_list.extend(
            super(EndWindingCirc, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._coil_pitch is not None
            and self._coil_pitch is not None
            and isnan(other._coil_pitch)
            and isnan(self._coil_pitch)
        ):
            pass
        elif other._coil_pitch != self._coil_pitch:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._coil_pitch)
                    + ", other="
                    + str(other._coil_pitch)
                    + ")"
                )
                diff_list.append(name + ".coil_pitch" + val_str)
            else:
                diff_list.append(name + ".coil_pitch")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from EndWinding
        S += super(EndWindingCirc, self).__sizeof__()
        S += getsizeof(self.coil_pitch)
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

        # Get the properties inherited from EndWinding
        EndWindingCirc_dict = super(EndWindingCirc, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        EndWindingCirc_dict["coil_pitch"] = self.coil_pitch
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EndWindingCirc_dict["__class__"] = "EndWindingCirc"
        return EndWindingCirc_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        coil_pitch_val = self.coil_pitch
        Lew_enforced_val = self.Lew_enforced
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(coil_pitch=coil_pitch_val, Lew_enforced=Lew_enforced_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.coil_pitch = None
        # Set to None the properties inherited from EndWinding
        super(EndWindingCirc, self)._set_None()

    def _get_coil_pitch(self):
        """getter of coil_pitch"""
        return self._coil_pitch

    def _set_coil_pitch(self, value):
        """setter of coil_pitch"""
        check_var("coil_pitch", value, "float")
        self._coil_pitch = value

    coil_pitch = property(
        fget=_get_coil_pitch,
        fset=_set_coil_pitch,
        doc="""effective coil pitch (override) for length calculation

        :Type: float
        """,
    )
