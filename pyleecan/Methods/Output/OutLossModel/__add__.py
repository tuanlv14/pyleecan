import numpy as np


def __add__(self, other):
    if other == 0:
        return self
    try:
        other_loss_density = other.loss_density
        other_coeff_dict = other.coeff_dict
        other_group = other.group
    except AttributeError:
        other_loss_density = other["loss_density"]
        other_coeff_dict = other["coeff_dict"]
        other_group = other["group"]

    new_loss_density = self.loss_density + other_loss_density
    new_coeff_dict = self.coeff_dict.copy()
    for key, value in other_coeff_dict.items():
        if key in new_coeff_dict:
            new_coeff_dict[key] += value
        else:
            new_coeff_dict[key] = value
    new_group = self.group + " + " + other_group
    return {
        "loss_density": new_loss_density,
        "coeff_dict": new_coeff_dict,
        "group": new_group,
    }
