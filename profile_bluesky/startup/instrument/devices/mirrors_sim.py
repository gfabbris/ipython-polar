
"""
Magnet motor
"""

__all__ = [
    'toroidal_mirror','flat_mirror'
    ]

from ..session_logs import logger
logger.info(__file__)

from ophyd import Component, Device, EpicsMotor, EpicsSignal

## Toroidal Mirror ##
class ToroidalMirror(Device):

    y_upstream   = Component(EpicsMotor,'m1',labels=('motor','mirrors'))
    y_downstream = Component(EpicsMotor,'m2',labels=('motor','mirrors'))
    y = Component(EpicsSignal,'m10t2.D',write_pv=':m10avg',
                          labels=('motor','mirrors'))
    angle = Component(EpicsSignal,'m10t2.C',write_pv=':m10angl',
                        labels=('motor','mirrors'))


    x_upstream   = Component(EpicsMotor,'m3',labels=('motor','mirrors'))
    x_downstream = Component(EpicsMotor,'m4',labels=('motor','mirrors'))
    x = Component(EpicsSignal,'m10xt2.D',write_pv=':m10xavg',
                          labels=('mirrors'))
    x_angle = Component(EpicsSignal,'m10xt2.C',write_pv=':m10xangl',
                        labels=('mirrors'))

    bender = Component(EpicsMotor,'m5',labels=('motor','mirrors'))

toroidal_mirror = ToroidalMirror('xxx:',name='toroidal mirror')

class FlatMirror(Device):

    y_upstream   = Component(EpicsMotor,'m6',labels=('motor','mirrors'))
    y_downstream = Component(EpicsMotor,'m7',labels=('motor','mirrors'))
    y = Component(EpicsSignal,'m18t2.D',write_pv=':m18avg',
                          labels=('mirrors'))
    angle = Component(EpicsSignal,'m18t2.C',write_pv=':m18angl',
                        labels=('mirrors'))

    x_upstream   = Component(EpicsMotor,'m8',labels=('motor','mirrors'))
    x_downstream = Component(EpicsMotor,'m9',labels=('motor','mirrors'))
    x = Component(EpicsSignal,'m18xt2.D',write_pv=':m10xavg',
                          labels=('mirrors'))
    x_angle = Component(EpicsSignal,'m10xt2.C',write_pv=':m10xangl',
                        labels=('mirrors'))

flat_mirror = FlatMirror('xxx:',name='flat mirror')

# TODO: How to add the different default positions in the mirrors?
# TODO: Check that the limits option of EpicsSignal will work!
# TODO: KB mirrors.
