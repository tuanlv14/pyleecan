# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/MeshVTK.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/MeshVTK
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
from .Mesh import Mesh

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Mesh.MeshVTK.get_mesh_pv import get_mesh_pv
except ImportError as error:
    get_mesh_pv = error

try:
    from ..Methods.Mesh.MeshVTK.get_node_coordinate import get_node_coordinate
except ImportError as error:
    get_node_coordinate = error

try:
    from ..Methods.Mesh.MeshVTK.get_element import get_element
except ImportError as error:
    get_element = error

try:
    from ..Methods.Mesh.MeshVTK.get_normals import get_normals
except ImportError as error:
    get_normals = error

try:
    from ..Methods.Mesh.MeshVTK.get_surf import get_surf
except ImportError as error:
    get_surf = error

try:
    from ..Methods.Mesh.MeshVTK.get_element_area import get_element_area
except ImportError as error:
    get_element_area = error

try:
    from ..Methods.Mesh.MeshVTK.convert import convert
except ImportError as error:
    convert = error

try:
    from ..Methods.Mesh.MeshVTK.perm_coord import perm_coord
except ImportError as error:
    perm_coord = error

try:
    from ..Methods.Mesh.MeshVTK.get_path import get_path
except ImportError as error:
    get_path = error

try:
    from ..Methods.Mesh.MeshVTK.save_vtk import save_vtk
except ImportError as error:
    save_vtk = error


from numpy import array, array_equal
from numpy import isnan
from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from vtk import vtkPointSet
except ImportError:
    vtkPointSet = ImportError
from cloudpickle import dumps, loads
from ._check import CheckTypeError

try:
    from pyvista.core.pointset import PolyData
except ImportError:
    PolyData = ImportError
from ._check import InitUnKnowClassError


