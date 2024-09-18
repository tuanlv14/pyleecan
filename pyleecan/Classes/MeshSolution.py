# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/MeshSolution.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/MeshSolution
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
    from ..Methods.Mesh.MeshSolution.get_solution import get_solution
except ImportError as error:
    get_solution = error

try:
    from ..Methods.Mesh.MeshSolution.get_field import get_field
except ImportError as error:
    get_field = error

try:
    from ..Methods.Mesh.MeshSolution.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from ..Methods.Mesh.MeshSolution.get_mesh_field_pv import get_mesh_field_pv
except ImportError as error:
    get_mesh_field_pv = error

try:
    from ..Methods.Mesh.MeshSolution.plot_mesh import plot_mesh
except ImportError as error:
    plot_mesh = error

try:
    from ..Methods.Mesh.MeshSolution.plot_contour import plot_contour
except ImportError as error:
    plot_contour = error

try:
    from ..Methods.Mesh.MeshSolution.plot_deflection import plot_deflection
except ImportError as error:
    plot_deflection = error

try:
    from ..Methods.Mesh.MeshSolution.plot_glyph import plot_glyph
except ImportError as error:
    plot_glyph = error

try:
    from ..Methods.Mesh.MeshSolution.perm_coord import perm_coord
except ImportError as error:
    perm_coord = error

try:
    from ..Methods.Mesh.MeshSolution.get_deflection import get_deflection
except ImportError as error:
    get_deflection = error

try:
    from ..Methods.Mesh.MeshSolution.get_glyph import get_glyph
except ImportError as error:
    get_glyph = error

try:
    from ..Methods.Mesh.MeshSolution.add_solution import add_solution
except ImportError as error:
    add_solution = error

try:
    from ..Methods.Mesh.MeshSolution.replace_solution import replace_solution
except ImportError as error:
    replace_solution = error

try:
    from ..Methods.Mesh.MeshSolution.pop_solution import pop_solution
except ImportError as error:
    pop_solution = error

try:
    from ..Methods.Mesh.MeshSolution.keys import keys
except ImportError as error:
    keys = error

try:
    from ..Methods.Mesh.MeshSolution.items import items
except ImportError as error:
    items = error

try:
    from ..Methods.Mesh.MeshSolution.values import values
except ImportError as error:
    values = error

try:
    from ..Methods.Mesh.MeshSolution.__getitem__ import __getitem__
except ImportError as error:
    __getitem__ = error

try:
    from ..Methods.Mesh.MeshSolution.__setitem__ import __setitem__
except ImportError as error:
    __setitem__ = error

try:
    from ..Methods.Mesh.MeshSolution.__iter__ import __iter__
except ImportError as error:
    __iter__ = error

try:
    from ..Methods.Mesh.MeshSolution.export_to_mat import export_to_mat
except ImportError as error:
    export_to_mat = error


from numpy import isnan
from ._check import InitUnKnowClassError


