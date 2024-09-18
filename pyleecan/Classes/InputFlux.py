# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/InputFlux.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/InputFlux
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .InputCurrent import InputCurrent

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputFlux.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ..Classes.ImportMatrixVal import ImportMatrixVal
from numpy import ndarray
from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class InputFlux(InputCurrent):
    """Input to skip the magnetic module and start with the structural one"""

    VERSION = 1

    # cf Methods.Simulation.InputFlux.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError("Can't use InputFlux method gen_input: " + str(gen_input))
            )
        )
    else:
        gen_input = gen_input
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        per_a=1,
        per_t=1,
        is_antiper_a=False,
        is_antiper_t=False,
        B_dict=None,
        unit=None,
        slice=None,
        B_enforced=None,
        Is=None,
        Ir=None,
        Is_harm=None,
        rot_dir=None,
        angle_rotor_initial=0,
        PWM=None,
        phase_dir=None,
        current_dir=None,
        is_periodicity_t=False,
        is_periodicity_a=False,
        is_generator=False,
        time=None,
        angle=None,
        Nt_tot=2048,
        Nrev=None,
        Na_tot=2048,
        OP=None,
        t_final=None,
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
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "per_t" in list(init_dict.keys()):
                per_t = init_dict["per_t"]
            if "is_antiper_a" in list(init_dict.keys()):
                is_antiper_a = init_dict["is_antiper_a"]
            if "is_antiper_t" in list(init_dict.keys()):
                is_antiper_t = init_dict["is_antiper_t"]
            if "B_dict" in list(init_dict.keys()):
                B_dict = init_dict["B_dict"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "slice" in list(init_dict.keys()):
                slice = init_dict["slice"]
            if "B_enforced" in list(init_dict.keys()):
                B_enforced = init_dict["B_enforced"]
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "Is_harm" in list(init_dict.keys()):
                Is_harm = init_dict["Is_harm"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "PWM" in list(init_dict.keys()):
                PWM = init_dict["PWM"]
            if "phase_dir" in list(init_dict.keys()):
                phase_dir = init_dict["phase_dir"]
            if "current_dir" in list(init_dict.keys()):
                current_dir = init_dict["current_dir"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "is_generator" in list(init_dict.keys()):
                is_generator = init_dict["is_generator"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
            if "Nt_tot" in list(init_dict.keys()):
                Nt_tot = init_dict["Nt_tot"]
            if "Nrev" in list(init_dict.keys()):
                Nrev = init_dict["Nrev"]
            if "Na_tot" in list(init_dict.keys()):
                Na_tot = init_dict["Na_tot"]
            if "OP" in list(init_dict.keys()):
                OP = init_dict["OP"]
            if "t_final" in list(init_dict.keys()):
                t_final = init_dict["t_final"]
        # Set the properties (value check and convertion are done in setter)
        self.per_a = per_a
        self.per_t = per_t
        self.is_antiper_a = is_antiper_a
        self.is_antiper_t = is_antiper_t
        self.B_dict = B_dict
        self.unit = unit
        self.slice = slice
        self.B_enforced = B_enforced
        # Call InputCurrent init
        super(InputFlux, self).__init__(
            Is=Is,
            Ir=Ir,
            Is_harm=Is_harm,
            rot_dir=rot_dir,
            angle_rotor_initial=angle_rotor_initial,
            PWM=PWM,
            phase_dir=phase_dir,
            current_dir=current_dir,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            is_generator=is_generator,
            time=time,
            angle=angle,
            Nt_tot=Nt_tot,
            Nrev=Nrev,
            Na_tot=Na_tot,
            OP=OP,
            t_final=t_final,
        )
        # The class is frozen (in InputCurrent init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        InputFlux_str = ""
        # Get the properties inherited from InputCurrent
        InputFlux_str += super(InputFlux, self).__str__()
        InputFlux_str += "per_a = " + str(self.per_a) + linesep
        InputFlux_str += "per_t = " + str(self.per_t) + linesep
        InputFlux_str += "is_antiper_a = " + str(self.is_antiper_a) + linesep
        InputFlux_str += "is_antiper_t = " + str(self.is_antiper_t) + linesep
        InputFlux_str += "B_dict = " + str(self.B_dict) + linesep
        InputFlux_str += 'unit = "' + str(self.unit) + '"' + linesep
        InputFlux_str += (
            "slice = "
            + linesep
            + str(self.slice).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        InputFlux_str += "B_enforced = " + str(self.B_enforced) + linesep + linesep
        return InputFlux_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from InputCurrent
        if not super(InputFlux, self).__eq__(other):
            return False
        if other.per_a != self.per_a:
            return False
        if other.per_t != self.per_t:
            return False
        if other.is_antiper_a != self.is_antiper_a:
            return False
        if other.is_antiper_t != self.is_antiper_t:
            return False
        if other.B_dict != self.B_dict:
            return False
        if other.unit != self.unit:
            return False
        if not array_equal(other.slice, self.slice):
            return False
        if other.B_enforced != self.B_enforced:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from InputCurrent
        diff_list.extend(
            super(InputFlux, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._per_a != self._per_a:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_a) + ", other=" + str(other._per_a) + ")"
                )
                diff_list.append(name + ".per_a" + val_str)
            else:
                diff_list.append(name + ".per_a")
        if other._per_t != self._per_t:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_t) + ", other=" + str(other._per_t) + ")"
                )
                diff_list.append(name + ".per_t" + val_str)
            else:
                diff_list.append(name + ".per_t")
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
        if other._is_antiper_t != self._is_antiper_t:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_antiper_t)
                    + ", other="
                    + str(other._is_antiper_t)
                    + ")"
                )
                diff_list.append(name + ".is_antiper_t" + val_str)
            else:
                diff_list.append(name + ".is_antiper_t")
        if other._B_dict != self._B_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._B_dict)
                    + ", other="
                    + str(other._B_dict)
                    + ")"
                )
                diff_list.append(name + ".B_dict" + val_str)
            else:
                diff_list.append(name + ".B_dict")
        if other._unit != self._unit:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._unit) + ", other=" + str(other._unit) + ")"
                )
                diff_list.append(name + ".unit" + val_str)
            else:
                diff_list.append(name + ".unit")
        if not array_equal(other.slice, self.slice):
            diff_list.append(name + ".slice")
        if (other.B_enforced is None and self.B_enforced is not None) or (
            other.B_enforced is not None and self.B_enforced is None
        ):
            diff_list.append(name + ".B_enforced None mismatch")
        elif self.B_enforced is not None:
            diff_list.extend(
                self.B_enforced.compare(
                    other.B_enforced,
                    name=name + ".B_enforced",
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

        # Get size of the properties inherited from InputCurrent
        S += super(InputFlux, self).__sizeof__()
        S += getsizeof(self.per_a)
        S += getsizeof(self.per_t)
        S += getsizeof(self.is_antiper_a)
        S += getsizeof(self.is_antiper_t)
        if self.B_dict is not None:
            for key, value in self.B_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.unit)
        S += getsizeof(self.slice)
        S += getsizeof(self.B_enforced)
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

        # Get the properties inherited from InputCurrent
        InputFlux_dict = super(InputFlux, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        InputFlux_dict["per_a"] = self.per_a
        InputFlux_dict["per_t"] = self.per_t
        InputFlux_dict["is_antiper_a"] = self.is_antiper_a
        InputFlux_dict["is_antiper_t"] = self.is_antiper_t
        InputFlux_dict["B_dict"] = (
            self.B_dict.copy() if self.B_dict is not None else None
        )
        InputFlux_dict["unit"] = self.unit
        if self.slice is None:
            InputFlux_dict["slice"] = None
        else:
            if type_handle_ndarray == 0:
                InputFlux_dict["slice"] = self.slice.tolist()
            elif type_handle_ndarray == 1:
                InputFlux_dict["slice"] = self.slice.copy()
            elif type_handle_ndarray == 2:
                InputFlux_dict["slice"] = self.slice
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        if self.B_enforced is None:
            InputFlux_dict["B_enforced"] = None
        else:
            InputFlux_dict["B_enforced"] = self.B_enforced.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        InputFlux_dict["__class__"] = "InputFlux"
        return InputFlux_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        per_a_val = self.per_a
        per_t_val = self.per_t
        is_antiper_a_val = self.is_antiper_a
        is_antiper_t_val = self.is_antiper_t
        if self.B_dict is None:
            B_dict_val = None
        else:
            B_dict_val = self.B_dict.copy()
        unit_val = self.unit
        if self.slice is None:
            slice_val = None
        else:
            slice_val = self.slice.copy()
        if self.B_enforced is None:
            B_enforced_val = None
        else:
            B_enforced_val = self.B_enforced.copy()
        if self.Is is None:
            Is_val = None
        else:
            Is_val = self.Is.copy()
        if self.Ir is None:
            Ir_val = None
        else:
            Ir_val = self.Ir.copy()
        if self.Is_harm is None:
            Is_harm_val = None
        else:
            Is_harm_val = self.Is_harm.copy()
        rot_dir_val = self.rot_dir
        angle_rotor_initial_val = self.angle_rotor_initial
        if self.PWM is None:
            PWM_val = None
        else:
            PWM_val = self.PWM.copy()
        phase_dir_val = self.phase_dir
        current_dir_val = self.current_dir
        is_periodicity_t_val = self.is_periodicity_t
        is_periodicity_a_val = self.is_periodicity_a
        is_generator_val = self.is_generator
        if self.time is None:
            time_val = None
        else:
            time_val = self.time.copy()
        if self.angle is None:
            angle_val = None
        else:
            angle_val = self.angle.copy()
        Nt_tot_val = self.Nt_tot
        Nrev_val = self.Nrev
        Na_tot_val = self.Na_tot
        if self.OP is None:
            OP_val = None
        else:
            OP_val = self.OP.copy()
        t_final_val = self.t_final
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            per_a=per_a_val,
            per_t=per_t_val,
            is_antiper_a=is_antiper_a_val,
            is_antiper_t=is_antiper_t_val,
            B_dict=B_dict_val,
            unit=unit_val,
            slice=slice_val,
            B_enforced=B_enforced_val,
            Is=Is_val,
            Ir=Ir_val,
            Is_harm=Is_harm_val,
            rot_dir=rot_dir_val,
            angle_rotor_initial=angle_rotor_initial_val,
            PWM=PWM_val,
            phase_dir=phase_dir_val,
            current_dir=current_dir_val,
            is_periodicity_t=is_periodicity_t_val,
            is_periodicity_a=is_periodicity_a_val,
            is_generator=is_generator_val,
            time=time_val,
            angle=angle_val,
            Nt_tot=Nt_tot_val,
            Nrev=Nrev_val,
            Na_tot=Na_tot_val,
            OP=OP_val,
            t_final=t_final_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.per_a = None
        self.per_t = None
        self.is_antiper_a = None
        self.is_antiper_t = None
        self.B_dict = None
        self.unit = None
        self.slice = None
        self.B_enforced = None
        # Set to None the properties inherited from InputCurrent
        super(InputFlux, self)._set_None()

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
        doc="""Angle periodicity

        :Type: int
        """,
    )

    def _get_per_t(self):
        """getter of per_t"""
        return self._per_t

    def _set_per_t(self, value):
        """setter of per_t"""
        check_var("per_t", value, "int")
        self._per_t = value

    per_t = property(
        fget=_get_per_t,
        fset=_set_per_t,
        doc="""Time periodicity

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
        doc="""If angle is antiperiodic

        :Type: bool
        """,
    )

    def _get_is_antiper_t(self):
        """getter of is_antiper_t"""
        return self._is_antiper_t

    def _set_is_antiper_t(self, value):
        """setter of is_antiper_t"""
        check_var("is_antiper_t", value, "bool")
        self._is_antiper_t = value

    is_antiper_t = property(
        fget=_get_is_antiper_t,
        fset=_set_is_antiper_t,
        doc="""If time is antiperiodic

        :Type: bool
        """,
    )

    def _get_B_dict(self):
        """getter of B_dict"""
        return self._B_dict

    def _set_B_dict(self, value):
        """setter of B_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("B_dict", value, "dict")
        self._B_dict = value

    B_dict = property(
        fget=_get_B_dict,
        fset=_set_B_dict,
        doc="""Dict of Import objects or lists for each component of the flux

        :Type: dict
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
        doc="""Unit of the flux if not T

        :Type: str
        """,
    )

    def _get_slice(self):
        """getter of slice"""
        return self._slice

    def _set_slice(self, value):
        """setter of slice"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("slice", value, "ndarray")
        self._slice = value

    slice = property(
        fget=_get_slice,
        fset=_set_slice,
        doc="""Slice axis values

        :Type: ndarray
        """,
    )

    def _get_B_enforced(self):
        """getter of B_enforced"""
        return self._B_enforced

    def _set_B_enforced(self, value):
        """setter of B_enforced"""
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
                "SciDataTool.Classes", value.get("__class__"), "B_enforced"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = VectorField()
        check_var("B_enforced", value, "VectorField")
        self._B_enforced = value

    B_enforced = property(
        fget=_get_B_enforced,
        fset=_set_B_enforced,
        doc="""Airgap flux density as VectorField object

        :Type: SciDataTool.Classes.VectorField.VectorField
        """,
    )
