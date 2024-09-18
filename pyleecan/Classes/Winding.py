# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Winding.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Winding
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.Winding.comp_connection_mat import comp_connection_mat
except ImportError as error:
    comp_connection_mat = error

try:
    from ..Methods.Machine.Winding.comp_length_endwinding import comp_length_endwinding
except ImportError as error:
    comp_length_endwinding = error

try:
    from ..Methods.Machine.Winding.comp_Ncspc import comp_Ncspc
except ImportError as error:
    comp_Ncspc = error

try:
    from ..Methods.Machine.Winding.comp_Ntsp import comp_Ntsp
except ImportError as error:
    comp_Ntsp = error

try:
    from ..Methods.Machine.Winding.comp_periodicity import comp_periodicity
except ImportError as error:
    comp_periodicity = error

try:
    from ..Methods.Machine.Winding.comp_phasor_angle import comp_phasor_angle
except ImportError as error:
    comp_phasor_angle = error

try:
    from ..Methods.Machine.Winding.comp_winding_factor import comp_winding_factor
except ImportError as error:
    comp_winding_factor = error

try:
    from ..Methods.Machine.Winding.get_connection_mat import get_connection_mat
except ImportError as error:
    get_connection_mat = error

try:
    from ..Methods.Machine.Winding.get_dim_wind import get_dim_wind
except ImportError as error:
    get_dim_wind = error

try:
    from ..Methods.Machine.Winding.get_periodicity import get_periodicity
except ImportError as error:
    get_periodicity = error

try:
    from ..Methods.Machine.Winding.export_to_csv import export_to_csv
except ImportError as error:
    export_to_csv = error

try:
    from ..Methods.Machine.Winding.clean import clean
except ImportError as error:
    clean = error

try:
    from ..Methods.Machine.Winding.plot_radial import plot_radial
except ImportError as error:
    plot_radial = error

try:
    from ..Methods.Machine.Winding.plot_linear import plot_linear
except ImportError as error:
    plot_linear = error

try:
    from ..Methods.Machine.Winding.comp_Ncps import comp_Ncps
