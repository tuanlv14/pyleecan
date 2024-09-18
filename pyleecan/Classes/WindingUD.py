# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/WindingUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/WindingUD
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
from .Winding import Winding

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.WindingUD.init_as_CW1L import init_as_CW1L
except ImportError as error:
    init_as_CW1L = error

try:
    from ..Methods.Machine.WindingUD.init_as_CW2LR import init_as_CW2LR
except ImportError as error:
    init_as_CW2LR = error

try:
    from ..Methods.Machine.WindingUD.init_as_CW2LT import init_as_CW2LT
except ImportError as error:
    init_as_CW2LT = error

try:
    from ..Methods.Machine.WindingUD.init_as_DWL import init_as_DWL
except ImportError as error:
    init_as_DWL = error

try:
    from ..Methods.Machine.WindingUD.import_from_csv import import_from_csv
except ImportError as error:
    import_from_csv = error


from numpy import array, array_equal
from numpy import isnan
from ._check import InitUnKnowClassError


class WindingUD(Winding):
    """User defined winding"""

    VERSION = 1
    NAME = "User defined"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.WindingUD.init_as_CW1L
    if isinstance(init_as_CW1L, ImportError):
        init_as_CW1L = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_CW1L: " + str(init_as_CW1L)
                )
            )
        )
    else:
        init_as_CW1L = init_as_CW1L
    # cf Methods.Machine.WindingUD.init_as_CW2LR
    if isinstance(init_as_CW2LR, ImportError):
        init_as_CW2LR = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_CW2LR: " + str(init_as_CW2LR)
                )
            )
        )
    else:
        init_as_CW2LR = init_as_CW2LR
    # cf Methods.Machine.WindingUD.init_as_CW2LT
    if isinstance(init_as_CW2LT, ImportError):
        init_as_CW2LT = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_CW2LT: " + str(init_as_CW2LT)
                )
            )
        )
    else:
        init_as_CW2LT = init_as_CW2LT
    # cf Methods.Machine.WindingUD.init_as_DWL
    if isinstance(init_as_DWL, ImportError):
        init_as_DWL = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method init_as_DWL: " + str(init_as_DWL)
                )
            )
        )
    else:
        init_as_DWL = init_as_DWL
    # cf Methods.Machine.WindingUD.import_from_csv
    if isinstance(import_from_csv, ImportError):
        import_from_csv = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingUD method import_from_csv: "
                    + str(import_from_csv)
                )
            )
        )
    else:
        import_from_csv = import_from_csv
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
        # Call Winding init
        super(WindingUD, self).__init__(
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcp=Npcp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
            coil_pitch=coil_pitch,
            wind_mat=wind_mat,
            Nlayer=Nlayer,
            per_a=per_a,
            is_aper_a=is_aper_a,
            end_winding=end_winding,
            is_reverse_layer=is_reverse_layer,
            is_change_layer=is_change_layer,
            is_permute_B_C=is_permute_B_C,
            dual_tri_phase_shift=dual_tri_phase_shift,
            is_wye=is_wye,
        )
        # The class is frozen (in Winding init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        WindingUD_str = ""
        # Get the properties inherited from Winding
        WindingUD_str += super(WindingUD, self).__str__()
        return WindingUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Winding
        if not super(WindingUD, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Winding
        diff_list.extend(
            super(WindingUD, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Winding
        S += super(WindingUD, self).__sizeof__()
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

        # Get the properties inherited from Winding
        WindingUD_dict = super(WindingUD, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        WindingUD_dict["__class__"] = "WindingUD"
        return WindingUD_dict

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

        # Set to None the properties inherited from Winding
        super(WindingUD, self)._set_None()
