def convert(self):
    """Convert the dict from .mot into a pyleecan machine or vice versa

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    """

    self.selection_machine_rules()

    # conversion rules list
    if self.is_P_to_other == False:  # conversion to Pyleecan
        for rule in self.rules_list:
            try:
                # utilisation polymorphism to choose type rule
                self.machine = rule.convert_to_P(
                    self.other_dict, self.machine, self.other_unit_dict
                )
            except Exception as e:
                self.get_logger().error(
                    "Error while running rule " + rule.get_name() + ":\n" + str(e)
                )
                raise Exception(
                    "Error while running rule " + rule.get_name() + ":\n" + str(e)
                )

    else:  # conversion to other
        for rule in self.rules_list:
            try:
                self.other_dict = rule.convert_to_other(
                    self.other_dict, self.machine, self.other_unit_dict
                )
            except Exception as e:
                self.get_logger().error(
                    "Error while running rule " + rule.get_name() + ":\n" + str(e)
                )
                raise Exception(
                    "Error while running rule " + rule.get_name() + ":\n" + str(e)
                )
