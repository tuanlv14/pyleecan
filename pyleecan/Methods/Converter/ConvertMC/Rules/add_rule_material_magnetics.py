from .....Classes.RuleSimple import RuleSimple
from .....Classes.RuleEquation import RuleEquation
from .....Classes.RuleComplex import RuleComplex


def add_rule_material_magnetics(self, path_P, material):
    """Create and adapt all the rules related to machine dimensions (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    try:
        self.other_dict[f"[{material}]"]["MagneturValue"]

        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "MagneturValue"],
                P_obj_path=f"{path_P}.mag.mur_lin",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    except:
        pass

    try:
        self.other_dict[f"[{material}]"]["MagnetBrValue"]
        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "MagnetBrValue"],
                P_obj_path=f"{path_P}.mag.Brm20",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    except:
        pass

    try:
        self.other_dict[f"[{material}]"]["MagnetTempCoefBr"]

        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "MagnetTempCoefBr"],
                P_obj_path=f"{path_P}.mag.alpha_Br",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    except:
        pass

    try:
        self.other_dict[f"[{material}]"]["LaminationThickness"]

        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "LaminationThickness"],
                P_obj_path=f"{path_P}.mag.Wlam",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    except:
        pass

    self.rules_list.append(
        RuleComplex(
            fct_name="curve_B(H)",
            folder="MotorCAD",
            param_dict={"material": material, "path_P": path_P},
        )
    )
