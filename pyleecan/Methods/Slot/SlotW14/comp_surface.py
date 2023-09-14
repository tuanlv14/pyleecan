from numpy import sin
from ....Methods.Slot.Slot.comp_surface_wedges import comp_surface_wedges


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    if hasattr(self, "wedge_type"):
        wedge_type = self.wedge_type

    if wedge_type == 1:
        return (
            self.comp_surface_active()
            + self.comp_surface_opening()
            + self.comp_surface_wedge()
        )

    return self.comp_surface_active() + self.comp_surface_opening()
