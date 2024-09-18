# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/MachineAsync.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/MachineAsync
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
from .Machine import Machine

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineAsync.is_synchronous import is_synchronous
except ImportError as error:
    is_synchronous = error

try:
    from ..Methods.Machine.MachineAsync.comp_desc_dict import comp_desc_dict
except ImportError as error:
    comp_desc_dict = error


from numpy import isnan
from ._check import InitUnKnowClassError


class MachineAsync(Machine):
    """Abstract class for asynchronous machines"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineAsync.is_synchronous
    if isinstance(is_synchronous, ImportError):
        is_synchronous = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineAsync method is_synchronous: "
                    + str(is_synchronous)
                )
            )
        )
    else:
        is_synchronous = is_synchronous
    # cf Methods.Machine.MachineAsync.comp_desc_dict
    if isinstance(comp_desc_dict, ImportError):
        comp_desc_dict = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineAsync method comp_desc_dict: "
                    + str(comp_desc_dict)
                )
            )
        )
    else:
        comp_desc_dict = comp_desc_dict
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        frame=-1,
        shaft=-1,
        name="default_machine",
        desc="",
        type_machine=1,
        logger_name="Pyleecan.Machine",
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
            if "frame" in list(init_dict.keys()):
                frame = init_dict["frame"]
            if "shaft" in list(init_dict.keys()):
                shaft = init_dict["shaft"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "desc" in list(init_dict.keys()):
                desc = init_dict["desc"]
            if "type_machine" in list(init_dict.keys()):
                type_machine = init_dict["type_machine"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
        # Set the properties (value check and convertion are done in setter)
        # Call Machine init
        super(MachineAsync, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in Machine init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MachineAsync_str = ""
        # Get the properties inherited from Machine
        MachineAsync_str += super(MachineAsync, self).__str__()
        return MachineAsync_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Machine
        if not super(MachineAsync, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Machine
        diff_list.extend(
            super(MachineAsync, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Machine
        S += super(MachineAsync, self).__sizeof__()
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

        # Get the properties inherited from Machine
        MachineAsync_dict = super(MachineAsync, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MachineAsync_dict["__class__"] = "MachineAsync"
        return MachineAsync_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.frame is None:
            frame_val = None
        else:
            frame_val = self.frame.copy()
        if self.shaft is None:
            shaft_val = None
        else:
            shaft_val = self.shaft.copy()
        name_val = self.name
        desc_val = self.desc
        type_machine_val = self.type_machine
        logger_name_val = self.logger_name
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            frame=frame_val,
            shaft=shaft_val,
            name=name_val,
            desc=desc_val,
            type_machine=type_machine_val,
            logger_name=logger_name_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Machine
        super(MachineAsync, self)._set_None()
