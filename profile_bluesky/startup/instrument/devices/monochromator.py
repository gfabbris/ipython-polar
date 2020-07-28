"""
Monochromator motors
"""

__all__ = [
    'mono',
    ]

from ..session_logs import logger
logger.info(__file__)

from apsutils.devices import KohzuSeqCtl_Monochromator as Kohzu
from ophyd import Component, Device, EpicsMotor

class Monochromator(Kohzu):

    #th = EpicsMotor('4idb:m1', name='mono', labels=('motor',))  # Kohzu Theta # home_slew_rate=0
    #y = EpicsMotor('4idb:m2', name='mon_y', labels=('motor',))  # Kohzu Y2
    #z = EpicsMotor('4idb:m3', name='mon_z', labels=('motor',))  # Kohzu Y2  # Kohzu Z2
    thf = EpicsMotor('4idb:m4', name='mon_thf', labels=('motor',))  # Kohzu Th2f
    chi = EpicsMotor('4idb:m5', name='mon_chi', labels=('motor',))  # Kohzu Chi

mono = Monochromator('4idb:', name='monochromator')

# TODO: Should we add control over other stuff?
