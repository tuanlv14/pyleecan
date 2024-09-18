# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Material/MatStructural.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Material/MatStructural
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


class MatStructural(FrozenClass):
    """Material Structural properties"""

    VERSION = 1

    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        rho=7650,
        Ex=215000000000.0,
        Ey=215000000000.0,
        Ez=80000000000,
        nu_xy=0.3,
        nu_xz=0.03,
        nu_yz=0.03,
        Gxz=2000000000,
        Gxy=0,
        Gyz=2000000000,
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
            if "rho" in list(init_dict.keys()):
                rho = init_dict["rho"]
            if "Ex" in list(init_dict.keys()):
                Ex = init_dict["Ex"]
            if "Ey" in list(init_dict.keys()):
                Ey = init_dict["Ey"]
            if "Ez" in list(init_dict.keys()):
                Ez = init_dict["Ez"]
            if "nu_xy" in list(init_dict.keys()):
                nu_xy = init_dict["nu_xy"]
            if "nu_xz" in list(init_dict.keys()):
                nu_xz = init_dict["nu_xz"]
            if "nu_yz" in list(init_dict.keys()):
                nu_yz = init_dict["nu_yz"]
            if "Gxz" in list(init_dict.keys()):
                Gxz = init_dict["Gxz"]
            if "Gxy" in list(init_dict.keys()):
                Gxy = init_dict["Gxy"]
            if "Gyz" in list(init_dict.keys()):
                Gyz = init_dict["Gyz"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.rho = rho
        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez
        self.nu_xy = nu_xy
        self.nu_xz = nu_xz
        self.nu_yz = nu_yz
        self.Gxz = Gxz
        self.Gxy = Gxy
        self.Gyz = Gyz

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MatStructural_str = ""
        if self.parent is None:
            MatStructural_str += "parent = None " + linesep
        else:
            MatStructural_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MatStructural_str += "rho = " + str(self.rho) + linesep
        MatStructural_str += "Ex = " + str(self.Ex) + linesep
        MatStructural_str += "Ey = " + str(self.Ey) + linesep
        MatStructural_str += "Ez = " + str(self.Ez) + linesep
        MatStructural_str += "nu_xy = " + str(self.nu_xy) + linesep
        MatStructural_str += "nu_xz = " + str(self.nu_xz) + linesep
        MatStructural_str += "nu_yz = " + str(self.nu_yz) + linesep
        MatStructural_str += "Gxz = " + str(self.Gxz) + linesep
        MatStructural_str += "Gxy = " + str(self.Gxy) + linesep
        MatStructural_str += "Gyz = " + str(self.Gyz) + linesep
        return MatStructural_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.rho != self.rho:
            return False
        if other.Ex != self.Ex:
            return False
        if other.Ey != self.Ey:
            return False
        if other.Ez != self.Ez:
            return False
        if other.nu_xy != self.nu_xy:
            return False
        if other.nu_xz != self.nu_xz:
            return False
        if other.nu_yz != self.nu_yz:
            return False
        if other.Gxz != self.Gxz:
            return False
        if other.Gxy != self.Gxy:
            return False
        if other.Gyz != self.Gyz:
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
            other._rho is not None
            and self._rho is not None
            and isnan(other._rho)
            and isnan(self._rho)
        ):
            pass
        elif other._rho != self._rho:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._rho) + ", other=" + str(other._rho) + ")"
                )
                diff_list.append(name + ".rho" + val_str)
            else:
                diff_list.append(name + ".rho")
        if (
            other._Ex is not None
            and self._Ex is not None
            and isnan(other._Ex)
            and isnan(self._Ex)
        ):
            pass
        elif other._Ex != self._Ex:
            if is_add_value:
                val_str = " (self=" + str(self._Ex) + ", other=" + str(other._Ex) + ")"
                diff_list.append(name + ".Ex" + val_str)
            else:
                diff_list.append(name + ".Ex")
        if (
            other._Ey is not None
            and self._Ey is not None
            and isnan(other._Ey)
            and isnan(self._Ey)
        ):
            pass
        elif other._Ey != self._Ey:
            if is_add_value:
                val_str = " (self=" + str(self._Ey) + ", other=" + str(other._Ey) + ")"
                diff_list.append(name + ".Ey" + val_str)
            else:
                diff_list.append(name + ".Ey")
        if (
            other._Ez is not None
            and self._Ez is not None
            and isnan(other._Ez)
            and isnan(self._Ez)
        ):
            pass
        elif other._Ez != self._Ez:
            if is_add_value:
                val_str = " (self=" + str(self._Ez) + ", other=" + str(other._Ez) + ")"
                diff_list.append(name + ".Ez" + val_str)
            else:
                diff_list.append(name + ".Ez")
        if (
            other._nu_xy is not None
            and self._nu_xy is not None
            and isnan(other._nu_xy)
            and isnan(self._nu_xy)
        ):
            pass
        elif other._nu_xy != self._nu_xy:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._nu_xy) + ", other=" + str(other._nu_xy) + ")"
                )
                diff_list.append(name + ".nu_xy" + val_str)
            else:
                diff_list.append(name + ".nu_xy")
        if (
            other._nu_xz is not None
            and self._nu_xz is not None
            and isnan(other._nu_xz)
            and isnan(self._nu_xz)
        ):
            pass
        elif other._nu_xz != self._nu_xz:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._nu_xz) + ", other=" + str(other._nu_xz) + ")"
                )
                diff_list.append(name + ".nu_xz" + val_str)
            else:
                diff_list.append(name + ".nu_xz")
        if (
            other._nu_yz is not None
            and self._nu_yz is not None
            and isnan(other._nu_yz)
            and isnan(self._nu_yz)
        ):
            pass
        elif other._nu_yz != self._nu_yz:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._nu_yz) + ", other=" + str(other._nu_yz) + ")"
                )
                diff_list.append(name + ".nu_yz" + val_str)
            else:
                diff_list.append(name + ".nu_yz")
        if (
            other._Gxz is not None
            and self._Gxz is not None
            and isnan(other._Gxz)
            and isnan(self._Gxz)
        ):
            pass
        elif other._Gxz != self._Gxz:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Gxz) + ", other=" + str(other._Gxz) + ")"
                )
                diff_list.append(name + ".Gxz" + val_str)
            else:
                diff_list.append(name + ".Gxz")
        if (
            other._Gxy is not None
            and self._Gxy is not None
            and isnan(other._Gxy)
            and isnan(self._Gxy)
        ):
            pass
        elif other._Gxy != self._Gxy:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Gxy) + ", other=" + str(other._Gxy) + ")"
                )
                diff_list.append(name + ".Gxy" + val_str)
            else:
                diff_list.append(name + ".Gxy")
        if (
            other._Gyz is not None
            and self._Gyz is not None
            and isnan(other._Gyz)
            and isnan(self._Gyz)
        ):
            pass
        elif other._Gyz != self._Gyz:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Gyz) + ", other=" + str(other._Gyz) + ")"
                )
                diff_list.append(name + ".Gyz" + val_str)
            else:
                diff_list.append(name + ".Gyz")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.rho)
        S += getsizeof(self.Ex)
        S += getsizeof(self.Ey)
        S += getsizeof(self.Ez)
        S += getsizeof(self.nu_xy)
        S += getsizeof(self.nu_xz)
        S += getsizeof(self.nu_yz)
        S += getsizeof(self.Gxz)
        S += getsizeof(self.Gxy)
        S += getsizeof(self.Gyz)
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

        MatStructural_dict = dict()
        MatStructural_dict["rho"] = self.rho
        MatStructural_dict["Ex"] = self.Ex
        MatStructural_dict["Ey"] = self.Ey
        MatStructural_dict["Ez"] = self.Ez
        MatStructural_dict["nu_xy"] = self.nu_xy
        MatStructural_dict["nu_xz"] = self.nu_xz
        MatStructural_dict["nu_yz"] = self.nu_yz
        MatStructural_dict["Gxz"] = self.Gxz
        MatStructural_dict["Gxy"] = self.Gxy
        MatStructural_dict["Gyz"] = self.Gyz
        # The class name is added to the dict for deserialisation purpose
        MatStructural_dict["__class__"] = "MatStructural"
        return MatStructural_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        rho_val = self.rho
        Ex_val = self.Ex
        Ey_val = self.Ey
        Ez_val = self.Ez
        nu_xy_val = self.nu_xy
        nu_xz_val = self.nu_xz
        nu_yz_val = self.nu_yz
        Gxz_val = self.Gxz
        Gxy_val = self.Gxy
        Gyz_val = self.Gyz
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            rho=rho_val,
            Ex=Ex_val,
            Ey=Ey_val,
            Ez=Ez_val,
            nu_xy=nu_xy_val,
            nu_xz=nu_xz_val,
            nu_yz=nu_yz_val,
            Gxz=Gxz_val,
            Gxy=Gxy_val,
            Gyz=Gyz_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.rho = None
        self.Ex = None
        self.Ey = None
        self.Ez = None
        self.nu_xy = None
        self.nu_xz = None
        self.nu_yz = None
        self.Gxz = None
        self.Gxy = None
        self.Gyz = None

    def _get_rho(self):
        """getter of rho"""
        return self._rho

    def _set_rho(self, value):
        """setter of rho"""
        check_var("rho", value, "float", Vmin=0)
        self._rho = value

    rho = property(
        fget=_get_rho,
        fset=_set_rho,
        doc="""mass per unit volume [kg/m3]

        :Type: float
        :min: 0
        """,
    )

    def _get_Ex(self):
        """getter of Ex"""
        return self._Ex

    def _set_Ex(self, value):
        """setter of Ex"""
        check_var("Ex", value, "float", Vmin=0)
        self._Ex = value

    Ex = property(
        fget=_get_Ex,
        fset=_set_Ex,
        doc="""equivalent Young modulus (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_Ey(self):
        """getter of Ey"""
        return self._Ey

    def _set_Ey(self, value):
        """setter of Ey"""
        check_var("Ey", value, "float", Vmin=0)
        self._Ey = value

    Ey = property(
        fget=_get_Ey,
        fset=_set_Ey,
        doc="""equivalent Young modulus (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_Ez(self):
        """getter of Ez"""
        return self._Ez

    def _set_Ez(self, value):
        """setter of Ez"""
        check_var("Ez", value, "float", Vmin=0)
        self._Ez = value

    Ez = property(
        fget=_get_Ez,
        fset=_set_Ez,
        doc="""equivalent Young modulus (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_nu_xy(self):
        """getter of nu_xy"""
        return self._nu_xy

    def _set_nu_xy(self, value):
        """setter of nu_xy"""
        check_var("nu_xy", value, "float", Vmin=0)
        self._nu_xy = value

    nu_xy = property(
        fget=_get_nu_xy,
        fset=_set_nu_xy,
        doc="""equivalent Poisson ratio in the XY plane (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_nu_xz(self):
        """getter of nu_xz"""
        return self._nu_xz

    def _set_nu_xz(self, value):
        """setter of nu_xz"""
        check_var("nu_xz", value, "float", Vmin=0)
        self._nu_xz = value

    nu_xz = property(
        fget=_get_nu_xz,
        fset=_set_nu_xz,
        doc="""equivalent Poisson ratio in the XZ plane (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_nu_yz(self):
        """getter of nu_yz"""
        return self._nu_yz

    def _set_nu_yz(self, value):
        """setter of nu_yz"""
        check_var("nu_yz", value, "float", Vmin=0)
        self._nu_yz = value

    nu_yz = property(
        fget=_get_nu_yz,
        fset=_set_nu_yz,
        doc="""equivalent Poisson ratio in the YZ plane (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_Gxz(self):
        """getter of Gxz"""
        return self._Gxz

    def _set_Gxz(self, value):
        """setter of Gxz"""
        check_var("Gxz", value, "float", Vmin=0)
        self._Gxz = value

    Gxz = property(
        fget=_get_Gxz,
        fset=_set_Gxz,
        doc="""shear modulus in XY plane (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_Gxy(self):
        """getter of Gxy"""
        return self._Gxy

    def _set_Gxy(self, value):
        """setter of Gxy"""
        check_var("Gxy", value, "float", Vmin=0)
        self._Gxy = value

    Gxy = property(
        fget=_get_Gxy,
        fset=_set_Gxy,
        doc="""shear modulus in XZ plane (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )

    def _get_Gyz(self):
        """getter of Gyz"""
        return self._Gyz

    def _set_Gyz(self, value):
        """setter of Gyz"""
        check_var("Gyz", value, "float", Vmin=0)
        self._Gyz = value

    Gyz = property(
        fget=_get_Gyz,
        fset=_set_Gyz,
        doc="""shear modulus in YZ plane (XY is lamination plane, Z is rotation axis)

        :Type: float
        :min: 0
        """,
    )