class MeshSolution(FrozenClass):
    """Abstract class to associate a mesh with one or several solutions"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshSolution.get_solution
    if isinstance(get_solution, ImportError):
        get_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_solution: " + str(get_solution)
                )
            )
        )
    else:
        get_solution = get_solution
    # cf Methods.Mesh.MeshSolution.get_field
    if isinstance(get_field, ImportError):
        get_field = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_field: " + str(get_field)
                )
            )
        )
    else:
        get_field = get_field
    # cf Methods.Mesh.MeshSolution.get_group
    if isinstance(get_group, ImportError):
        get_group = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_group: " + str(get_group)
                )
            )
        )
    else:
        get_group = get_group
    # cf Methods.Mesh.MeshSolution.get_mesh_field_pv
    if isinstance(get_mesh_field_pv, ImportError):
        get_mesh_field_pv = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_mesh_field_pv: "
                    + str(get_mesh_field_pv)
                )
            )
        )
    else:
        get_mesh_field_pv = get_mesh_field_pv
    # cf Methods.Mesh.MeshSolution.plot_mesh
    if isinstance(plot_mesh, ImportError):
        plot_mesh = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_mesh: " + str(plot_mesh)
                )
            )
        )
    else:
        plot_mesh = plot_mesh
    # cf Methods.Mesh.MeshSolution.plot_contour
    if isinstance(plot_contour, ImportError):
        plot_contour = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_contour: " + str(plot_contour)
                )
            )
        )
    else:
        plot_contour = plot_contour
    # cf Methods.Mesh.MeshSolution.plot_deflection
    if isinstance(plot_deflection, ImportError):
        plot_deflection = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_deflection: "
                    + str(plot_deflection)
                )
            )
        )
    else:
        plot_deflection = plot_deflection
    # cf Methods.Mesh.MeshSolution.plot_glyph
    if isinstance(plot_glyph, ImportError):
        plot_glyph = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method plot_glyph: " + str(plot_glyph)
                )
            )
        )
    else:
        plot_glyph = plot_glyph
    # cf Methods.Mesh.MeshSolution.perm_coord
    if isinstance(perm_coord, ImportError):
        perm_coord = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method perm_coord: " + str(perm_coord)
                )
            )
        )
    else:
        perm_coord = perm_coord
    # cf Methods.Mesh.MeshSolution.get_deflection
    if isinstance(get_deflection, ImportError):
        get_deflection = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_deflection: "
                    + str(get_deflection)
                )
            )
        )
    else:
        get_deflection = get_deflection
    # cf Methods.Mesh.MeshSolution.get_glyph
    if isinstance(get_glyph, ImportError):
        get_glyph = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method get_glyph: " + str(get_glyph)
                )
            )
        )
    else:
        get_glyph = get_glyph
    # cf Methods.Mesh.MeshSolution.add_solution
    if isinstance(add_solution, ImportError):
        add_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method add_solution: " + str(add_solution)
                )
            )
        )
    else:
        add_solution = add_solution
    # cf Methods.Mesh.MeshSolution.replace_solution
    if isinstance(replace_solution, ImportError):
        replace_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method replace_solution: "
                    + str(replace_solution)
                )
            )
        )
    else:
        replace_solution = replace_solution
    # cf Methods.Mesh.MeshSolution.pop_solution
    if isinstance(pop_solution, ImportError):
        pop_solution = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method pop_solution: " + str(pop_solution)
                )
            )
        )
    else:
        pop_solution = pop_solution
    # cf Methods.Mesh.MeshSolution.keys
    if isinstance(keys, ImportError):
        keys = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshSolution method keys: " + str(keys))
            )
        )
    else:
        keys = keys
    # cf Methods.Mesh.MeshSolution.items
    if isinstance(items, ImportError):
        items = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshSolution method items: " + str(items))
            )
        )
    else:
        items = items
    # cf Methods.Mesh.MeshSolution.values
    if isinstance(values, ImportError):
        values = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshSolution method values: " + str(values))
            )
        )
    else:
        values = values
    # cf Methods.Mesh.MeshSolution.__getitem__
    if isinstance(__getitem__, ImportError):
        __getitem__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method __getitem__: " + str(__getitem__)
                )
            )
        )
    else:
        __getitem__ = __getitem__
    # cf Methods.Mesh.MeshSolution.__setitem__
    if isinstance(__setitem__, ImportError):
        __setitem__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method __setitem__: " + str(__setitem__)
                )
            )
        )
    else:
        __setitem__ = __setitem__
    # cf Methods.Mesh.MeshSolution.__iter__
    if isinstance(__iter__, ImportError):
        __iter__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshSolution method __iter__: " + str(__iter__))
            )
        )
    else:
        __iter__ = __iter__
    # cf Methods.Mesh.MeshSolution.export_to_mat
    if isinstance(export_to_mat, ImportError):
        export_to_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshSolution method export_to_mat: " + str(export_to_mat)
                )
            )
        )
    else:
        export_to_mat = export_to_mat
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        label="",
        mesh=-1,
        solution_dict=-1,
        group=None,
        dimension=2,
        path=None,
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
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "solution_dict" in list(init_dict.keys()):
                solution_dict = init_dict["solution_dict"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
            if "path" in list(init_dict.keys()):
                path = init_dict["path"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.label = label
        self.mesh = mesh
        self.solution_dict = solution_dict
        self.group = group
        self.dimension = dimension
        self.path = path

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MeshSolution_str = ""
        if self.parent is None:
            MeshSolution_str += "parent = None " + linesep
        else:
            MeshSolution_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        MeshSolution_str += 'label = "' + str(self.label) + '"' + linesep
        if self.mesh is not None:
            tmp = self.mesh.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            MeshSolution_str += "mesh = " + tmp
        else:
            MeshSolution_str += "mesh = None" + linesep + linesep
        if len(self.solution_dict) == 0:
            MeshSolution_str += "solution_dict = dict()" + linesep
        for key, obj in self.solution_dict.items():
            tmp = (
                self.solution_dict[key].__str__().replace(linesep, linesep + "\t")
                + linesep
            )
            MeshSolution_str += "solution_dict[" + key + "] =" + tmp + linesep + linesep
        MeshSolution_str += "group = " + str(self.group) + linesep
        MeshSolution_str += "dimension = " + str(self.dimension) + linesep
        MeshSolution_str += 'path = "' + str(self.path) + '"' + linesep
        return MeshSolution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.label != self.label:
            return False
        if other.mesh != self.mesh:
            return False
        if other.solution_dict != self.solution_dict:
            return False
        if other.group != self.group:
            return False
        if other.dimension != self.dimension:
            return False
        if other.path != self.path:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._label != self._label:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._label) + ", other=" + str(other._label) + ")"
                )
                diff_list.append(name + ".label" + val_str)
            else:
                diff_list.append(name + ".label")
        if (other.mesh is None and self.mesh is not None) or (
            other.mesh is not None and self.mesh is None
        ):
            diff_list.append(name + ".mesh None mismatch")
        elif self.mesh is not None:
            diff_list.extend(
                self.mesh.compare(
                    other.mesh,
                    name=name + ".mesh",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (other.solution_dict is None and self.solution_dict is not None) or (
            other.solution_dict is not None and self.solution_dict is None
        ):
            diff_list.append(name + ".solution_dict None mismatch")
        elif self.solution_dict is None:
            pass
        elif len(other.solution_dict) != len(self.solution_dict):
            diff_list.append("len(" + name + "solution_dict)")
        else:
            for key in self.solution_dict:
                diff_list.extend(
                    self.solution_dict[key].compare(
                        other.solution_dict[key],
                        name=name + ".solution_dict[" + str(key) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if other._group != self._group:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._group) + ", other=" + str(other._group) + ")"
                )
                diff_list.append(name + ".group" + val_str)
            else:
                diff_list.append(name + ".group")
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
        if other._path != self._path:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._path) + ", other=" + str(other._path) + ")"
                )
                diff_list.append(name + ".path" + val_str)
            else:
                diff_list.append(name + ".path")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.label)
        S += getsizeof(self.mesh)
        if self.solution_dict is not None:
            for key, value in self.solution_dict.items():
                S += getsizeof(value) + getsizeof(key)
        if self.group is not None:
            for key, value in self.group.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.dimension)
        S += getsizeof(self.path)
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

        MeshSolution_dict = dict()
        MeshSolution_dict["label"] = self.label
        if self.mesh is None:
            MeshSolution_dict["mesh"] = None
        else:
            MeshSolution_dict["mesh"] = self.mesh.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        if self.solution_dict is None:
            MeshSolution_dict["solution_dict"] = None
        else:
            MeshSolution_dict["solution_dict"] = dict()
            for key, obj in self.solution_dict.items():
                if obj is not None:
                    MeshSolution_dict["solution_dict"][key] = obj.as_dict(
                        type_handle_ndarray=type_handle_ndarray,
                        keep_function=keep_function,
                        **kwargs
                    )
                else:
                    MeshSolution_dict["solution_dict"][key] = None
        MeshSolution_dict["group"] = (
            self.group.copy() if self.group is not None else None
        )
        MeshSolution_dict["dimension"] = self.dimension
        MeshSolution_dict["path"] = self.path
        # The class name is added to the dict for deserialisation purpose
        MeshSolution_dict["__class__"] = "MeshSolution"
        return MeshSolution_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        label_val = self.label
        if self.mesh is None:
            mesh_val = None
        else:
            mesh_val = self.mesh.copy()
        if self.solution_dict is None:
            solution_dict_val = None
        else:
            solution_dict_val = dict()
            for key, obj in self.solution_dict.items():
                solution_dict_val[key] = obj.copy()
        if self.group is None:
            group_val = None
        else:
            group_val = self.group.copy()
        dimension_val = self.dimension
        path_val = self.path
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            label=label_val,
            mesh=mesh_val,
            solution_dict=solution_dict_val,
            group=group_val,
            dimension=dimension_val,
            path=path_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.label = None
        if self.mesh is not None:
            self.mesh._set_None()
        self.solution_dict = None
        self.group = None
        self.dimension = None
        self.path = None

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    label = property(
        fget=_get_label,
        fset=_set_label,
        doc="""(Optional) Descriptive name of the mesh

        :Type: str
        """,
    )

    def _get_mesh(self):
        """getter of mesh"""
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "mesh")
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Mesh = import_class("pyleecan.Classes", "Mesh", "mesh")
            value = Mesh()
        check_var("mesh", value, "Mesh")
        self._mesh = value

        if self._mesh is not None:
            self._mesh.parent = self

    mesh = property(
        fget=_get_mesh,
        fset=_set_mesh,
        doc="""A Mesh object. 

        :Type: Mesh
        """,
    )

    def _get_solution_dict(self):
        """getter of solution_dict"""
        if self._solution_dict is not None:
            for key, obj in self._solution_dict.items():
                if obj is not None:
                    obj.parent = self
        return self._solution_dict

    def _set_solution_dict(self, value):
        """setter of solution_dict"""
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
                        "pyleecan.Classes", obj.get("__class__"), "solution_dict"
                    )
                    value[key] = class_obj(init_dict=obj)
        if type(value) is int and value == -1:
            value = dict()
        check_var("solution_dict", value, "{Solution}")
        self._solution_dict = value

    solution_dict = property(
        fget=_get_solution_dict,
        fset=_set_solution_dict,
        doc="""A dictionary of Solution objects

        :Type: {Solution}
        """,
    )

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("group", value, "dict")
        self._group = value

    group = property(
        fget=_get_group,
        fset=_set_group,
        doc="""Dict sorted by groups name with list of elements indices. 

        :Type: dict
        """,
    )

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

    def _get_path(self):
        """getter of path"""
        return self._path

    def _set_path(self, value):
        """setter of path"""
        check_var("path", value, "str")
        self._path = value

    path = property(
        fget=_get_path,
        fset=_set_path,
        doc="""Path where the MeshSolution is stored as a file

        :Type: str
        """,
    )