class MeshVTK(Mesh):
    """Gather the mesh storage format"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.MeshVTK.get_mesh_pv
    if isinstance(get_mesh_pv, ImportError):
        get_mesh_pv = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_mesh_pv: " + str(get_mesh_pv))
            )
        )
    else:
        get_mesh_pv = get_mesh_pv
    # cf Methods.Mesh.MeshVTK.get_node_coordinate
    if isinstance(get_node_coordinate, ImportError):
        get_node_coordinate = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshVTK method get_node_coordinate: "
                    + str(get_node_coordinate)
                )
            )
        )
    else:
        get_node_coordinate = get_node_coordinate
    # cf Methods.Mesh.MeshVTK.get_element
    if isinstance(get_element, ImportError):
        get_element = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_element: " + str(get_element))
            )
        )
    else:
        get_element = get_element
    # cf Methods.Mesh.MeshVTK.get_normals
    if isinstance(get_normals, ImportError):
        get_normals = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_normals: " + str(get_normals))
            )
        )
    else:
        get_normals = get_normals
    # cf Methods.Mesh.MeshVTK.get_surf
    if isinstance(get_surf, ImportError):
        get_surf = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_surf: " + str(get_surf))
            )
        )
    else:
        get_surf = get_surf
    # cf Methods.Mesh.MeshVTK.get_element_area
    if isinstance(get_element_area, ImportError):
        get_element_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MeshVTK method get_element_area: "
                    + str(get_element_area)
                )
            )
        )
    else:
        get_element_area = get_element_area
    # cf Methods.Mesh.MeshVTK.convert
    if isinstance(convert, ImportError):
        convert = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method convert: " + str(convert))
            )
        )
    else:
        convert = convert
    # cf Methods.Mesh.MeshVTK.perm_coord
    if isinstance(perm_coord, ImportError):
        perm_coord = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method perm_coord: " + str(perm_coord))
            )
        )
    else:
        perm_coord = perm_coord
    # cf Methods.Mesh.MeshVTK.get_path
    if isinstance(get_path, ImportError):
        get_path = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method get_path: " + str(get_path))
            )
        )
    else:
        get_path = get_path
    # cf Methods.Mesh.MeshVTK.save_vtk
    if isinstance(save_vtk, ImportError):
        save_vtk = property(
            fget=lambda x: raise_(
                ImportError("Can't use MeshVTK method save_vtk: " + str(save_vtk))
            )
        )
    else:
        save_vtk = save_vtk
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        mesh=None,
        is_pyvista_mesh=False,
        format="vtk",
        path=None,
        name="mesh",
        surf=None,
        is_vtk_surf=False,
        surf_path="",
        surf_name="",
        node_normals=None,
        dimension=2,
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
            if "mesh" in list(init_dict.keys()):
                mesh = init_dict["mesh"]
            if "is_pyvista_mesh" in list(init_dict.keys()):
                is_pyvista_mesh = init_dict["is_pyvista_mesh"]
            if "format" in list(init_dict.keys()):
                format = init_dict["format"]
            if "path" in list(init_dict.keys()):
                path = init_dict["path"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "surf" in list(init_dict.keys()):
                surf = init_dict["surf"]
            if "is_vtk_surf" in list(init_dict.keys()):
                is_vtk_surf = init_dict["is_vtk_surf"]
            if "surf_path" in list(init_dict.keys()):
                surf_path = init_dict["surf_path"]
            if "surf_name" in list(init_dict.keys()):
                surf_name = init_dict["surf_name"]
            if "node_normals" in list(init_dict.keys()):
                node_normals = init_dict["node_normals"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Set the properties (value check and convertion are done in setter)
        self.mesh = mesh
        self.is_pyvista_mesh = is_pyvista_mesh
        self.format = format
        self.path = path
        self.name = name
        self.surf = surf
        self.is_vtk_surf = is_vtk_surf
        self.surf_path = surf_path
        self.surf_name = surf_name
        self.node_normals = node_normals
        # Call Mesh init
        super(MeshVTK, self).__init__(dimension=dimension)
        # The class is frozen (in Mesh init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MeshVTK_str = ""
        # Get the properties inherited from Mesh
        MeshVTK_str += super(MeshVTK, self).__str__()
        MeshVTK_str += "mesh = " + str(self.mesh) + linesep + linesep
        MeshVTK_str += "is_pyvista_mesh = " + str(self.is_pyvista_mesh) + linesep
        MeshVTK_str += 'format = "' + str(self.format) + '"' + linesep
        MeshVTK_str += 'path = "' + str(self.path) + '"' + linesep
        MeshVTK_str += 'name = "' + str(self.name) + '"' + linesep
        MeshVTK_str += "surf = " + str(self.surf) + linesep + linesep
        MeshVTK_str += "is_vtk_surf = " + str(self.is_vtk_surf) + linesep
        MeshVTK_str += 'surf_path = "' + str(self.surf_path) + '"' + linesep
        MeshVTK_str += 'surf_name = "' + str(self.surf_name) + '"' + linesep
        MeshVTK_str += (
            "node_normals = "
            + linesep
            + str(self.node_normals).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return MeshVTK_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Mesh
        if not super(MeshVTK, self).__eq__(other):
            return False
        if other.mesh != self.mesh:
            return False
        if other.is_pyvista_mesh != self.is_pyvista_mesh:
            return False
        if other.format != self.format:
            return False
        if other.path != self.path:
            return False
        if other.name != self.name:
            return False
        if other.surf != self.surf:
            return False
        if other.is_vtk_surf != self.is_vtk_surf:
            return False
        if other.surf_path != self.surf_path:
            return False
        if other.surf_name != self.surf_name:
            return False
        if not array_equal(other.node_normals, self.node_normals):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Mesh
        diff_list.extend(
            super(MeshVTK, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.mesh is None and self.mesh is not None) or (
            other.mesh is not None and self.mesh is None
        ):
            diff_list.append(name + ".mesh None mismatch")
        elif self.mesh is not None and self.mesh != other.mesh:
            diff_list.append(name + ".mesh")
        if other._is_pyvista_mesh != self._is_pyvista_mesh:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_pyvista_mesh)
                    + ", other="
                    + str(other._is_pyvista_mesh)
                    + ")"
                )
                diff_list.append(name + ".is_pyvista_mesh" + val_str)
            else:
                diff_list.append(name + ".is_pyvista_mesh")
        if other._format != self._format:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._format)
                    + ", other="
                    + str(other._format)
                    + ")"
                )
                diff_list.append(name + ".format" + val_str)
            else:
                diff_list.append(name + ".format")
        if other._path != self._path:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._path) + ", other=" + str(other._path) + ")"
                )
                diff_list.append(name + ".path" + val_str)
            else:
                diff_list.append(name + ".path")
        if other._name != self._name:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._name) + ", other=" + str(other._name) + ")"
                )
                diff_list.append(name + ".name" + val_str)
            else:
                diff_list.append(name + ".name")
        if (other.surf is None and self.surf is not None) or (
            other.surf is not None and self.surf is None
        ):
            diff_list.append(name + ".surf None mismatch")
        elif self.surf is not None and self.surf != other.surf:
            diff_list.append(name + ".surf")
        if other._is_vtk_surf != self._is_vtk_surf:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._is_vtk_surf)
                    + ", other="
                    + str(other._is_vtk_surf)
                    + ")"
                )
                diff_list.append(name + ".is_vtk_surf" + val_str)
            else:
                diff_list.append(name + ".is_vtk_surf")
        if other._surf_path != self._surf_path:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._surf_path)
                    + ", other="
                    + str(other._surf_path)
                    + ")"
                )
                diff_list.append(name + ".surf_path" + val_str)
            else:
                diff_list.append(name + ".surf_path")
        if other._surf_name != self._surf_name:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._surf_name)
                    + ", other="
                    + str(other._surf_name)
                    + ")"
                )
                diff_list.append(name + ".surf_name" + val_str)
            else:
                diff_list.append(name + ".surf_name")
        if not array_equal(other.node_normals, self.node_normals):
            diff_list.append(name + ".node_normals")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Mesh
        S += super(MeshVTK, self).__sizeof__()
        S += getsizeof(self.mesh)
        S += getsizeof(self.is_pyvista_mesh)
        S += getsizeof(self.format)
        S += getsizeof(self.path)
        S += getsizeof(self.name)
        S += getsizeof(self.surf)
        S += getsizeof(self.is_vtk_surf)
        S += getsizeof(self.surf_path)
        S += getsizeof(self.surf_name)
        S += getsizeof(self.node_normals)
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

        # Get the properties inherited from Mesh
        MeshVTK_dict = super(MeshVTK, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        MeshVTK_dict["mesh"] = None
        MeshVTK_dict["is_pyvista_mesh"] = self.is_pyvista_mesh
        MeshVTK_dict["format"] = self.format
        MeshVTK_dict["path"] = self.path
        MeshVTK_dict["name"] = self.name
        MeshVTK_dict["surf"] = None
        MeshVTK_dict["is_vtk_surf"] = self.is_vtk_surf
        MeshVTK_dict["surf_path"] = self.surf_path
        MeshVTK_dict["surf_name"] = self.surf_name
        if self.node_normals is None:
            MeshVTK_dict["node_normals"] = None
        else:
            if type_handle_ndarray == 0:
                MeshVTK_dict["node_normals"] = self.node_normals.tolist()
            elif type_handle_ndarray == 1:
                MeshVTK_dict["node_normals"] = self.node_normals.copy()
            elif type_handle_ndarray == 2:
                MeshVTK_dict["node_normals"] = self.node_normals
            else:
                raise Exception(
                    "Unknown type_handle_ndarray: " + str(type_handle_ndarray)
                )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MeshVTK_dict["__class__"] = "MeshVTK"
        return MeshVTK_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        mesh_val = None
        is_pyvista_mesh_val = self.is_pyvista_mesh
        format_val = self.format
        path_val = self.path
        name_val = self.name
        surf_val = None
        is_vtk_surf_val = self.is_vtk_surf
        surf_path_val = self.surf_path
        surf_name_val = self.surf_name
        if self.node_normals is None:
            node_normals_val = None
        else:
            node_normals_val = self.node_normals.copy()
        dimension_val = self.dimension
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            mesh=mesh_val,
            is_pyvista_mesh=is_pyvista_mesh_val,
            format=format_val,
            path=path_val,
            name=name_val,
            surf=surf_val,
            is_vtk_surf=is_vtk_surf_val,
            surf_path=surf_path_val,
            surf_name=surf_name_val,
            node_normals=node_normals_val,
            dimension=dimension_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.mesh = None
        self.is_pyvista_mesh = None
        self.format = None
        self.path = None
        self.name = None
        self.surf = None
        self.is_vtk_surf = None
        self.surf_path = None
        self.surf_name = None
        self.node_normals = None
        # Set to None the properties inherited from Mesh
        super(MeshVTK, self)._set_None()

    def _get_mesh(self):
        """getter of mesh"""
        return self._mesh

    def _set_mesh(self, value):
        """setter of mesh"""
        if value == -1:
            value = vtkPointSet()
        check_var("mesh", value, "vtkPointSet")
        self._mesh = value

    mesh = property(
        fget=_get_mesh,
        fset=_set_mesh,
        doc="""Pyvista object of the mesh (optional)

        :Type: vtk.vtkPointSet
        """,
    )

    def _get_is_pyvista_mesh(self):
        """getter of is_pyvista_mesh"""
        return self._is_pyvista_mesh

    def _set_is_pyvista_mesh(self, value):
        """setter of is_pyvista_mesh"""
        check_var("is_pyvista_mesh", value, "bool")
        self._is_pyvista_mesh = value

    is_pyvista_mesh = property(
        fget=_get_is_pyvista_mesh,
        fset=_set_is_pyvista_mesh,
        doc="""Store the pyvista object

        :Type: bool
        """,
    )

    def _get_format(self):
        """getter of format"""
        return self._format

    def _set_format(self, value):
        """setter of format"""
        check_var("format", value, "str")
        self._format = value

    format = property(
        fget=_get_format,
        fset=_set_format,
        doc="""Format in which the mesh is stored

        :Type: str
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
        doc="""Path where the mesh is stored

        :Type: str
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc="""Name of the mesh file

        :Type: str
        """,
    )

    def _get_surf(self):
        """getter of surf"""
        return self._surf

    def _set_surf(self, value):
        """setter of surf"""
        if value == -1:
            value = PolyData()
        check_var("surf", value, "PolyData")
        self._surf = value

    surf = property(
        fget=_get_surf,
        fset=_set_surf,
        doc="""Pyvista object of the outer surface

        :Type: pyvista.core.pointset.PolyData
        """,
    )

    def _get_is_vtk_surf(self):
        """getter of is_vtk_surf"""
        return self._is_vtk_surf

    def _set_is_vtk_surf(self, value):
        """setter of is_vtk_surf"""
        check_var("is_vtk_surf", value, "bool")
        self._is_vtk_surf = value

    is_vtk_surf = property(
        fget=_get_is_vtk_surf,
        fset=_set_is_vtk_surf,
        doc="""Save the surface mesh in a vtk file

        :Type: bool
        """,
    )

    def _get_surf_path(self):
        """getter of surf_path"""
        return self._surf_path

    def _set_surf_path(self, value):
        """setter of surf_path"""
        check_var("surf_path", value, "str")
        self._surf_path = value

    surf_path = property(
        fget=_get_surf_path,
        fset=_set_surf_path,
        doc="""Path where the outer surface is stored

        :Type: str
        """,
    )

    def _get_surf_name(self):
        """getter of surf_name"""
        return self._surf_name

    def _set_surf_name(self, value):
        """setter of surf_name"""
        check_var("surf_name", value, "str")
        self._surf_name = value

    surf_name = property(
        fget=_get_surf_name,
        fset=_set_surf_name,
        doc="""Name of the outer surface file

        :Type: str
        """,
    )

    def _get_node_normals(self):
        """getter of node_normals"""
        return self._node_normals

    def _set_node_normals(self, value):
        """setter of node_normals"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("node_normals", value, "ndarray")
        self._node_normals = value

    node_normals = property(
        fget=_get_node_normals,
        fset=_set_node_normals,
        doc="""Array of normals to nodes (element vertices)

        :Type: ndarray
        """,
    )
