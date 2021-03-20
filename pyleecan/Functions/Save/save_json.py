from datetime import datetime
from json import dump
from logging import getLogger
from os import mkdir
from os.path import basename, isdir, isfile, join

from numpy import int32

from ... import __version__
from ...Classes import get_class_dict
from ...Classes._frozen import FrozenClass
from ...definitions import PACKAGE_NAME


def create_folder(name, logger):
    """
    Create the folder: "YYYY_mm_dd HH_MM_SS name"
    """
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
    path = dt_string + name

    # Check if the directory exists
    while isdir(path):
        now = datetime.now()
        dt_string = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
        path = dt_string + name

    logger.info("Creating folder " + path + " to save the object.")
    mkdir(path)

    return path


def fix_file_name(save_path, obj, is_folder, logger):
    """
    Check save_path and modify or create it if needed, i.e. add or remove file extension
    .json or create new name based on class name.

    Parameters
    ----------
    save_path: str
        File/Folder path
    obj:
        Pyleecan object to save
    is_folder: bool
        object is saved if folder mode
    """
    if not save_path:
        if is_folder:  # Create the folder
            save_path = create_folder(type(obj).__name__, logger)
        else:
            save_path = join(type(obj).__name__ + ".json")
    elif not save_path.endswith(".json") and not is_folder:
        save_path = save_path + ".json"
    elif is_folder:
        if save_path.endswith(".json"):
            save_path = save_path[:-5]
        if not isdir(save_path):
            mkdir(save_path)

    return save_path


def is_json_serializable(obj):
    if isinstance(obj, (bool, float, int, str)):
        return True
    else:
        return False


def has_as_dict(obj):
    """Check if object has 'as_dict' method."""
    return hasattr(obj, "as_dict") and callable(getattr(obj, "as_dict", None))


def build_data(obj, logger):
    """
    Build a json serializable data structure of lists, dicts and pyleecan objects.
    Data that can not be serialized will be set to None. Tuples will also be None.

    Parameters
    ----------
    obj :
        An object to serialize

    Returns
    -------
    data :
        A serializable data structure
    """
    # lists
    if isinstance(obj, list):
        data = []
        for elem in obj:
            data.append(build_data(elem, logger))
        return data
    # dicts
    if isinstance(obj, dict):
        data = {}
        for key in obj:
            data[key] = build_data(obj[key], logger)
        return data
    # pyleecan classes, i.e. instances with as_dict method
    if has_as_dict(obj):
        return build_data(obj.as_dict(), logger)
    if isinstance(obj, int32):  # int
        return int(obj)
    # other allowed types
    if is_json_serializable(obj):
        return obj
    # tuples (excluded)
    if isinstance(obj, tuple):
        pass  # TODO Do we need tuples? If we do, add pyleecan tuple helper class.

    if obj is not None:
        logger.warning(
            f"build_data(): Objects of type {type(obj).__name__} can not be "
            + "serialized for now and will be saved as None."
        )

    return None


def save_split_obj(obj, folder_path, logger):
    """
    Scan the object attribute and save the object in a dedicated file

    Parameters
    ----------

    obj: dict
        object dictionnary to save

    folder_path: str
        directory to save all the files

    logger: logging.Logger
        logger to display information

    Returns
    -------
    name : str
        name of the file containing the object
    """
    if "name" in obj.keys() and obj["name"] != "" and obj["name"] != None:
        name = obj["name"] + ".json"
        if not isfile(join(folder_path, name)):
            with open(join(folder_path, name), "w") as json_file:
                msg = "Saving " + obj["name"] + " in " + join(folder_path, name)
                dump(obj, json_file, sort_keys=True, indent=4, separators=(",", ": "))
        else:
            msg = "Skipping " + obj["name"] + " in " + join(folder_path, name)
    else:
        zeros = "0000"
        num = 1
        prefix = zeros[: -len(str(num))] + str(num)
        name = obj["__class__"] + prefix

        # Define the file name
        while isfile(join(folder_path, name + ".json")):
            num += 1
            prefix = zeros[: -len(str(num))] + str(num)
            name = obj["__class__"] + prefix

        # Save the file
        name += ".json"
        file_path = join(folder_path, name)
        msg = f"Saving unamed object of class {obj['__class__']} in {file_path}"
        with open(file_path, "w") as json_file:
            dump(obj, json_file, sort_keys=True, indent=4, separators=(",", ": "))

    logger.info(msg)

    return name  # Set the name to load the file


def save_separated_obj(classes_tuple, obj_dict, folder_path, logger):
    """
    Save classes_tuple objects contained in obj_dict in separated files and modify
    obj_dict.

    Parameters
    ----------

    classes_tuple: tuple
        tuple containing the classe names to save separately

    obj_dict: dict
        object dictionnary to save

    folder_path: str
        directory to save all the files

    logger: logging.Logger
        logger to display information

    Returns
    -------
    obj_dict : dict
        object dictionnary to save
    """

    for key, val in obj_dict.items():
        if isinstance(val, dict):
            obj_dict[key] = _split_(val, classes_tuple, folder_path, logger)

        elif isinstance(val, list):
            for idx, list_val in enumerate(val):
                # Pyleecan obj and normal dict (to unify code)
                if isinstance(list_val, dict):
                    val[idx] = _split_(list_val, classes_tuple, folder_path, logger)

    return obj_dict


def _split_(val, classes_tuple, folder_path, logger):
    if "__class__" in val.keys() and val["__class__"] in classes_tuple:
        # Call save_separated_obj to save the sub object into files
        save_separated_obj(classes_tuple, val, folder_path, logger)
        # Save this object and get the file name
        obj = save_split_obj(val, folder_path, logger)
    else:
        # Scan the dicts attributes
        obj = save_separated_obj(classes_tuple, val, folder_path, logger)
    return obj


def save_json(
    obj,
    save_path="",
    is_folder=False,
    class_to_split=("Simulation", "Machine", "Material"),
):
    """Save the object to the save_path

    Parameters
    ----------
    obj :
        A pyleecan object
    save_path: str
        path to the folder to save the object
    is_folder: bool
        to split the object in different files
    class_to_split: list
        list of classes (and daughter classes) that should be split
    """
    if isinstance(obj, FrozenClass):  # Pyleecan obj
        # Get the object logger
        logger = obj.get_logger()
    else:
        logger = getLogger("Pyleecan")

    # correct file name if needed
    save_path = fix_file_name(save_path, obj, is_folder, logger)

    # save
    obj = build_data(obj, logger)
    now = datetime.now()
    obj["__save_date__"] = now.strftime("%Y_%m_%d %Hh%Mmin%Ss ")
    obj["__version__"] = PACKAGE_NAME + "_" + __version__
    if is_folder:
        # Add the classes daughters
        class_to_add = []
        class_dict = get_class_dict()

        for class_name in class_to_split:
            class_to_add.extend(class_dict[class_name]["daughters"])

        class_to_split += tuple(class_to_add)

        # Call ref_objects to save the objects separately
        obj = save_separated_obj(class_to_split, obj, save_path, logger)

        i = max(save_path.rfind("/"), save_path.rfind("\\"))
        if i != -1:
            save_path += save_path[i:]
        else:
            save_path += "/" + save_path
        save_path += ".json"

    logger.info("Saving in " + save_path)
    with open(save_path, "w") as json_file:
        dump(obj, json_file, sort_keys=True, indent=4, separators=(",", ": "))

    return obj
