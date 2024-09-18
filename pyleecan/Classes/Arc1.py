# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Geometry/Arc1.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Geometry/Arc1
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
from .Arc import Arc

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Geometry.Arc1.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Geometry.Arc1.comp_length import comp_length
except ImportError as error:
    comp_length = error

try:
    from ..Methods.Geometry.Arc1.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Geometry.Arc1.discretize import discretize
except ImportError as error:
    discretize = error

try:
    from ..Methods.Geometry.Arc1.get_angle import get_angle
except ImportError as error:
    get_angle = error

try:
    from ..Methods.Geometry.Arc1.get_begin import get_begin
except ImportError as error:
    get_begin = error

try:
    from ..Methods.Geometry.Arc1.get_center import get_center
except ImportError as error:
    get_center = error

try:
    from ..Methods.Geometry.Arc1.get_end import get_end
except ImportError as error:
    get_end = error

try:
    from ..Methods.Geometry.Arc1.get_middle import get_middle
except ImportError as error:
    get_middle = error

try:
    from ..Methods.Geometry.Arc1.reverse import reverse
except ImportError as error:
    reverse = error

try:
    from ..Methods.Geometry.Arc1.rotate import rotate
except ImportError as error:
    rotate = error

try:
    from ..Methods.Geometry.Arc1.scale import scale
except ImportError as error:
    scale = error

try:
    from ..Methods.Geometry.Arc1.split_half import split_half
except ImportError as error:
    split_half = error

try:
    from ..Methods.Geometry.Arc1.translate import translate
except ImportError as error:
    translate = error

try:
    from ..Methods.Geometry.Arc1.split_point import split_point
