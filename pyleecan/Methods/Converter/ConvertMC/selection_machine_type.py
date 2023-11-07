from pyleecan.Methods.Converter.ConvertMC.Rules.add_rule_machine_type import (
    add_rule_machine_type,
)
from pyleecan.Methods.Converter.ConvertMC.Rules.add_rule_machine_dimension import (
    add_rule_machine_dimension,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_BPM_rules import (
    selection_BPM_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_IM_rules import (
    selection_IM_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_SRM_rules import (
    selection_SRM_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_BPMO_rules import (
    selection_BPMO_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_PMDC_rules import (
    selection_PMDC_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_BPMO_rules import (
    selection_BPMO_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_SYNC_rules import (
    selection_SYNC_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_CLAW_rules import (
    selection_CLAW_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_IM1PH_rules import (
    selection_IM1PH_rules,
)
from pyleecan.Methods.Converter.ConvertMC.machine_type.selection_WFC_rules import (
    selection_WFC_rules,
)

from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM


def selection_machine_type(self):
    # check the direction of conversion
    if self.is_P_to_other == False:
        motor_type = self.other_dict["[Calc_Options]"]["Motor_Type"]

    else:
        motor_type = type(self.machine).__name__

    # add rule present in all machine
    add_rule_machine_type(self)
    add_rule_machine_dimension(self)
    # selecion motor_type
    if motor_type in ["BPM", "MachineSIPMSM"]:
        # particularity for BPM with airgap, changemen rule machine dimension
        selection_BPM_rules(self)

    elif motor_type in ["IM", "MachineIPmSM"]:
        selection_IM_rules(self)

    elif motor_type == "SRM":
        selection_SRM_rules(self)

    elif motor_type == "BPMO":
        selection_BPMO_rules(self)

    elif motor_type == "PMDC":
        selection_PMDC_rules(self)

    elif motor_type == "SYNC":
        selection_SYNC_rules(self)

    elif motor_type == "CLAW":
        selection_CLAW_rules(self)

    elif motor_type == "IM1PH":
        selection_IM1PH_rules(self)

    elif motor_type == "WFC":
        selection_WFC_rules(self)
