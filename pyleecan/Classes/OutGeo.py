# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutGeo.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutGeo
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


class OutGeo(FrozenClass):
    """Gather the geometrical and the global outputs"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        stator=None,
        rotor=None,
        Wgap_mec=None,
        Wgap_mag=None,
        Rgap_mec=None,
        Lgap=None,
        logger_name="Pyleecan.OutGeo",
        angle_rotor_initial=None,
        rot_dir=None,
        per_a=None,
        is_antiper_a=None,
        per_t_S=None,
        is_antiper_t_S=None,
        axes_dict=None,
        per_t_R=None,
        is_antiper_t_R=None,
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
            if "stator" in list(init_dict.keys()):
                stator = init_dict["stator"]
            if "rotor" in list(init_dict.keys()):
                rotor = init_dict["rotor"]
            if "Wgap_mec" in list(init_dict.keys()):
                Wgap_mec = init_dict["Wgap_mec"]
            if "Wgap_mag" in list(init_dict.keys()):
                Wgap_mag = init_dict["Wgap_mag"]
            if "Rgap_mec" in list(init_dict.keys()):
                Rgap_mec = init_dict["Rgap_mec"]
            if "Lgap" in list(init_dict.keys()):
                Lgap = init_dict["Lgap"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "per_t_S" in list(init_dict.keys()):
                per_t_S = init_dict["per_t_S"]
            if "is_antiper_t_S" in list(init_dict.keys()):
                is_antiper_t_S = init_dict["is_antiper_t_S"]
            if "axes_dict" in list(init_dict.keys()):
                axes_dict = init_dict["axes_dict"]
            if "per_t_R" in list(init_dict.keys()):
                per_t_R = init_dict["per_t_R"]
            if "is_antiper_t_R" in list(init_dict.keys()):
                is_antiper_t_R = init_dict["is_antiper_t_R"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.stator = stator
        self.rotor = rotor
        self.Wgap_mec = Wgap_mec
        self.Wgap_mag = Wgap_mag
        self.Rgap_mec = Rgap_mec
        self.Lgap = Lgap
        self.logger_name = logger_name
        self.angle_rotor_initial = angle_rotor_initial
        self.rot_dir = rot_dir
        self.per_a = per_a
        self.is_antiper_a = is_antiper_a
        self.per_t_S = per_t_S
        self.is_antiper_t_S = is_antiper_t_S
        self.axes_dict = axes_dict
        self.per_t_R = per_t_R
        self.is_antiper_t_R = is_antiper_t_R

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutGeo_str = ""
        if self.parent is None:
            OutGeo_str += "parent = None " + linesep
        else:
            OutGeo_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.stator is not None:
            tmp = self.stator.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutGeo_str += "stator = " + tmp
        else:
            OutGeo_str += "stator = None" + linesep + linesep
        if self.rotor is not None:
            tmp = self.rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            OutGeo_str += "rotor = " + tmp
        else:
            OutGeo_str += "rotor = None" + linesep + linesep
        OutGeo_str += "Wgap_mec = " + str(self.Wgap_mec) + linesep
        OutGeo_str += "Wgap_mag = " + str(self.Wgap_mag) + linesep
        OutGeo_str += "Rgap_mec = " + str(self.Rgap_mec) + linesep
        OutGeo_str += "Lgap = " + str(self.Lgap) + linesep
        OutGeo_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        OutGeo_str += "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        OutGeo_str += "rot_dir = " + str(self.rot_dir) + linesep
        OutGeo_str += "per_a = " + str(self.per_a) + linesep
        OutGeo_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        OutGeo_str += "per_t_S = " + str(self.per_t_S) + linesep
        OutGeo_str += "is_antiper_t_S = " + str(self.is_antiper_t_S) + linesep
        OutGeo_str += "axes_dict = " + str(self.axes_dict) + linesep + linesep
        OutGeo_str += "per_t_R = " + str(self.per_t_R) + linesep
        OutGeo_str += "is_antiper_t_R = " + str(self.is_antiper_t_R) + linesep
        return OutGeo_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.stator != self.stator:
            return False
        if other.rotor != self.rotor:
            return False
        if other.Wgap_mec != self.Wgap_mec:
            return False
        if other.Wgap_mag != self.Wgap_mag:
            return False
        if other.Rgap_mec != self.Rgap_mec:
            return False
        if other.Lgap != self.Lgap:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.per_a != self.per_a:
            return False
        if other.is_antiper_a != self.is_antiper_a:
            return False
        if other.per_t_S != self.per_t_S:
            return False
        if other.is_antiper_t_S != self.is_antiper_t_S:
            return False
        if other.axes_dict != self.axes_dict:
            return False
        if other.per_t_R != self.per_t_R:
            return False
        if other.is_antiper_t_R != self.is_antiper_t_R:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
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
        if (
            other._Wgap_mec is not None
            and self._Wgap_mec is not None
            and isnan(other._Wgap_mec)
            and isnan(self._Wgap_mec)
        ):
            pass
        elif other._Wgap_mec != self._Wgap_mec:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Wgap_mec)
                    + ", other="
                    + str(other._Wgap_mec)
                    + ")"
                )
                diff_list.append(name + ".Wgap_mec" + val_str)
            else:
                diff_list.append(name + ".Wgap_mec")
        if (
            other._Wgap_mag is not None
            and self._Wgap_mag is not None
            and isnan(other._Wgap_mag)
            and isnan(self._Wgap_mag)
        ):
            pass
        elif other._Wgap_mag != self._Wgap_mag:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Wgap_mag)
                    + ", other="
                    + str(other._Wgap_mag)
                    + ")"
                )
                diff_list.append(name + ".Wgap_mag" + val_str)
            else:
                diff_list.append(name + ".Wgap_mag")
        if (
            other._Rgap_mec is not None
            and self._Rgap_mec is not None
            and isnan(other._Rgap_mec)
            and isnan(self._Rgap_mec)
        ):
            pass
        elif other._Rgap_mec != self._Rgap_mec:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Rgap_mec)
                    + ", other="
                    + str(other._Rgap_mec)
                    + ")"
                )
                diff_list.append(name + ".Rgap_mec" + val_str)
            else:
                diff_list.append(name + ".Rgap_mec")
        if (
            other._Lgap is not None
            and self._Lgap is not None
            and isnan(other._Lgap)
            and isnan(self._Lgap)
        ):
            pass
        elif other._Lgap != self._Lgap:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Lgap) + ", other=" + str(other._Lgap) + ")"
                )
                diff_list.append(name + ".Lgap" + val_str)
            else:
                diff_list.append(name + ".Lgap")
        if other._logger_name != self._logger_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._logger_name)
                    + ", other="
                    + str(other._logger_name)
                    + ")"
                )
                diff_list.append(name + ".logger_name" + val_str)
            else:
                diff_list.append(name + ".logger_name")
        if (
            other._angle_rotor_initial is not None
            and self._angle_rotor_initial is not None
            and isnan(other._angle_rotor_initial)
            and isnan(self._angle_rotor_initial)
        ):
            pass
        elif other._angle_rotor_initial != self._angle_rotor_initial:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._angle_rotor_initial)
                    + ", other="
                    + str(other._angle_rotor_initial)
                    + ")"
                )
                diff_list.append(name + ".angle_rotor_initial" + val_str)
            else:
                diff_list.append(name + ".angle_rotor_initial")
        if other._rot_dir != self._rot_dir:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._rot_dir)
                    + ", other="
                    + str(other._rot_dir)
                    + ")"
                )
                diff_list.append(name + ".rot_dir" + val_str)
            else:
                diff_list.append(name + ".rot_dir")
        if other._per_a != self._per_a:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_a) + ", other=" + str(other._per_a) + ")"
                )
                diff_list.append(name + ".per_a" + val_str)
            else:
                diff_list.append(name + ".per_a")
        if other._is_antiper_a != self._is_antiper_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_a)
                    + ", other="
                    + str(other._is_antiper_a)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_a" + val_str)
            else:
                diff_list.append(name + ".is_antiper_a")
        if other._per_t_S != self._per_t_S:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._per_t_S)
                    + ", other="
                    + str(other._per_t_S)
                    + ")"
                )
                diff_list.append(name + ".per_t_S" + val_str)
            else:
                diff_list.append(name + ".per_t_S")
        if other._is_antiper_t_S != self._is_antiper_t_S:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_t_S)
                    + ", other="
                    + str(other._is_antiper_t_S)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_t_S" + val_str)
            else:
                diff_list.append(name + ".is_antiper_t_S")
        if (other.axes_dict is None and self.axes_dict is not None) or (
            other.axes_dict is not None and self.axes_dict is None
        ):
            diff_list.append(name + ".axes_dict None mismatch")
        elif self.axes_dict is None:
            pass
        elif len(other.axes_dict) != len(self.axes_dict):
            diff_list.append("len(" + name + "axes_dict)")
        else:
            for key in self.axes_dict:
                diff_list.extend(
                    self.axes_dict[key].compare(
                        other.axes_dict[key],
                        name=name + ".axes_dict[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if other._per_t_R != self._per_t_R:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._per_t_R)
                    + ", other="
                    + str(other._per_t_R)
                    + ")"
                )
                diff_list.append(name + ".per_t_R" + val_str)
            else:
                diff_list.append(name + ".per_t_R")
        if other._is_antiper_t_R != self._is_antiper_t_R:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_t_R)
                    + ", other="
                    + str(other._is_antiper_t_R)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_t_R" + val_str)
            else:
                diff_list.append(name + ".is_antiper_t_R")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.stator)
        S += getsizeof(self.rotor)
        S += getsizeof(self.Wgap_mec)
        S += getsizeof(self.Wgap_mag)
        S += getsizeof(self.Rgap_mec)
        S += getsizeof(self.Lgap)
        S += getsizeof(self.logger_name)
        S += getsizeof(self.angle_rotor_initial)
        S += getsizeof(self.rot_dir)
        S += getsizeof(self.per_a)
        S += getsizeof(self.is_antiper_a)
        S += getsizeof(self.per_t_S)
        S += getsizeof(self.is_antiper_t_S)
        if self.axes_dict is not None:
            for key, value in self.axes_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.per_t_R)
        S += getsizeof(self.is_antiper_t_R)
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

        OutGeo_dict = dict()
        if self.stator is None:
            OutGeo_dict["stator"] = None
        else:
            OutGeo_dict["stator"] = self.stator.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.rotor is None:
            OutGeo_dict["rotor"] = None
        else:
            OutGeo_dict["rotor"] = self.rotor.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        OutGeo_dict["Wgap_mec"] = self.Wgap_mec
        OutGeo_dict["Wgap_mag"] = self.Wgap_mag
        OutGeo_dict["Rgap_mec"] = self.Rgap_mec
        OutGeo_dict["Lgap"] = self.Lgap
        OutGeo_dict["logger_name"] = self.logger_name
        OutGeo_dict["angle_rotor_initial"] = self.angle_rotor_initial
        OutGeo_dict["rot_dir"] = self.rot_dir
        OutGeo_dict["per_a"] = self.per_a
        OutGeo_dict["is_antiper_a"] = self.is_antiper_a
        OutGeo_dict["per_t_S"] = self.per_t_S
        OutGeo_dict["is_antiper_t_S"] = self.is_antiper_t_S
        if self.axes_dict is None:
            OutGeo_dict["axes_dict"] = None
        else:
            OutGeo_dict["axes_dict"] = dict()
            for key, obj in self.axes_dict.items():
                if obj is not None:
                    OutGeo_dict["axes_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    OutGeo_dict["axes_dict"][key] = None
        OutGeo_dict["per_t_R"] = self.per_t_R
        OutGeo_dict["is_antiper_t_R"] = self.is_antiper_t_R
        # The class name is added to the dict for deserialisation purpose
        OutGeo_dict["__class__"] = "OutGeo"
        return OutGeo_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.stator is None:
            stator_val = None
        else:
            stator_val = self.stator.copy()
        if self.rotor is None:
            rotor_val = None
        else:
            rotor_val = self.rotor.copy()
        Wgap_mec_val = self.Wgap_mec
        Wgap_mag_val = self.Wgap_mag
        Rgap_mec_val = self.Rgap_mec
        Lgap_val = self.Lgap
        logger_name_val = self.logger_name
        angle_rotor_initial_val = self.angle_rotor_initial
        rot_dir_val = self.rot_dir
        per_a_val = self.per_a
        is_antiper_a_val = self.is_antiper_a
        per_t_S_val = self.per_t_S
        is_antiper_t_S_val = self.is_antiper_t_S
        if self.axes_dict is None:
            axes_dict_val = None
        else:
            axes_dict_val = dict()
            for key, obj in self.axes_dict.items():
                axes_dict_val[key] = obj.copy()
        per_t_R_val = self.per_t_R
        is_antiper_t_R_val = self.is_antiper_t_R
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            stator=stator_val,
            rotor=rotor_val,
            Wgap_mec=Wgap_mec_val,
            Wgap_mag=Wgap_mag_val,
            Rgap_mec=Rgap_mec_val,
            Lgap=Lgap_val,
            logger_name=logger_name_val,
            angle_rotor_initial=angle_rotor_initial_val,
            rot_dir=rot_dir_val,
            per_a=per_a_val,
            is_antiper_a=is_antiper_a_val,
            per_t_S=per_t_S_val,
            is_antiper_t_S=is_antiper_t_S_val,
            axes_dict=axes_dict_val,
            per_t_R=per_t_R_val,
            is_antiper_t_R=is_antiper_t_R_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.stator is not None:
            self.stator._set_None()
        if self.rotor is not None:
            self.rotor._set_None()
        self.Wgap_mec = None
        self.Wgap_mag = None
        self.Rgap_mec = None
        self.Lgap = None
        self.logger_name = None
        self.angle_rotor_initial = None
        self.rot_dir = None
        self.per_a = None
        self.is_antiper_a = None
        self.per_t_S = None
        self.is_antiper_t_S = None
        self.axes_dict = None
        self.per_t_R = None
        self.is_antiper_t_R = None

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
            OutGeoLam = import_class("pyleecan.Classes", "OutGeoLam", "stator")
            value = OutGeoLam()
        check_var("stator", value, "OutGeoLam")
        self._stator = value

        if self._stator is not None:
            self._stator.parent = self

    stator = property(
        fget=_get_stator,
        fset=_set_stator,
        doc="""Geometry output of the stator

        :Type: OutGeoLam
        """,
    )

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
            OutGeoLam = import_class("pyleecan.Classes", "OutGeoLam", "rotor")
            value = OutGeoLam()
        check_var("rotor", value, "OutGeoLam")
        self._rotor = value

        if self._rotor is not None:
            self._rotor.parent = self

    rotor = property(
        fget=_get_rotor,
        fset=_set_rotor,
        doc="""Geometry output of the rotor

        :Type: OutGeoLam
        """,
    )

    def _get_Wgap_mec(self):
        """getter of Wgap_mec"""
        return self._Wgap_mec

    def _set_Wgap_mec(self, value):
        """setter of Wgap_mec"""
        check_var("Wgap_mec", value, "float")
        self._Wgap_mec = value

    Wgap_mec = property(
        fget=_get_Wgap_mec,
        fset=_set_Wgap_mec,
        doc="""mechanical airgap width (minimal distance between the lamination including magnet)

        :Type: float
        """,
    )

    def _get_Wgap_mag(self):
        """getter of Wgap_mag"""
        return self._Wgap_mag

    def _set_Wgap_mag(self, value):
        """setter of Wgap_mag"""
        check_var("Wgap_mag", value, "float")
        self._Wgap_mag = value

    Wgap_mag = property(
        fget=_get_Wgap_mag,
        fset=_set_Wgap_mag,
        doc="""the magnetic airgap width (distance beetween the two Laminations bore radius)

        :Type: float
        """,
    )

    def _get_Rgap_mec(self):
        """getter of Rgap_mec"""
        return self._Rgap_mec

    def _set_Rgap_mec(self, value):
        """setter of Rgap_mec"""
        check_var("Rgap_mec", value, "float")
        self._Rgap_mec = value

    Rgap_mec = property(
        fget=_get_Rgap_mec,
        fset=_set_Rgap_mec,
        doc="""radius of the center of the mecanical airgap

        :Type: float
        """,
    )

    def _get_Lgap(self):
        """getter of Lgap"""
        return self._Lgap

    def _set_Lgap(self, value):
        """setter of Lgap"""
        check_var("Lgap", value, "float")
        self._Lgap = value

    Lgap = property(
        fget=_get_Lgap,
        fset=_set_Lgap,
        doc="""Airgap active length

        :Type: float
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc="""Name of the logger to use

        :Type: str
        """,
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc="""Difference between the d axis angle of the stator and the rotor

        :Type: float
        """,
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "int", Vmin=-1, Vmax=1)
        self._rot_dir = value

    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc="""Rotation direction of the rotor (rot_dir*N0, default value given by ROT_DIR_REF)

        :Type: int
        :min: -1
        :max: 1
        """,
    )

    def _get_per_a(self):
        """getter of per_a"""
        return self._per_a

    def _set_per_a(self, value):
        """setter of per_a"""
        check_var("per_a", value, "int")
        self._per_a = value

    per_a = property(
        fget=_get_per_a,
        fset=_set_per_a,
        doc="""Number of spatial periodicities of the machine

        :Type: int
        """,
    )

    def _get_is_antiper_a(self):
        """getter of is_antiper_a"""
        return self._is_antiper_a

    def _set_is_antiper_a(self, value):
        """setter of is_antiper_a"""
        check_var("is_antiper_a", value, "bool")
        self._is_antiper_a = value

    is_antiper_a = property(
        fget=_get_is_antiper_a,
        fset=_set_is_antiper_a,
        doc="""True if an spatial anti-periodicity is possible after the periodicities

        :Type: bool
        """,
    )

    def _get_per_t_S(self):
        """getter of per_t_S"""
        return self._per_t_S

    def _set_per_t_S(self, value):
        """setter of per_t_S"""
        check_var("per_t_S", value, "int")
        self._per_t_S = value

    per_t_S = property(
        fget=_get_per_t_S,
        fset=_set_per_t_S,
        doc="""Number of time periodicities of the machine in static referential

        :Type: int
        """,
    )

    def _get_is_antiper_t_S(self):
        """getter of is_antiper_t_S"""
        return self._is_antiper_t_S

    def _set_is_antiper_t_S(self, value):
        """setter of is_antiper_t_S"""
        check_var("is_antiper_t_S", value, "bool")
        self._is_antiper_t_S = value

    is_antiper_t_S = property(
        fget=_get_is_antiper_t_S,
        fset=_set_is_antiper_t_S,
        doc="""True if an time anti-periodicity is possible after the periodicities in static referential

        :Type: bool
        """,
    )

    def _get_axes_dict(self):
        """getter of axes_dict"""
        if self._axes_dict is not None:
            for key, obj in self._axes_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._axes_dict

    def _set_axes_dict(self, value):
        """setter of axes_dict"""
        if type(value) is dict:
            for key, obj in value.items():
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[key] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "SciDataTool.Classes", obj.get("__class__"), "axes_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("axes_dict", value, "{Data}")
        self._axes_dict = value

    axes_dict = property(
        fget=_get_axes_dict,
        fset=_set_axes_dict,
        doc="""Dict containing axes data without periodicities used for plots and to have simulation full time/angle vectors

        :Type: {SciDataTool.Classes.DataND.Data}
        """,
    )

    def _get_per_t_R(self):
        """getter of per_t_R"""
        return self._per_t_R

    def _set_per_t_R(self, value):
        """setter of per_t_R"""
        check_var("per_t_R", value, "int")
        self._per_t_R = value

    per_t_R = property(
        fget=_get_per_t_R,
        fset=_set_per_t_R,
        doc="""Number of time periodicities of the machine in rotating referential

        :Type: int
        """,
    )

    def _get_is_antiper_t_R(self):
        """getter of is_antiper_t_R"""
        return self._is_antiper_t_R

    def _set_is_antiper_t_R(self, value):
        """setter of is_antiper_t_R"""
        check_var("is_antiper_t_R", value, "bool")
        self._is_antiper_t_R = value

    is_antiper_t_R = property(
        fget=_get_is_antiper_t_R,
        fset=_set_is_antiper_t_R,
        doc="""True if an time anti-periodicity is possible after the periodicities in rotating referential

        :Type: bool
        """,
    )
