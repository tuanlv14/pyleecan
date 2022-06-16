from ....Functions.labels import HOLEV_LAB, VENT_LAB


def get_R_id(self):
    """Return the "Radial" index for label (index in lam.hole or lam.axial_vent)

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    R_id : int
        "Radial" index of the hole in the lamination
    surf_type : str
        Label to use for the surface type (HoleV or Vent)
    """

    if self.parent is None:  # Compatibility For plotting
        return (0, HOLEV_LAB)
    elif (
        hasattr(self.parent, "hole")
        and self.parent.hole is not None
        and self in self.parent.hole
    ):
        return (self.parent.hole.index(self), HOLEV_LAB)
    elif (
        hasattr(self.parent, "hole_north")
        and self.parent.hole_north is not None
        and self in self.parent.hole_north
    ):
        return (self.parent.hole_north.index(self), HOLEV_LAB)
    elif (
        hasattr(self.parent, "hole_south")
        and self.parent.hole_south is not None
        and self in self.parent.hole_south
    ):
        return (self.parent.hole_south.index(self), HOLEV_LAB)
    elif self.parent.axial_vent is not None and self in self.parent.axial_vent:
        return (self.parent.axial_vent.index(self), VENT_LAB)
    else:
        raise Exception("Error, impossible to get Hole R-id")
