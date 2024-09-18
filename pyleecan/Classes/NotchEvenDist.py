# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/NotchEvenDist.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/NotchEvenDist
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
from .Notch import Notch

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.NotchEvenDist.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.NotchEvenDist.comp_periodicity_spatial import (
        comp_periodicity_spatial,
    )
except ImportError as error:
    comp_periodicity_spatial = error

try:
    from ..Methods.Machine.NotchEvenDist.get_notch_desc_list import get_notch_desc_list
except ImportError as error:
    get_notch_desc_list = error

try:
    from ..Methods.Machine.NotchEvenDist.build_geometry_key import build_geometry_key
except ImportError as error:
    build_geometry_key = error

try:
    from ..Methods.Machine.NotchEvenDist.get_key_Ox_radius import get_key_Ox_radius
except ImportError as error:
    get_key_Ox_radius = error


from numpy import isnan
from ._check import InitUnKnowClassError


class NotchEvenDist(Notch):
    """Class for evenly distributed notches (according to Zs)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.NotchEvenDist.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.NotchEvenDist.comp_periodicity_spatial
    if isinstance(comp_periodicity_spatial, ImportError):
        comp_periodicity_spatial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method comp_periodicity_spatial: "
                    + str(comp_periodicity_spatial)
                )
            )
        )
    else:
        comp_periodicity_spatial = comp_periodicity_spatial
    # cf Methods.Machine.NotchEvenDist.get_notch_desc_list
    if isinstance(get_notch_desc_list, ImportError):
        get_notch_desc_list = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method get_notch_desc_list: "
                    + str(get_notch_desc_list)
                )
            )
        )
    else:
        get_notch_desc_list = get_notch_desc_list
    # cf Methods.Machine.NotchEvenDist.build_geometry_key
    if isinstance(build_geometry_key, ImportError):
        build_geometry_key = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method build_geometry_key: "
                    + str(build_geometry_key)
                )
            )
        )
    else:
        build_geometry_key = build_geometry_key
    # cf Methods.Machine.NotchEvenDist.get_key_Ox_radius
    if isinstance(get_key_Ox_radius, ImportError):
        get_key_Ox_radius = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use NotchEvenDist method get_key_Ox_radius: "
                    + str(get_key_Ox_radius)
                )
            )
        )
    else:
        get_key_Ox_radius = get_key_Ox_radius
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, alpha=0, notch_shape=-1, key_mat=None, init_dict=None, init_str=None
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
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
            if "notch_shape" in list(init_dict.keys()):
                notch_shape = init_dict["notch_shape"]
            if "key_mat" in list(init_dict.keys()):
                key_mat = init_dict["key_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.alpha = alpha
        self.notch_shape = notch_shape
        # Call Notch init
        super(NotchEvenDist, self).__init__(key_mat=key_mat)
        # The class is frozen (in Notch init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        NotchEvenDist_str = ""
        # Get the properties inherited from Notch
        NotchEvenDist_str += super(NotchEvenDist, self).__str__()
        NotchEvenDist_str += "alpha = " + str(self.alpha) + linesep
        if self.notch_shape is not None:
            tmp = (
                self.notch_shape.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            NotchEvenDist_str += "notch_shape = " + tmp
        else:
            NotchEvenDist_str += "notch_shape = None" + linesep + linesep
        return NotchEvenDist_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Notch
        if not super(NotchEvenDist, self).__eq__(other):
            return False
        if other.alpha != self.alpha:
            return False
        if other.notch_shape != self.notch_shape:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Notch
        diff_list.extend(
            super(NotchEvenDist, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._alpha is not None
            and self._alpha is not None
            and isnan(other._alpha)
            and isnan(self._alpha)
        ):
            pass
        elif other._alpha != self._alpha:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._alpha) + ", other=" + str(other._alpha) + ")"
                )
                diff_list.append(name + ".alpha" + val_str)
            else:
                diff_list.append(name + ".alpha")
        if (other.notch_shape is None and self.notch_shape is not None) or (
            other.notch_shape is not None and self.notch_shape is None
        ):
            diff_list.append(name + ".notch_shape None mismatch")
        elif self.notch_shape is not None:
            diff_list.extend(
                self.notch_shape.compare(
                    other.notch_shape,
                    name=name + ".notch_shape",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Notch
        S += super(NotchEvenDist, self).__sizeof__()
        S += getsizeof(self.alpha)
        S += getsizeof(self.notch_shape)
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

        # Get the properties inherited from Notch
        NotchEvenDist_dict = super(NotchEvenDist, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        NotchEvenDist_dict["alpha"] = self.alpha
        if self.notch_shape is None:
            NotchEvenDist_dict["notch_shape"] = None
        else:
            NotchEvenDist_dict["notch_shape"] = self.notch_shape.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        NotchEvenDist_dict["__class__"] = "NotchEvenDist"
        return NotchEvenDist_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        alpha_val = self.alpha
        if self.notch_shape is None:
            notch_shape_val = None
        else:
            notch_shape_val = self.notch_shape.copy()
        if self.key_mat is None:
            key_mat_val = None
        else:
            key_mat_val = self.key_mat.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            alpha=alpha_val, notch_shape=notch_shape_val, key_mat=key_mat_val
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.alpha = None
        if self.notch_shape is not None:
            self.notch_shape._set_None()
        # Set to None the properties inherited from Notch
        super(NotchEvenDist, self)._set_None()

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float")
        self._alpha = value

    alpha = property(
        fget=_get_alpha,
        fset=_set_alpha,
        doc="""angular positon of the first notch (0 is middle of first tooth)

        :Type: float
        """,
    )

    def _get_notch_shape(self):
        """getter of notch_shape"""
        return self._notch_shape

    def _set_notch_shape(self, value):
        """setter of notch_shape"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "notch_shape"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Slot = import_class("pyleecan.Classes", "Slot", "notch_shape")
            value = Slot()
        check_var("notch_shape", value, "Slot")
        self._notch_shape = value

        if self._notch_shape is not None:
            self._notch_shape.parent = self

    notch_shape = property(
        fget=_get_notch_shape,
        fset=_set_notch_shape,
        doc="""Shape of the Notch

        :Type: Slot
        """,
    )