except ImportError as error:
    comp_Ncps = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class Winding(FrozenClass):
    """Winding class generating connection matrix using Star of slots method (coupling with SWAT-EM)"""

    VERSION = 1
    NAME = "Star of slots"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Winding.comp_connection_mat
    if isinstance(comp_connection_mat, ImportError):
        comp_connection_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_connection_mat: "
                    + str(comp_connection_mat)
                )
            )
        )
    else:
        comp_connection_mat = comp_connection_mat
    # cf Methods.Machine.Winding.comp_length_endwinding
    if isinstance(comp_length_endwinding, ImportError):
        comp_length_endwinding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_length_endwinding: "
                    + str(comp_length_endwinding)
                )
            )
        )
    else:
        comp_length_endwinding = comp_length_endwinding
    # cf Methods.Machine.Winding.comp_Ncspc
    if isinstance(comp_Ncspc, ImportError):
        comp_Ncspc = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method comp_Ncspc: " + str(comp_Ncspc))
            )
        )
    else:
        comp_Ncspc = comp_Ncspc
    # cf Methods.Machine.Winding.comp_Ntsp
    if isinstance(comp_Ntsp, ImportError):
        comp_Ntsp = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method comp_Ntsp: " + str(comp_Ntsp))
            )
        )
    else:
        comp_Ntsp = comp_Ntsp
    # cf Methods.Machine.Winding.comp_periodicity
    if isinstance(comp_periodicity, ImportError):
        comp_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_periodicity: "
                    + str(comp_periodicity)
                )
            )
        )
    else:
        comp_periodicity = comp_periodicity
    # cf Methods.Machine.Winding.comp_phasor_angle
    if isinstance(comp_phasor_angle, ImportError):
        comp_phasor_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_phasor_angle: "
                    + str(comp_phasor_angle)
                )
            )
        )
    else:
        comp_phasor_angle = comp_phasor_angle
    # cf Methods.Machine.Winding.comp_winding_factor
    if isinstance(comp_winding_factor, ImportError):
        comp_winding_factor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_winding_factor: "
                    + str(comp_winding_factor)
                )
            )
        )
    else:
        comp_winding_factor = comp_winding_factor
    # cf Methods.Machine.Winding.get_connection_mat
    if isinstance(get_connection_mat, ImportError):
        get_connection_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method get_connection_mat: "
                    + str(get_connection_mat)
                )
            )
        )
    else:
        get_connection_mat = get_connection_mat
    # cf Methods.Machine.Winding.get_dim_wind
    if isinstance(get_dim_wind, ImportError):
        get_dim_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method get_dim_wind: " + str(get_dim_wind)
                )
            )
        )
    else:
        get_dim_wind = get_dim_wind
    # cf Methods.Machine.Winding.get_periodicity
    if isinstance(get_periodicity, ImportError):
        get_periodicity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method get_periodicity: " + str(get_periodicity)
                )
            )
        )
    else:
        get_periodicity = get_periodicity
    # cf Methods.Machine.Winding.export_to_csv
    if isinstance(export_to_csv, ImportError):
        export_to_csv = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method export_to_csv: " + str(export_to_csv)
                )
            )
        )
    else:
        export_to_csv = export_to_csv
    # cf Methods.Machine.Winding.clean
    if isinstance(clean, ImportError):
        clean = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method clean: " + str(clean))
            )
        )
    else:
        clean = clean
    # cf Methods.Machine.Winding.plot_radial
    if isinstance(plot_radial, ImportError):
        plot_radial = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method plot_radial: " + str(plot_radial))
            )
        )
    else:
        plot_radial = plot_radial
    # cf Methods.Machine.Winding.plot_linear
    if isinstance(plot_linear, ImportError):
        plot_linear = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method plot_linear: " + str(plot_linear))
            )
        )
    else:
        plot_linear = plot_linear
    # cf Methods.Machine.Winding.comp_Ncps
    if isinstance(comp_Ncps, ImportError):
        comp_Ncps = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method comp_Ncps: " + str(comp_Ncps))
            )
        )
    else:
        comp_Ncps = comp_Ncps
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        coil_pitch=1,
        wind_mat=None,
        Nlayer=1,
        per_a=None,
        is_aper_a=None,
        end_winding=-1,
        is_reverse_layer=False,
        is_change_layer=False,
        is_permute_B_C=False,
        dual_tri_phase_shift=None,
        is_wye=True,
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
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcp" in list(init_dict.keys()):
                Npcp = init_dict["Npcp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "wind_mat" in list(init_dict.keys()):
                wind_mat = init_dict["wind_mat"]
            if "Nlayer" in list(init_dict.keys()):
                Nlayer = init_dict["Nlayer"]
            if "per_a" in list(init_dict.keys()):
                per_a = init_dict["per_a"]
            if "is_aper_a" in list(init_dict.keys()):
                is_aper_a = init_dict["is_aper_a"]
            if "end_winding" in list(init_dict.keys()):
                end_winding = init_dict["end_winding"]
            if "is_reverse_layer" in list(init_dict.keys()):
                is_reverse_layer = init_dict["is_reverse_layer"]
            if "is_change_layer" in list(init_dict.keys()):
                is_change_layer = init_dict["is_change_layer"]
            if "is_permute_B_C" in list(init_dict.keys()):
                is_permute_B_C = init_dict["is_permute_B_C"]
            if "dual_tri_phase_shift" in list(init_dict.keys()):
                dual_tri_phase_shift = init_dict["dual_tri_phase_shift"]
            if "is_wye" in list(init_dict.keys()):
                is_wye = init_dict["is_wye"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_reverse_wind = is_reverse_wind
        self.Nslot_shift_wind = Nslot_shift_wind
        self.qs = qs
        self.Ntcoil = Ntcoil
        self.Npcp = Npcp
        self.type_connection = type_connection
        self.p = p
        self.Lewout = Lewout
        self.conductor = conductor
        self.coil_pitch = coil_pitch
        self.wind_mat = wind_mat
        self.Nlayer = Nlayer
        self.per_a = per_a
        self.is_aper_a = is_aper_a
        self.end_winding = end_winding
        self.is_reverse_layer = is_reverse_layer
        self.is_change_layer = is_change_layer
        self.is_permute_B_C = is_permute_B_C
        self.dual_tri_phase_shift = dual_tri_phase_shift
        self.is_wye = is_wye

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Winding_str = ""
        if self.parent is None:
            Winding_str += "parent = None " + linesep
        else:
            Winding_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Winding_str += "is_reverse_wind = " + str(self.is_reverse_wind) + linesep
        Winding_str += "Nslot_shift_wind = " + str(self.Nslot_shift_wind) + linesep
        Winding_str += "qs = " + str(self.qs) + linesep
        Winding_str += "Ntcoil = " + str(self.Ntcoil) + linesep
        Winding_str += "Npcp = " + str(self.Npcp) + linesep
        Winding_str += "type_connection = " + str(self.type_connection) + linesep
        Winding_str += "p = " + str(self.p) + linesep
        Winding_str += "Lewout = " + str(self.Lewout) + linesep
        if self.conductor is not None:
            tmp = self.conductor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Winding_str += "conductor = " + tmp
        else:
            Winding_str += "conductor = None" + linesep + linesep
        Winding_str += "coil_pitch = " + str(self.coil_pitch) + linesep
        Winding_str += (
            "wind_mat = "
            + linesep
            + str(self.wind_mat).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        Winding_str += "Nlayer = " + str(self.Nlayer) + linesep
        Winding_str += "per_a = " + str(self.per_a) + linesep
        Winding_str += "is_aper_a = " + str(self.is_aper_a) + linesep
        if self.end_winding is not None:
            tmp = (
                self.end_winding.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            Winding_str += "end_winding = " + tmp
        else:
            Winding_str += "end_winding = None" + linesep + linesep
        Winding_str += "is_reverse_layer = " + str(self.is_reverse_layer) + linesep
        Winding_str += "is_change_layer = " + str(self.is_change_layer) + linesep
        Winding_str += "is_permute_B_C = " + str(self.is_permute_B_C) + linesep
        Winding_str += (
            "dual_tri_phase_shift = " + str(self.dual_tri_phase_shift) + linesep
        )
        Winding_str += "is_wye = " + str(self.is_wye) + linesep
        return Winding_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_reverse_wind != self.is_reverse_wind:
            return False
        if other.Nslot_shift_wind != self.Nslot_shift_wind:
            return False
        if other.qs != self.qs:
            return False
        if other.Ntcoil != self.Ntcoil:
            return False
        if other.Npcp != self.Npcp:
            return False
        if other.type_connection != self.type_connection:
            return False
        if other.p != self.p:
            return False
        if other.Lewout != self.Lewout:
            return False
        if other.conductor != self.conductor:
            return False
        if other.coil_pitch != self.coil_pitch:
            return False
        if not array_equal(other.wind_mat, self.wind_mat):
            return False
        if other.Nlayer != self.Nlayer:
            return False
        if other.per_a != self.per_a:
            return False
        if other.is_aper_a != self.is_aper_a:
            return False
        if other.end_winding != self.end_winding:
            return False
        if other.is_reverse_layer != self.is_reverse_layer:
            return False
        if other.is_change_layer != self.is_change_layer:
            return False
        if other.is_permute_B_C != self.is_permute_B_C:
            return False
        if other.dual_tri_phase_shift != self.dual_tri_phase_shift:
            return False
        if other.is_wye != self.is_wye:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._is_reverse_wind != self._is_reverse_wind:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_reverse_wind)
                    + ", other="
                    + str(other._is_reverse_wind)
                    + ")"
                )
                diff_list.append(name + ".is_reverse_wind" + val_str)
            else:
                diff_list.append(name + ".is_reverse_wind")
        if other._Nslot_shift_wind != self._Nslot_shift_wind:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Nslot_shift_wind)
                    + ", other="
                    + str(other._Nslot_shift_wind)
                    + ")"
                )
                diff_list.append(name + ".Nslot_shift_wind" + val_str)
            else:
                diff_list.append(name + ".Nslot_shift_wind")
        if other._qs != self._qs:
            if is_add_value:
                val_str = " (self=" + str(self._qs) + ", other=" + str(other._qs) + ")"
                diff_list.append(name + ".qs" + val_str)
            else:
                diff_list.append(name + ".qs")
        if other._Ntcoil != self._Ntcoil:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Ntcoil)
                    + ", other="
                    + str(other._Ntcoil)
                    + ")"
                )
                diff_list.append(name + ".Ntcoil" + val_str)
            else:
                diff_list.append(name + ".Ntcoil")
        if other._Npcp != self._Npcp:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Npcp) + ", other=" + str(other._Npcp) + ")"
                )
                diff_list.append(name + ".Npcp" + val_str)
            else:
                diff_list.append(name + ".Npcp")
        if other._type_connection != self._type_connection:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_connection)
                    + ", other="
                    + str(other._type_connection)
                    + ")"
                )
                diff_list.append(name + ".type_connection" + val_str)
            else:
                diff_list.append(name + ".type_connection")
        if other._p != self._p:
            if is_add_value:
                val_str = " (self=" + str(self._p) + ", other=" + str(other._p) + ")"
                diff_list.append(name + ".p" + val_str)
            else:
                diff_list.append(name + ".p")
        if (
            other._Lewout is not None
            and self._Lewout is not None
            and isnan(other._Lewout)
            and isnan(self._Lewout)
        ):
            pass
        elif other._Lewout != self._Lewout:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Lewout)
                    + ", other="
                    + str(other._Lewout)
                    + ")"
                )
                diff_list.append(name + ".Lewout" + val_str)
            else:
                diff_list.append(name + ".Lewout")
        if (other.conductor is None and self.conductor is not None) or (
            other.conductor is not None and self.conductor is None
        ):
            diff_list.append(name + ".conductor None mismatch")
        elif self.conductor is not None:
            diff_list.extend(
                self.conductor.compare(
                    other.conductor,
                    name=name + ".conductor",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._coil_pitch != self._coil_pitch:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._coil_pitch)
                    + ", other="
                    + str(other._coil_pitch)
                    + ")"
                )
                diff_list.append(name + ".coil_pitch" + val_str)
            else:
                diff_list.append(name + ".coil_pitch")
        if not array_equal(other.wind_mat, self.wind_mat):
            diff_list.append(name + ".wind_mat")
        if other._Nlayer != self._Nlayer:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Nlayer)
                    + ", other="
                    + str(other._Nlayer)
                    + ")"
                )
                diff_list.append(name + ".Nlayer" + val_str)
            else:
                diff_list.append(name + ".Nlayer")
        if other._per_a != self._per_a:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._per_a) + ", other=" + str(other._per_a) + ")"
                )
                diff_list.append(name + ".per_a" + val_str)
            else:
                diff_list.append(name + ".per_a")
        if other._is_aper_a != self._is_aper_a:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_aper_a)
                    + ", other="
                    + str(other._is_aper_a)
                    + ")"
                )
                diff_list.append(name + ".is_aper_a" + val_str)
            else:
                diff_list.append(name + ".is_aper_a")
        if (other.end_winding is None and self.end_winding is not None) or (
            other.end_winding is not None and self.end_winding is None
        ):
            diff_list.append(name + ".end_winding None mismatch")
        elif self.end_winding is not None:
            diff_list.extend(
                self.end_winding.compare(
                    other.end_winding,
                    name=name + ".end_winding",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if other._is_reverse_layer != self._is_reverse_layer:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_reverse_layer)
                    + ", other="
                    + str(other._is_reverse_layer)
                    + ")"
                )
                diff_list.append(name + ".is_reverse_layer" + val_str)
            else:
                diff_list.append(name + ".is_reverse_layer")
        if other._is_change_layer != self._is_change_layer:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_change_layer)
                    + ", other="
                    + str(other._is_change_layer)
                    + ")"
                )
                diff_list.append(name + ".is_change_layer" + val_str)
            else:
                diff_list.append(name + ".is_change_layer")
        if other._is_permute_B_C != self._is_permute_B_C:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_permute_B_C)
                    + ", other="
                    + str(other._is_permute_B_C)
                    + ")"
                )
                diff_list.append(name + ".is_permute_B_C" + val_str)
            else:
                diff_list.append(name + ".is_permute_B_C")
        if (
            other._dual_tri_phase_shift is not None
            and self._dual_tri_phase_shift is not None
            and isnan(other._dual_tri_phase_shift)
            and isnan(self._dual_tri_phase_shift)
        ):
            pass
        elif other._dual_tri_phase_shift != self._dual_tri_phase_shift:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._dual_tri_phase_shift)
                    + ", other="
                    + str(other._dual_tri_phase_shift)
                    + ")"
                )
                diff_list.append(name + ".dual_tri_phase_shift" + val_str)
            else:
                diff_list.append(name + ".dual_tri_phase_shift")
        if other._is_wye != self._is_wye:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_wye)
                    + ", other="
                    + str(other._is_wye)
                    + ")"
                )
                diff_list.append(name + ".is_wye" + val_str)
            else:
                diff_list.append(name + ".is_wye")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.is_reverse_wind)
        S += getsizeof(self.Nslot_shift_wind)
        S += getsizeof(self.qs)
        S += getsizeof(self.Ntcoil)
        S += getsizeof(self.Npcp)
        S += getsizeof(self.type_connection)
        S += getsizeof(self.p)
        S += getsizeof(self.Lewout)
        S += getsizeof(self.conductor)
        S += getsizeof(self.coil_pitch)
        S += getsizeof(self.wind_mat)
        S += getsizeof(self.Nlayer)
        S += getsizeof(self.per_a)
        S += getsizeof(self.is_aper_a)
        S += getsizeof(self.end_winding)
        S += getsizeof(self.is_reverse_layer)
        S += getsizeof(self.is_change_layer)
        S += getsizeof(self.is_permute_B_C)
        S += getsizeof(self.dual_tri_phase_shift)
        S += getsizeof(self.is_wye)
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

        Winding_dict = dict()
        Winding_dict["is_reverse_wind"] = self.is_reverse_wind
        Winding_dict["Nslot_shift_wind"] = self.Nslot_shift_wind
        Winding_dict["qs"] = self.qs
        Winding_dict["Ntcoil"] = self.Ntcoil
        Winding_dict["Npcp"] = self.Npcp
        Winding_dict["type_connection"] = self.type_connection
        Winding_dict["p"] = self.p
        Winding_dict["Lewout"] = self.Lewout
        if self.conductor is None:
            Winding_dict["conductor"] = None
        else:
            Winding_dict["conductor"] = self.conductor.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Winding_dict["coil_pitch"] = self.coil_pitch
        if self.wind_mat is None:
            Winding_dict["wind_mat"] = None
        else:
            if type_handle_ndarray == 0:
                Winding_dict["wind_mat"] = self.wind_mat.tolist()
            elif type_handle_ndarray == 1:
                Winding_dict["wind_mat"] = self.wind_mat.copy()
            elif type_handle_ndarray == 2:
                Winding_dict["wind_mat"] = self.wind_mat
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        Winding_dict["Nlayer"] = self.Nlayer
        Winding_dict["per_a"] = self.per_a
        Winding_dict["is_aper_a"] = self.is_aper_a
        if self.end_winding is None:
            Winding_dict["end_winding"] = None
        else:
            Winding_dict["end_winding"] = self.end_winding.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        Winding_dict["is_reverse_layer"] = self.is_reverse_layer
        Winding_dict["is_change_layer"] = self.is_change_layer
        Winding_dict["is_permute_B_C"] = self.is_permute_B_C
        Winding_dict["dual_tri_phase_shift"] = self.dual_tri_phase_shift
        Winding_dict["is_wye"] = self.is_wye
        # The class name is added to the dict for deserialisation purpose
        Winding_dict["__class__"] = "Winding"
        return Winding_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        is_reverse_wind_val = self.is_reverse_wind
        Nslot_shift_wind_val = self.Nslot_shift_wind
        qs_val = self.qs
        Ntcoil_val = self.Ntcoil
        Npcp_val = self.Npcp
        type_connection_val = self.type_connection
        p_val = self.p
        Lewout_val = self.Lewout
        if self.conductor is None:
            conductor_val = None
        else:
            conductor_val = self.conductor.copy()
        coil_pitch_val = self.coil_pitch
        if self.wind_mat is None:
            wind_mat_val = None
        else:
            wind_mat_val = self.wind_mat.copy()
        Nlayer_val = self.Nlayer
        per_a_val = self.per_a
        is_aper_a_val = self.is_aper_a
        if self.end_winding is None:
            end_winding_val = None
        else:
            end_winding_val = self.end_winding.copy()
        is_reverse_layer_val = self.is_reverse_layer
        is_change_layer_val = self.is_change_layer
        is_permute_B_C_val = self.is_permute_B_C
        dual_tri_phase_shift_val = self.dual_tri_phase_shift
        is_wye_val = self.is_wye
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            is_reverse_wind=is_reverse_wind_val,
            Nslot_shift_wind=Nslot_shift_wind_val,
            qs=qs_val,
            Ntcoil=Ntcoil_val,
            Npcp=Npcp_val,
            type_connection=type_connection_val,
            p=p_val,
            Lewout=Lewout_val,
            conductor=conductor_val,
            coil_pitch=coil_pitch_val,
            wind_mat=wind_mat_val,
            Nlayer=Nlayer_val,
            per_a=per_a_val,
            is_aper_a=is_aper_a_val,
            end_winding=end_winding_val,
            is_reverse_layer=is_reverse_layer_val,
            is_change_layer=is_change_layer_val,
            is_permute_B_C=is_permute_B_C_val,
            dual_tri_phase_shift=dual_tri_phase_shift_val,
            is_wye=is_wye_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_reverse_wind = None
        self.Nslot_shift_wind = None
        self.qs = None
        self.Ntcoil = None
        self.Npcp = None
        self.type_connection = None
        self.p = None
        self.Lewout = None
        if self.conductor is not None:
            self.conductor._set_None()
        self.coil_pitch = None
        self.wind_mat = None
        self.Nlayer = None
        self.per_a = None
        self.is_aper_a = None
        if self.end_winding is not None:
            self.end_winding._set_None()
        self.is_reverse_layer = None
        self.is_change_layer = None
        self.is_permute_B_C = None
        self.dual_tri_phase_shift = None
        self.is_wye = None

    def _get_is_reverse_wind(self):
        """getter of is_reverse_wind"""
        return self._is_reverse_wind

    def _set_is_reverse_wind(self, value):
        """setter of is_reverse_wind"""
        check_var("is_reverse_wind", value, "bool")
        self._is_reverse_wind = value

    is_reverse_wind = property(
        fget=_get_is_reverse_wind,
        fset=_set_is_reverse_wind,
        doc="""1 to reverse the default winding algorithm along the airgap (c, b, a instead of a, b, c along the trigonometric direction)

        :Type: bool
        """,
    )

    def _get_Nslot_shift_wind(self):
        """getter of Nslot_shift_wind"""
        return self._Nslot_shift_wind

    def _set_Nslot_shift_wind(self, value):
        """setter of Nslot_shift_wind"""
        check_var("Nslot_shift_wind", value, "int")
        self._Nslot_shift_wind = value

    Nslot_shift_wind = property(
        fget=_get_Nslot_shift_wind,
        fset=_set_Nslot_shift_wind,
        doc="""Number of slots to shift the coils obtained with pyleecan winding algorithm (a, b, c becomes b, c, a with Nslot_shift_wind=1)

        :Type: int
        """,
    )

    def _get_qs(self):
        """getter of qs"""
        return self._qs

    def _set_qs(self, value):
        """setter of qs"""
        check_var("qs", value, "int", Vmin=0)
        self._qs = value

    qs = property(
        fget=_get_qs,
        fset=_set_qs,
        doc="""number of phases 

        :Type: int
        :min: 0
        """,
    )

    def _get_Ntcoil(self):
        """getter of Ntcoil"""
        return self._Ntcoil

    def _set_Ntcoil(self, value):
        """setter of Ntcoil"""
        check_var("Ntcoil", value, "int", Vmin=1)
        self._Ntcoil = value

    Ntcoil = property(
        fget=_get_Ntcoil,
        fset=_set_Ntcoil,
        doc="""number of turns per coil

        :Type: int
        :min: 1
        """,
    )

    def _get_Npcp(self):
        """getter of Npcp"""
        return self._Npcp

    def _set_Npcp(self, value):
        """setter of Npcp"""
        check_var("Npcp", value, "int", Vmin=1)
        self._Npcp = value

    Npcp = property(
        fget=_get_Npcp,
        fset=_set_Npcp,
        doc="""number of parallel circuits per phase

        :Type: int
        :min: 1
        """,
    )

    def _get_type_connection(self):
        """getter of type_connection"""
        return self._type_connection

    def _set_type_connection(self, value):
        """setter of type_connection"""
        check_var("type_connection", value, "int", Vmin=-1, Vmax=1)
        self._type_connection = value

    type_connection = property(
        fget=_get_type_connection,
        fset=_set_type_connection,
        doc="""Winding connection : 0 star (Y), 1 triangle (delta), -1 no connection

        :Type: int
        :min: -1
        :max: 1
        """,
    )

    def _get_p(self):
        """getter of p"""
        return self._p

    def _set_p(self, value):
        """setter of p"""
        check_var("p", value, "int", Vmin=1)
        self._p = value

    p = property(
        fget=_get_p,
        fset=_set_p,
        doc="""pole pairs number

        :Type: int
        :min: 1
        """,
    )

    def _get_Lewout(self):
        """getter of Lewout"""
        return self._Lewout

    def _set_Lewout(self, value):
        """setter of Lewout"""
        check_var("Lewout", value, "float", Vmin=0)
        self._Lewout = value

    Lewout = property(
        fget=_get_Lewout,
        fset=_set_Lewout,
        doc="""straight length of the conductors outside the lamination before the curved part of winding overhang [m] - can be negative to tune the average turn length (only used in voltage driven simulations)

        :Type: float
        :min: 0
        """,
    )

    def _get_conductor(self):
        """getter of conductor"""
        return self._conductor

    def _set_conductor(self, value):
        """setter of conductor"""
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
                "pyleecan.Classes", value.get("__class__"), "conductor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Conductor = import_class("pyleecan.Classes", "Conductor", "conductor")
            value = Conductor()
        check_var("conductor", value, "Conductor")
        self._conductor = value

        if self._conductor is not None:
            self._conductor.parent = self

    conductor = property(
        fget=_get_conductor,
        fset=_set_conductor,
        doc="""Winding's conductor

        :Type: Conductor
        """,
    )

    def _get_coil_pitch(self):
        """getter of coil_pitch"""
        return self._coil_pitch

    def _set_coil_pitch(self, value):
        """setter of coil_pitch"""
        check_var("coil_pitch", value, "int")
        self._coil_pitch = value

    coil_pitch = property(
        fget=_get_coil_pitch,
        fset=_set_coil_pitch,
        doc="""Distance (in slot) between a conductor of a certain phase and the corresponding return conductor

        :Type: int
        """,
    )

    def _get_wind_mat(self):
        """getter of wind_mat"""
        return self._wind_mat

    def _set_wind_mat(self, value):
        """setter of wind_mat"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("wind_mat", value, "ndarray")
        self._wind_mat = value

    wind_mat = property(
        fget=_get_wind_mat,
        fset=_set_wind_mat,
        doc="""Winding matrix calculated with Star of slots (from SWAT_EM package)

        :Type: ndarray
        """,
    )

    def _get_Nlayer(self):
        """getter of Nlayer"""
        return self._Nlayer

    def _set_Nlayer(self, value):
        """setter of Nlayer"""
        check_var("Nlayer", value, "int", Vmin=1)
        self._Nlayer = value

    Nlayer = property(
        fget=_get_Nlayer,
        fset=_set_Nlayer,
        doc="""Number of different coils in a slot

        :Type: int
        :min: 1
        """,
    )

    def _get_per_a(self):
        """getter of per_a"""
        return self._per_a

    def _set_per_a(self, value):
        """setter of per_a"""
        check_var("per_a", value, "int", Vmin=1)
        self._per_a = value

    per_a = property(
        fget=_get_per_a,
        fset=_set_per_a,
        doc="""Number of spatial periods of the winding

        :Type: int
        :min: 1
        """,
    )

    def _get_is_aper_a(self):
        """getter of is_aper_a"""
        return self._is_aper_a

    def _set_is_aper_a(self, value):
        """setter of is_aper_a"""
        check_var("is_aper_a", value, "bool")
        self._is_aper_a = value

    is_aper_a = property(
        fget=_get_is_aper_a,
        fset=_set_is_aper_a,
        doc="""True if the winding is anti-periodic over space

        :Type: bool
        """,
    )

    def _get_end_winding(self):
        """getter of end_winding"""
        return self._end_winding

    def _set_end_winding(self, value):
        """setter of end_winding"""
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
                "pyleecan.Classes", value.get("__class__"), "end_winding"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            EndWinding = import_class("pyleecan.Classes", "EndWinding", "end_winding")
            value = EndWinding()
        check_var("end_winding", value, "EndWinding")
        self._end_winding = value

        if self._end_winding is not None:
            self._end_winding.parent = self

    end_winding = property(
        fget=_get_end_winding,
        fset=_set_end_winding,
        doc="""End Winding's definition

        :Type: EndWinding
        """,
    )

    def _get_is_reverse_layer(self):
        """getter of is_reverse_layer"""
        return self._is_reverse_layer

    def _set_is_reverse_layer(self, value):
        """setter of is_reverse_layer"""
        check_var("is_reverse_layer", value, "bool")
        self._is_reverse_layer = value

    is_reverse_layer = property(
        fget=_get_is_reverse_layer,
        fset=_set_is_reverse_layer,
        doc="""1 to reverse the layers (rad from 0 to Nrad-1 => Nrad-1 to 0)

        :Type: bool
        """,
    )

    def _get_is_change_layer(self):
        """getter of is_change_layer"""
        return self._is_change_layer

    def _set_is_change_layer(self, value):
        """setter of is_change_layer"""
        check_var("is_change_layer", value, "bool")
        self._is_change_layer = value

    is_change_layer = property(
        fget=_get_is_change_layer,
        fset=_set_is_change_layer,
        doc="""1 to change the layer from radial to tangential or tangential to radial

        :Type: bool
        """,
    )

    def _get_is_permute_B_C(self):
        """getter of is_permute_B_C"""
        return self._is_permute_B_C

    def _set_is_permute_B_C(self, value):
        """setter of is_permute_B_C"""
        check_var("is_permute_B_C", value, "bool")
        self._is_permute_B_C = value

    is_permute_B_C = property(
        fget=_get_is_permute_B_C,
        fset=_set_is_permute_B_C,
        doc="""True to permute phase B and phase C

        :Type: bool
        """,
    )

    def _get_dual_tri_phase_shift(self):
        """getter of dual_tri_phase_shift"""
        return self._dual_tri_phase_shift

    def _set_dual_tri_phase_shift(self, value):
        """setter of dual_tri_phase_shift"""
        check_var("dual_tri_phase_shift", value, "float")
        self._dual_tri_phase_shift = value

    dual_tri_phase_shift = property(
        fget=_get_dual_tri_phase_shift,
        fset=_set_dual_tri_phase_shift,
        doc="""Phase shift between both tri-phase systems in dual-tri-phase case

        :Type: float
        """,
    )

    def _get_is_wye(self):
        """getter of is_wye"""
        return self._is_wye

    def _set_is_wye(self, value):
        """setter of is_wye"""
        check_var("is_wye", value, "bool")
        self._is_wye = value

    is_wye = property(
        fget=_get_is_wye,
        fset=_set_is_wye,
        doc="""True if the alimentation is wye (else delta)

        :Type: bool
        """,
    )
