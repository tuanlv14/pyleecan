# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/MachineLSPM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/MachineLSPM
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
from .MachineSync import MachineSync

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.MachineLSPM.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Machine.MachineLSPM.get_machine_type import get_machine_type
except ImportError as error:
    get_machine_type = error


from numpy import isnan
from ._check import InitUnKnowClassError


class MachineLSPM(MachineSync):
    """Line Start Permanent Magnet Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.MachineLSPM.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use MachineLSPM method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Machine.MachineLSPM.get_machine_type
    if isinstance(get_machine_type, ImportError):
        get_machine_type = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MachineLSPM method get_machine_type: "
                    + str(get_machine_type)
                )
            )
        )
    else:
        get_machine_type = get_machine_type
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        rotor=-1,
        stator=-1,
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
            if "rotor" in list(init_dict.keys()):
                rotor = init_dict["rotor"]
            if "stator" in list(init_dict.keys()):
                stator = init_dict["stator"]
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
        self.rotor = rotor
        self.stator = stator
        # Call MachineSync init
        super(MachineLSPM, self).__init__(
            frame=frame,
            shaft=shaft,
            name=name,
            desc=desc,
            type_machine=type_machine,
            logger_name=logger_name,
        )
        # The class is frozen (in MachineSync init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MachineLSPM_str = ""
        # Get the properties inherited from MachineSync
        MachineLSPM_str += super(MachineLSPM, self).__str__()
        if self.rotor is not None:
            tmp = self.rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineLSPM_str += "rotor = " + tmp
        else:
            MachineLSPM_str += "rotor = None" + linesep + linesep
        if self.stator is not None:
            tmp = self.stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MachineLSPM_str += "stator = " + tmp
        else:
            MachineLSPM_str += "stator = None" + linesep + linesep
        return MachineLSPM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from MachineSync
        if not super(MachineLSPM, self).__eq__(other):
            return False
        if other.rotor != self.rotor:
            return False
        if other.stator != self.stator:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from MachineSync
        diff_list.extend(
            super(MachineLSPM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.rotor is None and self.rotor is not None) or (
            other.rotor is not None and self.rotor is None
        ):
            diff_list.append(name + ".rotor None mismatch")
        elif self.rotor is not None:
            diff_list.extend(
                self.rotor.compare(
                    other.rotor,
                    name=name + ".rotor",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.stator is None and self.stator is not None) or (
            other.stator is not None and self.stator is None
        ):
            diff_list.append(name + ".stator None mismatch")
        elif self.stator is not None:
            diff_list.extend(
                self.stator.compare(
                    other.stator,
                    name=name + ".stator",
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

        # Get size of the properties inherited from MachineSync
        S += super(MachineLSPM, self).__sizeof__()
        S += getsizeof(self.rotor)
        S += getsizeof(self.stator)
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

        # Get the properties inherited from MachineSync
        MachineLSPM_dict = super(MachineLSPM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.rotor is None:
            MachineLSPM_dict["rotor"] = None
        else:
            MachineLSPM_dict["rotor"] = self.rotor.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.stator is None:
            MachineLSPM_dict["stator"] = None
        else:
            MachineLSPM_dict["stator"] = self.stator.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MachineLSPM_dict["__class__"] = "MachineLSPM"
        return MachineLSPM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.rotor is None:
            rotor_val = None
        else:
            rotor_val = self.rotor.copy()
        if self.stator is None:
            stator_val = None
        else:
            stator_val = self.stator.copy()
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
            rotor=rotor_val,
            stator=stator_val,
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

        if self.rotor is not None:
            self.rotor._set_None()
        if self.stator is not None:
            self.stator._set_None()
        # Set to None the properties inherited from MachineSync
        super(MachineLSPM, self)._set_None()

    def _get_rotor(self):
        """getter of rotor"""
        return self._rotor

    def _set_rotor(self, value):
        """setter of rotor"""
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
                "pyleecan.Classes", value.get("__class__"), "rotor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            LamSquirrelCageMag = import_class(
                "pyleecan.Classes", "LamSquirrelCageMag", "rotor"
            )
            value = LamSquirrelCageMag()
        check_var("rotor", value, "LamSquirrelCageMag")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    rotor = property(
        fget=_get_rotor,
        fset=_set_rotor,
        doc="""Machine's Rotor

        :Type: LamSquirrelCageMag
        """,
    )

    def _get_stator(self):
        """getter of stator"""
        return self._stator

    def _set_stator(self, value):
        """setter of stator"""
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
                "pyleecan.Classes", value.get("__class__"), "stator"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind", "stator")
            value = LamSlotWind()
        check_var("stator", value, "LamSlotWind")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    stator = property(
        fget=_get_stator,
        fset=_set_stator,
        doc="""Machine's Stator

        :Type: LamSlotWind
        """,
    )
