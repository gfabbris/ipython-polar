
"""
Diffractometer motors
"""

__all__ = [
    'cryo',
    'huber'
    ]

from ..session_logs import logger
logger.info(__file__)

from ophyd import Component, Device, EpicsMotor

## Cryo carrier ##
class CryoStage(Device):
    x = Component(EpicsMotor, 'm1', labels=('motor', 'cryo'))  # Cryo X
    y = Component(EpicsMotor, 'm2', labels=('motor', 'cryo'))  # Cryo Y
    z = Component(EpicsMotor, 'm3', labels=('motor', 'cryo'))  # Cryo Z

cryo = CryoStage(prefix='xxx:',name='cryo')

## 8c rotations ##
class Diffractometer(Device):
    th = Component(EpicsMotor,'m4', labels=('motor','diffractometer'))  # Theta # slop=2
    tth = Component(EpicsMotor,'m5', labels=('motor','diffractometer'))  # Two Theta
    phi = Component(EpicsMotor,'m6', labels=('motor','diffractometer'))  # Phi
    chi = Component(EpicsMotor,'m7', labels=('motor','diffractometer'))  # Chi
    bth = Component(EpicsMotor,'m8', labels=('motor','diffractometer'))  # Base Th
    btth = Component(EpicsMotor,'m9', labels=('motor','diffractometer'))  # Base tth
    ath = Component(EpicsMotor,'m10', labels=('motor','diffractometer'))  # Ana Theta
    achi = Component(EpicsMotor,'m11', labels=('motor','diffractometer'))  # Ana Chi
    atth = Component(EpicsMotor,'m12', labels=('motor','diffractometer'))  # Ana 2Theta
    x = Component(EpicsMotor,'m13', labels=('motor','diffractometer'))  # 8C horiz
    y = Component(EpicsMotor,'m14', labels=('motor','diffractometer'))  # 8C verical

huber = Diffractometer(prefix='xxx:',name='huber')

# TODO: look at todo folder. Use hklpy when setting these up, so that we
#       can create fourc and sixc

# TODO: discuss the extend of which we want to add classes like the one below
#class Diffractometer(Device):
#   cryo = Component(CryoStage)
#   scaler = ScalerCH( ... )
#   filters =
#   magnets =
#diffractometer = Diffractometer(name="diffractometer")
