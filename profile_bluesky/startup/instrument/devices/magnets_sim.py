"""
Magnet motors
"""

__all__ = [
    'mag6t',
    ]

from ..session_logs import logger
logger.info(__file__)

from ophyd import Component, Device, EpicsMotor

## Magnet and sample motors ##
class Magnet6T(Device):
    tabth = Component(EpicsMotor,'m1', labels=('motor','6T magnet'))  # 4T Mag Th
    tabx = Component(EpicsMotor,'m2', labels=('motor','6T magnet'))  # 4T MagTab X
    taby = Component(EpicsMotor,'m3', labels=('motor','6T magnet'))  # 4T MagTab Y

    tabth2 = Component(EpicsMotor,'m4', labels=('motor','6T magnet'))  # AMIMagnetPhi
    tabz2 = Component(EpicsMotor,'m5', labels=('motor','6T magnet'))  # AMIMagnetZ
    tabx2 = Component(EpicsMotor,'m6', labels=('motor','6T magnet'))  # AMIMagenetX

    sampy = Component(EpicsMotor,'m7', labels=('motor','6T magnet'))  # CIATRA
    sampth = Component(EpicsMotor,'m8', labels=('motor','6T magnet'))  # CIA ROT

mag6t = Magnet6T('xxx:',name='6T magnet')

# TODO: should we add the magnet field controls here?
