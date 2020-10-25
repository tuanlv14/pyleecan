# -*- coding: utf-8 -*-
from ....Functions.Simulation.create_from_axis import create_from_axis


def comp_time_angle(self, output):
    """Compute the time and space discretization of the Magnetics module

    Parameters
    ----------
    self : Magnetic
        a Magnetic object
    output : Output
        an Output object (to update)

    """

    # Get time and space (anti-)periodicities of the machine
    (
        per_a,
        is_antiper_a,
        per_t,
        is_antiper_t,
    ) = output.get_machine_periodicity()

    # Compute Time axis based on the one stored in OutElec
    Time, is_periodicity_t = create_from_axis(
        axis_in=output.elec.Time,
        per=per_t,
        is_aper=is_antiper_t,
        is_include_per=self.is_periodicity_t,
        is_remove_aper=False,
    )

    if is_periodicity_t != self.is_periodicity_t:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_t = False
        Nt_tot = Time.get_length(is_oneperiod=False)        
        self.get_logger().warning(
            "WARNING: In Magnetic model, Nt_tot="
            + str(Nt_tot)
            + " is not divisible by the machine time periodicity ("
            + str(per_t)
            + "). Time periodicity removed"
        )

    # Store Time axis in OutMag
    output.mag.Time = Time

    # Compute Angle axis based on the one stored in OutElec
    Angle, is_periodicity_a = create_from_axis(
        axis_in=output.elec.Angle,
        per=per_a,
        is_aper=is_antiper_a,
        is_include_per=self.is_periodicity_a,
        is_remove_aper=False,
    )

    if is_periodicity_a != self.is_periodicity_a:
        # Remove time periodicity in Magnetic model
        self.is_periodicity_a = False
        Na_tot = Angle.get_length(is_oneperiod=False)
        self.get_logger().warning(
            "WARNING: In Magnetic model, Na_tot="
            + str(Na_tot)
            + " is not divisible by the machine angular periodicity ("
            + str(per_a)
            + "). Angular periodicity removed"
        )

    # Store Angle axis in OutMag
    output.mag.Angle = Angle
