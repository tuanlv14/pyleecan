# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/SlotDC.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/SlotDC
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
    from ..Methods.Slot.SlotDC._comp_point_coordinate import _comp_point_coordinate
except ImportError as error:
    _comp_point_coordinate = error

try:
    from ..Methods.Slot.SlotDC.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.SlotDC.get_surface_active import get_surface_active
except ImportError as error:
    get_surface_active = error

try:
    from ..Methods.Slot.SlotDC.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.SlotDC.comp_angle_opening import comp_angle_opening
except ImportError as error:
    comp_angle_opening = error

try:
    from ..Methods.Slot.SlotDC.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Slot.SlotDC.comp_height_active import comp_height_active
except ImportError as error:
    comp_height_active = error

try:
    from ..Methods.Slot.SlotDC.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.SlotDC.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error


from numpy import isnan
from ._check import InitUnKnowClassError


class SlotDC(Slot):
    """Slot with two rods (for double squirrel cage)"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.SlotDC._comp_point_coordinate
    if isinstance(_comp_point_coordinate, ImportError):
        _comp_point_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method _comp_point_coordinate: "
                    + str(_comp_point_coordinate)
                )
            )
        )
    else:
        _comp_point_coordinate = _comp_point_coordinate
    # cf Methods.Slot.SlotDC.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.SlotDC.get_surface_active
    if isinstance(get_surface_active, ImportError):
        get_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method get_surface_active: "
                    + str(get_surface_active)
                )
            )
        )
    else:
        get_surface_active = get_surface_active
    # cf Methods.Slot.SlotDC.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotDC method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.SlotDC.comp_angle_opening
    if isinstance(comp_angle_opening, ImportError):
        comp_angle_opening = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method comp_angle_opening: "
                    + str(comp_angle_opening)
                )
            )
        )
    else:
        comp_angle_opening = comp_angle_opening
    # cf Methods.Slot.SlotDC.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use SlotDC method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Slot.SlotDC.comp_height_active
    if isinstance(comp_height_active, ImportError):
        comp_height_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method comp_height_active: "
                    + str(comp_height_active)
                )
            )
        )
    else:
        comp_height_active = comp_height_active
    # cf Methods.Slot.SlotDC.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.SlotDC.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use SlotDC method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        W1=0.0122,
        H1=0.0122,
        D1=0.001,
        W2=0.0122,
        H2=0.001,
        D2=0.001,
        H3=0.001,
        R3=0.001,
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
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "H1" in list(init_dict.keys()):
                H1 = init_dict["H1"]
            if "D1" in list(init_dict.keys()):
                D1 = init_dict["D1"]
            if "W2" in list(init_dict.keys()):
                W2 = init_dict["W2"]
            if "H2" in list(init_dict.keys()):
                H2 = init_dict["H2"]
            if "D2" in list(init_dict.keys()):
                D2 = init_dict["D2"]
            if "H3" in list(init_dict.keys()):
                H3 = init_dict["H3"]
            if "R3" in list(init_dict.keys()):
                R3 = init_dict["R3"]
            if "Zs" in list(init_dict.keys()):
                Zs = init_dict["Zs"]
            if "wedge_mat" in list(init_dict.keys()):
                wedge_mat = init_dict["wedge_mat"]
            if "is_bore" in list(init_dict.keys()):
                is_bore = init_dict["is_bore"]
        # Set the properties (value check and convertion are done in setter)
        self.W1 = W1
        self.H1 = H1
        self.D1 = D1
        self.W2 = W2
        self.H2 = H2
        self.D2 = D2
        self.H3 = H3
        self.R3 = R3
        # Call Slot init
        super(SlotDC, self).__init__(Zs=Zs, wedge_mat=wedge_mat, is_bore=is_bore)
        # The class is frozen (in Slot init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        SlotDC_str = ""
        # Get the properties inherited from Slot
        SlotDC_str += super(SlotDC, self).__str__()
        SlotDC_str += "W1 = " + str(self.W1) + linesep
        SlotDC_str += "H1 = " + str(self.H1) + linesep
        SlotDC_str += "D1 = " + str(self.D1) + linesep
        SlotDC_str += "W2 = " + str(self.W2) + linesep
        SlotDC_str += "H2 = " + str(self.H2) + linesep
        SlotDC_str += "D2 = " + str(self.D2) + linesep
        SlotDC_str += "H3 = " + str(self.H3) + linesep
        SlotDC_str += "R3 = " + str(self.R3) + linesep
        return SlotDC_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Slot
        if not super(SlotDC, self).__eq__(other):
            return False
        if other.W1 != self.W1:
            return False
        if other.H1 != self.H1:
            return False
        if other.D1 != self.D1:
            return False
        if other.W2 != self.W2:
            return False
        if other.H2 != self.H2:
            return False
        if other.D2 != self.D2:
            return False
        if other.H3 != self.H3:
            return False
        if other.R3 != self.R3:
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
            super(SlotDC, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
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
            other._D1 is not None
            and self._D1 is not None
            and isnan(other._D1)
            and isnan(self._D1)
        ):
            pass
        elif other._D1 != self._D1:
            if is_add_value:
                val_str = " (self=" + str(self._D1) + ", other=" + str(other._D1) + ")"
                diff_list.append(name + ".D1" + val_str)
            else:
                diff_list.append(name + ".D1")
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
            other._D2 is not None
            and self._D2 is not None
            and isnan(other._D2)
            and isnan(self._D2)
        ):
            pass
        elif other._D2 != self._D2:
            if is_add_value:
                val_str = " (self=" + str(self._D2) + ", other=" + str(other._D2) + ")"
                diff_list.append(name + ".D2" + val_str)
            else:
                diff_list.append(name + ".D2")
        if (
            other._H3 is not None
            and self._H3 is not None
            and isnan(other._H3)
            and isnan(self._H3)
        ):
            pass
        elif other._H3 != self._H3:
            if is_add_value:
                val_str = " (self=" + str(self._H3) + ", other=" + str(other._H3) + ")"
                diff_list.append(name + ".H3" + val_str)
            else:
                diff_list.append(name + ".H3")
        if (
            other._R3 is not None
            and self._R3 is not None
            and isnan(other._R3)
            and isnan(self._R3)
        ):
            pass
        elif other._R3 != self._R3:
            if is_add_value:
                val_str = " (self=" + str(self._R3) + ", other=" + str(other._R3) + ")"
                diff_list.append(name + ".R3" + val_str)
            else:
                diff_list.append(name + ".R3")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Slot
        S += super(SlotDC, self).__sizeof__()
        S += getsizeof(self.W1)
        S += getsizeof(self.H1)
        S += getsizeof(self.D1)
        S += getsizeof(self.W2)
        S += getsizeof(self.H2)
        S += getsizeof(self.D2)
        S += getsizeof(self.H3)
        S += getsizeof(self.R3)
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
        SlotDC_dict = super(SlotDC, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        SlotDC_dict["W1"] = self.W1
        SlotDC_dict["H1"] = self.H1
        SlotDC_dict["D1"] = self.D1
        SlotDC_dict["W2"] = self.W2
        SlotDC_dict["H2"] = self.H2
        SlotDC_dict["D2"] = self.D2
        SlotDC_dict["H3"] = self.H3
        SlotDC_dict["R3"] = self.R3
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        SlotDC_dict["__class__"] = "SlotDC"
        return SlotDC_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        W1_val = self.W1
        H1_val = self.H1
        D1_val = self.D1
        W2_val = self.W2
        H2_val = self.H2
        D2_val = self.D2
        H3_val = self.H3
        R3_val = self.R3
        Zs_val = self.Zs
        if self.wedge_mat is None:
            wedge_mat_val = None
        else:
            wedge_mat_val = self.wedge_mat.copy()
        is_bore_val = self.is_bore
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            W1=W1_val,
            H1=H1_val,
            D1=D1_val,
            W2=W2_val,
            H2=H2_val,
            D2=D2_val,
            H3=H3_val,
            R3=R3_val,
            Zs=Zs_val,
            wedge_mat=wedge_mat_val,
            is_bore=is_bore_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.W1 = None
        self.H1 = None
        self.D1 = None
        self.W2 = None
        self.H2 = None
        self.D2 = None
        self.H3 = None
        self.R3 = None
        # Set to None the properties inherited from Slot
        super(SlotDC, self)._set_None()

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
        doc="""Slot isthmus width.

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
        doc="""Distance upper rod center to bore

        :Type: float
        :min: 0
        """,
    )

    def _get_D1(self):
        """getter of D1"""
        return self._D1

    def _set_D1(self, value):
        """setter of D1"""
        check_var("D1", value, "float", Vmin=0)
        self._D1 = value

    D1 = property(
        fget=_get_D1,
        fset=_set_D1,
        doc="""Diameter upper rod

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
        doc="""Middle connection width

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
        doc="""Height between the first and second center

        :Type: float
        :min: 0
        """,
    )

    def _get_D2(self):
        """getter of D2"""
        return self._D2

    def _set_D2(self, value):
        """setter of D2"""
        check_var("D2", value, "float", Vmin=0)
        self._D2 = value

    D2 = property(
        fget=_get_D2,
        fset=_set_D2,
        doc="""Diameter upper section lower rod

        :Type: float
        :min: 0
        """,
    )

    def _get_H3(self):
        """getter of H3"""
        return self._H3

    def _set_H3(self, value):
        """setter of H3"""
        check_var("H3", value, "float", Vmin=0)
        self._H3 = value

    H3 = property(
        fget=_get_H3,
        fset=_set_H3,
        doc="""Length of lower rod

        :Type: float
        :min: 0
        """,
    )

    def _get_R3(self):
        """getter of R3"""
        return self._R3

    def _set_R3(self, value):
        """setter of R3"""
        check_var("R3", value, "float", Vmin=0)
        self._R3 = value

    R3 = property(
        fget=_get_R3,
        fset=_set_R3,
        doc="""Radius lower section lower rod

        :Type: float
        :min: 0
        """,
    )
