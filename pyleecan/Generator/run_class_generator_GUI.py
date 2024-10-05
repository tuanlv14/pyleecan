import sys
from os.path import dirname, abspath, join

# Add the parent directory to sys.path
current_dir = dirname(abspath(__file__))
parent_dir = dirname(dirname(current_dir))
sys.path.insert(0, parent_dir)

try:
    from pyleecan.GUI.Dialog.DClassGenerator.DClassGenerator import DClassGenerator
except ImportError:
    print("Error: Unable to import pyleecan. Make sure it's installed or the path is correct.")
    sys.exit(1)

from qtpy.QtWidgets import QApplication

# UPDATE paths to preferred applications
# Path to preferred application to edit python files
PATH_EDITOR_PY = "notepad.exe"
# Path to preferred application to edit csv files
PATH_EDITOR_CSV = "notepad.exe"

def run_class_generator(argv):
    app = QApplication(argv)

    # Machine Setup Widget
    class_generator = DClassGenerator(path_editor_py=PATH_EDITOR_PY, path_editor_csv=PATH_EDITOR_CSV)

    class_generator.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(run_class_generator(sys.argv))
