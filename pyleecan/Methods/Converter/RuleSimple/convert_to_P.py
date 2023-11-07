def convert_to_P(self, other_dict, machine):
    # selection correct value
    other_value = self.get_other(other_dict)

    unit = self.set_unit(self.unit_type)

    # possibility to have str in other_value
    if self.scaling_to_P != 1:
        other_value = other_value * self.scaling_to_P / unit

    machine = self.set_P(machine, other_value)

    return machine
