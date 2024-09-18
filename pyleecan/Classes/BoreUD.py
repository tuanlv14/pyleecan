# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/BoreUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/BoreUD
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
from .Bore import Bore

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.BoreUD.get_bore_line import get_bore_line
except ImportError as error:
    get_bore_line = error

try:
    from ..Methods.Machine.BoreUD.comp_periodicity_spatial import (
        comp_periodicity_spatial,
    )
except ImportError as error:
    comp_periodicity_spatial = error


from numpy import isnan
from ._check import InitUnKnowClassError


class BoreUD(Bore):
    """User Defined Bore shape"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.BoreUD.get_bore_line
    if isinstance(get_bore_line, ImportError):
        get_bore_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreUD method get_bore_line: " + str(get_bore_line)
                )
            )
        )
    else:
        get_bore_line = get_bore_line
    # cf Methods.Machine.BoreUD.comp_periodicity_spatial
    if isinstance(comp_periodicity_spatial, ImportError):
        comp_periodicity_spatial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreUD method comp_periodicity_spatial: "
                    + str(comp_periodicity_spatial)
                )
            )
        )
    else:
        comp_periodicity_spatial = comp_periodicity_spatial
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        line_list=-1,
        sym=1,
        name="",
        type_merge_slot=1,
        alpha=0,
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
            if "line_list" in list(init_dict.keys()):
                line_list = init_dict["line_list"]
            if "sym" in list(init_dict.keys()):
                sym = init_dict["sym"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "type_merge_slot" in list(init_dict.keys()):
                type_merge_slot = init_dict["type_merge_slot"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Set the properties (value check and convertion are done in setter)
        self.line_list = line_list
        self.sym = sym
        self.name = name
        # Call Bore init
        super(BoreUD, self).__init__(type_merge_slot=type_merge_slot, alpha=alpha)
        # The class is frozen (in Bore init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        BoreUD_str = ""
        # Get the properties inherited from Bore
        BoreUD_str += super(BoreUD, self).__str__()
        if len(self.line_list) == 0:
            BoreUD_str += "line_list = []" + linesep
        for ii in range(len(self.line_list)):
            tmp = (
                self.line_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            BoreUD_str += "line_list[" + str(ii) + "] =" + tmp + linesep + linesep
        BoreUD_str += "sym = " + str(self.sym) + linesep
        BoreUD_str += 'name = "' + str(self.name) + '"' + linesep
        return BoreUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Bore
        if not super(BoreUD, self).__eq__(other):
            return False
        if other.line_list != self.line_list:
            return False
        if other.sym != self.sym:
            return False
        if other.name != self.name:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Bore
        diff_list.extend(
            super(BoreUD, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.line_list is None and self.line_list is not None) or (
            other.line_list is not None and self.line_list is None
        ):
            diff_list.append(name + ".line_list None mismatch")
        elif self.line_list is None:
            pass
        elif len(other.line_list) != len(self.line_list):
            diff_list.append("len(" + name + ".line_list)")
        else:
            for ii in range(len(other.line_list)):
                diff_list.extend(
                    self.line_list[ii].compare(
                        other.line_list[ii],
                        name=name + ".line_list[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if other._sym != self._sym:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._sym) + ", other=" + str(other._sym) + ")"
                )
                diff_list.append(name + ".sym" + val_str)
            else:
                diff_list.append(name + ".sym")
        if other._name != self._name:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._name) + ", other=" + str(other._name) + ")"
                )
                diff_list.append(name + ".name" + val_str)
            else:
                diff_list.append(name + ".name")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Bore
        S += super(BoreUD, self).__sizeof__()
        if self.line_list is not None:
            for value in self.line_list:
                S += getsizeof(value)
        S += getsizeof(self.sym)
        S += getsizeof(self.name)
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

        # Get the properties inherited from Bore
        BoreUD_dict = super(BoreUD, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.line_list is None:
            BoreUD_dict["line_list"] = None
        else:
            BoreUD_dict["line_list"] = list()
            for obj in self.line_list:
                if obj is not None:
                    BoreUD_dict["line_list"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    BoreUD_dict["line_list"].append(None)
        BoreUD_dict["sym"] = self.sym
        BoreUD_dict["name"] = self.name
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        BoreUD_dict["__class__"] = "BoreUD"
        return BoreUD_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.line_list is None:
            line_list_val = None
        else:
            line_list_val = list()
            for obj in self.line_list:
                line_list_val.append(obj.copy())
        sym_val = self.sym
        name_val = self.name
        type_merge_slot_val = self.type_merge_slot
        alpha_val = self.alpha
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            line_list=line_list_val,
            sym=sym_val,
            name=name_val,
            type_merge_slot=type_merge_slot_val,
            alpha=alpha_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.line_list = None
        self.sym = None
        self.name = None
        # Set to None the properties inherited from Bore
        super(BoreUD, self)._set_None()

    def _get_line_list(self):
        """getter of line_list"""
        if self._line_list is not None:
            for obj in self._line_list:
                if obj is not None:
                    obj.parent = self
        return self._line_list

    def _set_line_list(self, value):
        """setter of line_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "line_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("line_list", value, "[Line]")
        self._line_list = value

    line_list = property(
        fget=_get_line_list,
        fset=_set_line_list,
        doc="""List of line to draw the full bore

        :Type: [Line]
        """,
    )

    def _get_sym(self):
        """getter of sym"""
        return self._sym

    def _set_sym(self, value):
        """setter of sym"""
        check_var("sym", value, "int", Vmin=1)
        self._sym = value

    sym = property(
        fget=_get_sym,
        fset=_set_sym,
        doc="""Symmetry factor (1= full machine, 2= half of the machine...)

        :Type: int
        :min: 1
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc="""Name of the bore (for save)

        :Type: str
        """,
    )
