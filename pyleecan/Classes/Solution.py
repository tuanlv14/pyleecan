# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Solution.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/Solution
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
from ._frozen import FrozenClass

from numpy import isnan
from ._check import InitUnKnowClassError


class Solution(FrozenClass):
    """Abstract class for solution related classes."""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_element="triangle",
        label=None,
        dimension=2,
        unit="",
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
            if "type_element" in list(init_dict.keys()):
                type_element = init_dict["type_element"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.type_element = type_element
        self.label = label
        self.dimension = dimension
        self.unit = unit

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Solution_str = ""
        if self.parent is None:
            Solution_str += "parent = None " + linesep
        else:
            Solution_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Solution_str += 'type_element = "' + str(self.type_element) + '"' + linesep
        Solution_str += 'label = "' + str(self.label) + '"' + linesep
        Solution_str += "dimension = " + str(self.dimension) + linesep
        Solution_str += 'unit = "' + str(self.unit) + '"' + linesep
        return Solution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type_element != self.type_element:
            return False
        if other.label != self.label:
            return False
        if other.dimension != self.dimension:
            return False
        if other.unit != self.unit:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._type_element != self._type_element:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_element)
                    + ", other="
                    + str(other._type_element)
                    + ")"
                )
                diff_list.append(name + ".type_element" + val_str)
            else:
                diff_list.append(name + ".type_element")
        if other._label != self._label:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._label) + ", other=" + str(other._label) + ")"
                )
                diff_list.append(name + ".label" + val_str)
            else:
                diff_list.append(name + ".label")
        if other._dimension != self._dimension:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._dimension)
                    + ", other="
                    + str(other._dimension)
                    + ")"
                )
                diff_list.append(name + ".dimension" + val_str)
            else:
                diff_list.append(name + ".dimension")
        if other._unit != self._unit:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._unit) + ", other=" + str(other._unit) + ")"
                )
                diff_list.append(name + ".unit" + val_str)
            else:
                diff_list.append(name + ".unit")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.type_element)
        S += getsizeof(self.label)
        S += getsizeof(self.dimension)
        S += getsizeof(self.unit)
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

        Solution_dict = dict()
        Solution_dict["type_element"] = self.type_element
        Solution_dict["label"] = self.label
        Solution_dict["dimension"] = self.dimension
        Solution_dict["unit"] = self.unit
        # The class name is added to the dict for deserialisation purpose
        Solution_dict["__class__"] = "Solution"
        return Solution_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_element_val = self.type_element
        label_val = self.label
        dimension_val = self.dimension
        unit_val = self.unit
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            type_element=type_element_val,
            label=label_val,
            dimension=dimension_val,
            unit=unit_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_element = None
        self.label = None
        self.dimension = None
        self.unit = None

    def _get_type_element(self):
        """getter of type_element"""
        return self._type_element

    def _set_type_element(self, value):
        """setter of type_element"""
        check_var("type_element", value, "str")
        self._type_element = value

    type_element = property(
        fget=_get_type_element,
        fset=_set_type_element,
        doc="""Type of element (Point, Segment2, Triangle3, etc.)

        :Type: str
        """,
    )

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    label = property(
        fget=_get_label,
        fset=_set_label,
        doc="""Label to identify the solution

        :Type: str
        """,
    )

    def _get_dimension(self):
        """getter of dimension"""
        return self._dimension

    def _set_dimension(self, value):
        """setter of dimension"""
        check_var("dimension", value, "int", Vmin=1, Vmax=3)
        self._dimension = value

    dimension = property(
        fget=_get_dimension,
        fset=_set_dimension,
        doc="""Dimension of the physical problem

        :Type: int
        :min: 1
        :max: 3
        """,
    )

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    unit = property(
        fget=_get_unit,
        fset=_set_unit,
        doc="""Unit of the solution

        :Type: str
        """,
    )
