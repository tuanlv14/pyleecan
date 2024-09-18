# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotW13.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotW13
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
from .Slot import Slot

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.SlotW13._comp_line_dict import _comp_line_dict
except ImportError as error:
    _comp_line_dict = error

try:
    from ..Methods.Slot.SlotW13._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotW13.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotW13.build_geometry_active import build_geometry_active
except ImportError as error:
    build_geometry_active = error

try:
    from ..Methods.Slot.SlotW13.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotW13.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotW13.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotW13.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.SlotW13.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotW13.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Slot.SlotW13.comp_surface_opening import comp_surface_opening
except ImportError as error:
    comp_surface_opening = error

try:
    from ..Methods.Slot.SlotW13.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotW13.get_surface_opening import get_surface_opening
except ImportError as error:
    get_surface_opening = error

try:
    from ..Methods.Slot.SlotW13.get_H1 import get_H1
except ImportError as error:
    get_H1 = error

try:
    from ..Methods.Slot.SlotW13.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error


from numpy import isnan
from ._check import InitUnKnowClassError


class SlotW13(Slot):
    """Open Rectangular or trapezoidal slot with wedge"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotW13._comp_line_dict
    if isinstance(_comp_line_dict, ImportError):
        _comp_line_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method _comp_line_dict: " + str(_comp_line_dict)
                )
            )
        )
    else:
        _comp_line_dict = _comp_line_dict
    # cf Methods.Slot.SlotW13._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotW13.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotW13.build_geometry_active
    if isinstance(build_geometry_active, ImportError):
        build_geometry_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method build_geometry_active: "
                    + str(build_geometry_active)
                )
            )
        )
    else:
        build_geometry_active = build_geometry_active
    # cf Methods.Slot.SlotW13.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW13 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotW13.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotW13.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW13 method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotW13.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.SlotW13.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotW13.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Slot.SlotW13.comp_surface_opening
    if isinstance(comp_surface_opening, ImportError):
        comp_surface_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method comp_surface_opening: "
                    + str(comp_surface_opening)
                )
            )
        )
    else:
        comp_surface_opening = comp_surface_opening
    # cf Methods.Slot.SlotW13.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotW13.get_surface_opening
    if isinstance(get_surface_opening, ImportError):
        get_surface_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method get_surface_opening: "
                    + str(get_surface_opening)
                )
            )
        )
    else:
        get_surface_opening = get_surface_opening
    # cf Methods.Slot.SlotW13.get_H1
    if isinstance(get_H1, ImportError):
        get_H1 = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotW13 method get_H1: " + str(get_H1))
            )
        )
    else:
        get_H1 = get_H1
    # cf Methods.Slot.SlotW13.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotW13 method plot_schematics: " + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W0=0.0122,
        H0=0.001,
        H1=0.0015,
        W1=0.014,
        H2=0.0325,
        W2=0.0122,
        W3=0.0122,
        H1_is_rad=False,
        Zs=36,
        wedge_mat=None,
        is_bore=True,
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
            if "W0" in list(init_dict.keys()):
                W0 = init_dict["W0"]
            if "H0" in list(init_dict.keys()):
                H0 = init_dict["H0"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "W3" in list(init_dict.keys()):
                W3 = init_dict["W3"]
            if "H1_is_rad" in list(init_dict.keys()):
                H1_is_rad = init_dict["H1_is_rad"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
            if "is_bore" in list(init_dict.keys()):
                is_bore = init_dict["is_bore"]
        # Set the properties (value check and convertion are done in setter)
        self.W0 = W0
        self.H0 = H0
        self.H1 = H1
        self.W1 = W1
        self.H2 = H2
        self.W2 = W2
        self.W3 = W3
        self.H1_is_rad = H1_is_rad
        # Call Slot init
        super(SlotW13, self).__init__(Zs=Zs, wedge_mat=wedge_mat, is_bore=is_bore)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotW13_str = ""
        # Get the properties inherited from Slot
        SlotW13_str += super(SlotW13, self).__str__()
        SlotW13_str += "W0 = " + str(self.W0) + linesep
        SlotW13_str += "H0 = " + str(self.H0) + linesep
        SlotW13_str += "H1 = " + str(self.H1) + linesep
        SlotW13_str += "W1 = " + str(self.W1) + linesep
        SlotW13_str += "H2 = " + str(self.H2) + linesep
        SlotW13_str += "W2 = " + str(self.W2) + linesep
        SlotW13_str += "W3 = " + str(self.W3) + linesep
        SlotW13_str += "H1_is_rad = " + str(self.H1_is_rad) + linesep
        return SlotW13_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotW13, self).__eq__(other):
            return False
        if other.W0 != self.W0:
            return False
        if other.H0 != self.H0:
            return False
        if other.H1 != self.H1:
            return False
        if other.W1 != self.W1:
            return False
        if other.H2 != self.H2:
            return False
        if other.W2 != self.W2:
            return False
        if other.W3 != self.W3:
            return False
        if other.H1_is_rad != self.H1_is_rad:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Slot
        diff_list.extend(
            super(SlotW13, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._W0 is not None
            and self._W0 is not None
            and isnan(other._W0)
            and isnan(self._W0)
        ):
            pass
        elif other._W0 != self._W0:
            if is_add_value:
                val_str = " (self=" + str(self._W0) + ", other=" + str(other._W0) + ")"
                diff_list.append(name + ".W0" + val_str)
            else:
                diff_list.append(name + ".W0")
        if (
            other._H0 is not None
            and self._H0 is not None
            and isnan(other._H0)
            and isnan(self._H0)
        ):
            pass
        elif other._H0 != self._H0:
            if is_add_value:
                val_str = " (self=" + str(self._H0) + ", other=" + str(other._H0) + ")"
                diff_list.append(name + ".H0" + val_str)
            else:
                diff_list.append(name + ".H0")
        if (
            other._H1 is not None
            and self._H1 is not None
            and isnan(other._H1)
            and isnan(self._H1)
        ):
            pass
        elif other._H1 != self._H1:
            if is_add_value:
                val_str = " (self=" + str(self._H1) + ", other=" + str(other._H1) + ")"
                diff_list.append(name + ".H1" + val_str)
            else:
                diff_list.append(name + ".H1")
        if (
            other._W1 is not None
            and self._W1 is not None
            and isnan(other._W1)
            and isnan(self._W1)
        ):
            pass
        elif other._W1 != self._W1:
            if is_add_value:
                val_str = " (self=" + str(self._W1) + ", other=" + str(other._W1) + ")"
                diff_list.append(name + ".W1" + val_str)
            else:
                diff_list.append(name + ".W1")
        if (
            other._H2 is not None
            and self._H2 is not None
            and isnan(other._H2)
            and isnan(self._H2)
        ):
            pass
        elif other._H2 != self._H2:
            if is_add_value:
                val_str = " (self=" + str(self._H2) + ", other=" + str(other._H2) + ")"
                diff_list.append(name + ".H2" + val_str)
            else:
                diff_list.append(name + ".H2")
        if (
            other._W2 is not None
            and self._W2 is not None
            and isnan(other._W2)
            and isnan(self._W2)
        ):
            pass
        elif other._W2 != self._W2:
            if is_add_value:
                val_str = " (self=" + str(self._W2) + ", other=" + str(other._W2) + ")"
                diff_list.append(name + ".W2" + val_str)
            else:
                diff_list.append(name + ".W2")
        if (
            other._W3 is not None
            and self._W3 is not None
            and isnan(other._W3)
            and isnan(self._W3)
        ):
            pass
        elif other._W3 != self._W3:
            if is_add_value:
                val_str = " (self=" + str(self._W3) + ", other=" + str(other._W3) + ")"
                diff_list.append(name + ".W3" + val_str)
            else:
                diff_list.append(name + ".W3")
        if other._H1_is_rad != self._H1_is_rad:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._H1_is_rad)
                    + ", other="
                    + str(other._H1_is_rad)
                    + ")"
                )
                diff_list.append(name + ".H1_is_rad" + val_str)
            else:
                diff_list.append(name + ".H1_is_rad")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotW13, self).__sizeof__()
        S += getsizeof(self.W0)
        S += getsizeof(self.H0)
        S += getsizeof(self.H1)
        S += getsizeof(self.W1)
        S += getsizeof(self.H2)
        S += getsizeof(self.W2)
        S += getsizeof(self.W3)
        S += getsizeof(self.H1_is_rad)
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

        # Get the properties inherited from Slot
        SlotW13_dict = super(SlotW13, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        SlotW13_dict["W0"] = self.W0
        SlotW13_dict["H0"] = self.H0
        SlotW13_dict["H1"] = self.H1
        SlotW13_dict["W1"] = self.W1
        SlotW13_dict["H2"] = self.H2
        SlotW13_dict["W2"] = self.W2
        SlotW13_dict["W3"] = self.W3
        SlotW13_dict["H1_is_rad"] = self.H1_is_rad
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotW13_dict["__class__"] = "SlotW13"
        return SlotW13_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        W0_val = self.W0
        H0_val = self.H0
        H1_val = self.H1
        W1_val = self.W1
        H2_val = self.H2
        W2_val = self.W2
        W3_val = self.W3
        H1_is_rad_val = self.H1_is_rad
        Zs_val = self.Zs
        if self.wedge_mat is None:
            wedge_mat_val = None
        else:
            wedge_mat_val = self.wedge_mat.copy()
        is_bore_val = self.is_bore
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            W0=W0_val,
            H0=H0_val,
            H1=H1_val,
            W1=W1_val,
            H2=H2_val,
            W2=W2_val,
            W3=W3_val,
            H1_is_rad=H1_is_rad_val,
            Zs=Zs_val,
            wedge_mat=wedge_mat_val,
            is_bore=is_bore_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W0 = None
        self.H0 = None
        self.H1 = None
        self.W1 = None
        self.H2 = None
        self.W2 = None
        self.W3 = None
        self.H1_is_rad = None
        # Set to None the properties inherited from Slot
        super(SlotW13, self)._set_None()

    def _get_W0(self):
        """getter of W0"""
        return self._W0

    def _set_W0(self, value):
        """setter of W0"""
        check_var("W0", value, "float", Vmin=0)
        self._W0 = value

    W0 = property(
        fget=_get_W0,
        fset=_set_W0,
        doc="""Slot isthmus width.

        :Type: float
        :min: 0
        """,
    )

    def _get_H0(self):
        """getter of H0"""
        return self._H0

    def _set_H0(self, value):
        """setter of H0"""
        check_var("H0", value, "float", Vmin=0)
        self._H0 = value

    H0 = property(
        fget=_get_H0,
        fset=_set_H0,
        doc="""Slot isthmus height.

        :Type: float
        :min: 0
        """,
    )

    def _get_H1(self):
        """getter of H1"""
        return self._H1

    def _set_H1(self, value):
        """setter of H1"""
        check_var("H1", value, "float", Vmin=0)
        self._H1 = value

    H1 = property(
        fget=_get_H1,
        fset=_set_H1,
        doc="""Slot wedge radial height or wedge angle .

        :Type: float
        :min: 0
        """,
    )

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float", Vmin=0)
        self._W1 = value

    W1 = property(
        fget=_get_W1,
        fset=_set_W1,
        doc="""Slot wedge width.

        :Type: float
        :min: 0
        """,
    )

    def _get_H2(self):
        """getter of H2"""
        return self._H2

    def _set_H2(self, value):
        """setter of H2"""
        check_var("H2", value, "float", Vmin=0)
        self._H2 = value

    H2 = property(
        fget=_get_H2,
        fset=_set_H2,
        doc="""Slot height below wedge 

        :Type: float
        :min: 0
        """,
    )

    def _get_W2(self):
        """getter of W2"""
        return self._W2

    def _set_W2(self, value):
        """setter of W2"""
        check_var("W2", value, "float", Vmin=0)
        self._W2 = value

    W2 = property(
        fget=_get_W2,
        fset=_set_W2,
        doc="""Slot width below wedge 

        :Type: float
        :min: 0
        """,
    )

    def _get_W3(self):
        """getter of W3"""
        return self._W3

    def _set_W3(self, value):
        """setter of W3"""
        check_var("W3", value, "float", Vmin=0)
        self._W3 = value

    W3 = property(
        fget=_get_W3,
        fset=_set_W3,
        doc="""Slot bottom width.

        :Type: float
        :min: 0
        """,
    )

    def _get_H1_is_rad(self):
        """getter of H1_is_rad"""
        return self._H1_is_rad

    def _set_H1_is_rad(self, value):
        """setter of H1_is_rad"""
        check_var("H1_is_rad", value, "bool")
        self._H1_is_rad = value

    H1_is_rad = property(
        fget=_get_H1_is_rad,
        fset=_set_H1_is_rad,
        doc="""H1 unit, 0 for m, 1 for rad

        :Type: bool
        """,
    )