except ImportError as error:
    split_point = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Arc1(Arc):
    """An arc between two points (defined by a radius)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Geometry.Arc1.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Geometry.Arc1.comp_length
    if isinstance(comp_length, ImportError):
        comp_length = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method comp_length: " + str(comp_length))
            )
        )
    else:
        comp_length = comp_length
    # cf Methods.Geometry.Arc1.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Geometry.Arc1.discretize
    if isinstance(discretize, ImportError):
        discretize = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method discretize: " + str(discretize))
            )
        )
    else:
        discretize = discretize
    # cf Methods.Geometry.Arc1.get_angle
    if isinstance(get_angle, ImportError):
        get_angle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method get_angle: " + str(get_angle))
            )
        )
    else:
        get_angle = get_angle
    # cf Methods.Geometry.Arc1.get_begin
    if isinstance(get_begin, ImportError):
        get_begin = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method get_begin: " + str(get_begin))
            )
        )
    else:
        get_begin = get_begin
    # cf Methods.Geometry.Arc1.get_center
    if isinstance(get_center, ImportError):
        get_center = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method get_center: " + str(get_center))
            )
        )
    else:
        get_center = get_center
    # cf Methods.Geometry.Arc1.get_end
    if isinstance(get_end, ImportError):
        get_end = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method get_end: " + str(get_end))
            )
        )
    else:
        get_end = get_end
    # cf Methods.Geometry.Arc1.get_middle
    if isinstance(get_middle, ImportError):
        get_middle = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method get_middle: " + str(get_middle))
            )
        )
    else:
        get_middle = get_middle
    # cf Methods.Geometry.Arc1.reverse
    if isinstance(reverse, ImportError):
        reverse = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method reverse: " + str(reverse))
            )
        )
    else:
        reverse = reverse
    # cf Methods.Geometry.Arc1.rotate
    if isinstance(rotate, ImportError):
        rotate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method rotate: " + str(rotate))
            )
        )
    else:
        rotate = rotate
    # cf Methods.Geometry.Arc1.scale
    if isinstance(scale, ImportError):
        scale = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method scale: " + str(scale))
            )
        )
    else:
        scale = scale
    # cf Methods.Geometry.Arc1.split_half
    if isinstance(split_half, ImportError):
        split_half = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method split_half: " + str(split_half))
            )
        )
    else:
        split_half = split_half
    # cf Methods.Geometry.Arc1.translate
    if isinstance(translate, ImportError):
        translate = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method translate: " + str(translate))
            )
        )
    else:
        translate = translate
    # cf Methods.Geometry.Arc1.split_point
    if isinstance(split_point, ImportError):
        split_point = property(
            fget=lambda x: raise_(
                ImportError("Can't use Arc1 method split_point: " + str(split_point))
            )
        )
    else:
        split_point = split_point
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        begin=0,
        end=0,
        radius=0,
        is_trigo_direction=True,
        prop_dict=None,
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
            if "begin" in list(init_dict.keys()):
                begin = init_dict["begin"]
            if "end" in list(init_dict.keys()):
                end = init_dict["end"]
            if "radius" in list(init_dict.keys()):
                radius = init_dict["radius"]
            if "is_trigo_direction" in list(init_dict.keys()):
                is_trigo_direction = init_dict["is_trigo_direction"]
            if "prop_dict" in list(init_dict.keys()):
                prop_dict = init_dict["prop_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.begin = begin
        self.end = end
        self.radius = radius
        self.is_trigo_direction = is_trigo_direction
        # Call Arc init
        super(Arc1, self).__init__(prop_dict=prop_dict)
        # The class is frozen (in Arc init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Arc1_str = ""
        # Get the properties inherited from Arc
        Arc1_str += super(Arc1, self).__str__()
        Arc1_str += "begin = " + str(self.begin) + linesep
        Arc1_str += "end = " + str(self.end) + linesep
        Arc1_str += "radius = " + str(self.radius) + linesep
        Arc1_str += "is_trigo_direction = " + str(self.is_trigo_direction) + linesep
        return Arc1_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Arc
        if not super(Arc1, self).__eq__(other):
            return False
        if other.begin != self.begin:
            return False
        if other.end != self.end:
            return False
        if other.radius != self.radius:
            return False
        if other.is_trigo_direction != self.is_trigo_direction:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Arc
        diff_list.extend(
            super(Arc1, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._begin != self._begin:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._begin) + ", other=" + str(other._begin) + ")"
                )
                diff_list.append(name + ".begin" + val_str)
            else:
                diff_list.append(name + ".begin")
        if other._end != self._end:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._end) + ", other=" + str(other._end) + ")"
                )
                diff_list.append(name + ".end" + val_str)
            else:
                diff_list.append(name + ".end")
        if (
            other._radius is not None
            and self._radius is not None
            and isnan(other._radius)
            and isnan(self._radius)
        ):
            pass
        elif other._radius != self._radius:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._radius)
                    + ", other="
                    + str(other._radius)
                    + ")"
                )
                diff_list.append(name + ".radius" + val_str)
            else:
                diff_list.append(name + ".radius")
        if other._is_trigo_direction != self._is_trigo_direction:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_trigo_direction)
                    + ", other="
                    + str(other._is_trigo_direction)
                    + ")"
                )
                diff_list.append(name + ".is_trigo_direction" + val_str)
            else:
                diff_list.append(name + ".is_trigo_direction")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Arc
        S += super(Arc1, self).__sizeof__()
        S += getsizeof(self.begin)
        S += getsizeof(self.end)
        S += getsizeof(self.radius)
        S += getsizeof(self.is_trigo_direction)
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

        # Get the properties inherited from Arc
        Arc1_dict = super(Arc1, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.begin is None:
            Arc1_dict["begin"] = None
        elif isinstance(self.begin, float):
            Arc1_dict["begin"] = self.begin
        else:
            Arc1_dict["begin"] = str(self.begin)
        if self.end is None:
            Arc1_dict["end"] = None
        elif isinstance(self.end, float):
            Arc1_dict["end"] = self.end
        else:
            Arc1_dict["end"] = str(self.end)
        Arc1_dict["radius"] = self.radius
        Arc1_dict["is_trigo_direction"] = self.is_trigo_direction
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        Arc1_dict["__class__"] = "Arc1"
        return Arc1_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        begin_val = self.begin
        end_val = self.end
        radius_val = self.radius
        is_trigo_direction_val = self.is_trigo_direction
        if self.prop_dict is None:
            prop_dict_val = None
        else:
            prop_dict_val = self.prop_dict.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            begin=begin_val,
            end=end_val,
            radius=radius_val,
            is_trigo_direction=is_trigo_direction_val,
            prop_dict=prop_dict_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.begin = None
        self.end = None
        self.radius = None
        self.is_trigo_direction = None
        # Set to None the properties inherited from Arc
        super(Arc1, self)._set_None()

    def _get_begin(self):
        """getter of begin"""
        return self._begin

    def _set_begin(self, value):
        """setter of begin"""
        if isinstance(value, str):
            value = complex(value)
        check_var("begin", value, "complex")
        self._begin = value

    begin = property(
        fget=_get_begin,
        fset=_set_begin,
        doc="""begin point of the arc

        :Type: complex
        """,
    )

    def _get_end(self):
        """getter of end"""
        return self._end

    def _set_end(self, value):
        """setter of end"""
        if isinstance(value, str):
            value = complex(value)
        check_var("end", value, "complex")
        self._end = value

    end = property(
        fget=_get_end,
        fset=_set_end,
        doc="""end point of the arc

        :Type: complex
        """,
    )

    def _get_radius(self):
        """getter of radius"""
        return self._radius

    def _set_radius(self, value):
        """setter of radius"""
        check_var("radius", value, "float")
        self._radius = value

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        doc="""Radius of the arc (can be + or -)

        :Type: float
        """,
    )

    def _get_is_trigo_direction(self):
        """getter of is_trigo_direction"""
        return self._is_trigo_direction

    def _set_is_trigo_direction(self, value):
        """setter of is_trigo_direction"""
        check_var("is_trigo_direction", value, "bool")
        self._is_trigo_direction = value

    is_trigo_direction = property(
        fget=_get_is_trigo_direction,
        fset=_set_is_trigo_direction,
        doc="""Rotation direction of the arc

        :Type: bool
        """,
    )
