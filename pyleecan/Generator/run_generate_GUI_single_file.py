# -*- coding: utf-8 -*-
import sys
from os.path import dirname, abspath, normpath, join, realpath, isdir
from os import listdir, remove, mkdir, system

# Add the parent directory of 'pyleecan' to the Python path
MAIN_DIR = dirname(dirname(dirname(realpath(__file__))))
sys.path.append(MAIN_DIR)

# Now use absolute imports
from pyleecan.Generator.gui_generator import generate_gui_single_file, generate_gui
from pyleecan.Generator.read_fct import read_all
from pyleecan.definitions import MAIN_DIR

package_name = "pyleecan"
soft_name = package_name
DOC_DIR = join(MAIN_DIR, "Generator", "ClassesRef")

# Edit this value to select the Ui file to generate
file_name = "DClassGenerator.ui"

if __name__ == "__main__":
    ui_folder_path = join(MAIN_DIR, "GUI")
    gen_dict = read_all(DOC_DIR, soft_name=soft_name)
    print("#############################\nGenerating gui....")
    generate_gui_single_file(
        file_name,
        ui_folder_path,
        gen_dict=gen_dict,
    )

    # Run black
    try:
        import black

        system('"{}" -m black {}'.format(sys.executable, ui_folder_path))
        if black.__version__.split(".")[0] != "20":
            print("\n############################################")
            print(
                "WARNING: The official version of black for pyleecan is 20, please update your black version"
            )
            print("############################################\n")
    except ImportError:
        print("/!\\ Please install and run black (version 20) /!\\")
