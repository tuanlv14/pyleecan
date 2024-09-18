# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Mesh.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/Mesh
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
    from ..Methods.Mesh.Mesh.get_node_coordinate import get_node_coordinate
except ImportError as error:
    get_node_coordinate = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Mesh(FrozenClass):
    """Abstract Class for mesh related classes"""

    VERSION = 1

    # cf Methods.Mesh.Mesh.get_node_coordinate
    if isinstance(get_node_coordinate, ImportError):
        get_node_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Mesh method get_node_coordinate: "
                    + str(get_node_coordinate)
                )
            )
        )
    else:
        get_node_coordinate = get_node_coordinate
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, dimension=2, init_dict=None, init_str=None):
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
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.dimension = dimension

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Mesh_str = ""
        if self.parent is None:
            Mesh_str += "parent = None " + linesep
        else:
            Mesh_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Mesh_str += "dimension = " + str(self.dimension) + linesep
        return Mesh_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.dimension != self.dimension:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
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
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.dimension)
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

        Mesh_dict = dict()
        Mesh_dict["dimension"] = self.dimension
        # The class name is added to the dict for deserialisation purpose
        Mesh_dict["__class__"] = "Mesh"
        return Mesh_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        dimension_val = self.dimension
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(dimension=dimension_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.dimension = None

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
