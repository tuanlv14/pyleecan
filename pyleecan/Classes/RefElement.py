# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Interpolation/RefElement.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/RefElement
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

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.RefElement.interpolation import interpolation
except ImportError as error:
    interpolation = error

try:
    from ..Methods.Mesh.RefElement.get_element_area import get_element_area
except ImportError as error:
    get_element_area = error


from numpy import isnan
from ._check import InitUnKnowClassError


class RefElement(FrozenClass):
    """Store shape functions definition in the reference element"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.RefElement.interpolation
    if isinstance(interpolation, ImportError):
        interpolation = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefElement method interpolation: " + str(interpolation)
                )
            )
        )
    else:
        interpolation = interpolation
    # cf Methods.Mesh.RefElement.get_element_area
    if isinstance(get_element_area, ImportError):
        get_element_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use RefElement method get_element_area: "
                    + str(get_element_area)
                )
            )
        )
    else:
        get_element_area = get_element_area
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, epsilon=0.05, init_dict=None, init_str=None):
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
            if "epsilon" in list(init_dict.keys()):
                epsilon = init_dict["epsilon"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.epsilon = epsilon

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        RefElement_str = ""
        if self.parent is None:
            RefElement_str += "parent = None " + linesep
        else:
            RefElement_str += "parent = " + str(type(self.parent)) + " object" + linesep
        RefElement_str += "epsilon = " + str(self.epsilon) + linesep
        return RefElement_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.epsilon != self.epsilon:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if (
            other._epsilon is not None
            and self._epsilon is not None
            and isnan(other._epsilon)
            and isnan(self._epsilon)
        ):
            pass
        elif other._epsilon != self._epsilon:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._epsilon)
                    + ", other="
                    + str(other._epsilon)
                    + ")"
                )
                diff_list.append(name + ".epsilon" + val_str)
            else:
                diff_list.append(name + ".epsilon")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.epsilon)
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

        RefElement_dict = dict()
        RefElement_dict["epsilon"] = self.epsilon
        # The class name is added to the dict for deserialisation purpose
        RefElement_dict["__class__"] = "RefElement"
        return RefElement_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        epsilon_val = self.epsilon
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(epsilon=epsilon_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.epsilon = None

    def _get_epsilon(self):
        """getter of epsilon"""
        return self._epsilon

    def _set_epsilon(self, value):
        """setter of epsilon"""
        check_var("epsilon", value, "float", Vmin=0.00e00)
        self._epsilon = value

    epsilon = property(
        fget=_get_epsilon,
        fset=_set_epsilon,
        doc="""Precision criterion

        :Type: float
        :min: 0.00E+00
        """,
    )
