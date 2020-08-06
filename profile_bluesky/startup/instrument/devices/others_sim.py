'''
Other motor/counters
'''

__all__ = [
    'uptab','kbic','xbpm'
    ]

from ..session_logs import logger
logger.info(__file__)

from ophyd import Component, Device, EpicsMotor

class UpTable(Device):
    y = Component(EpicsMotor, 'm1', labels=('motor','uptable'))  # Uptable Y
    x = Component(EpicsMotor, 'm6', labels=('motor','uptable'))  # Uptable Y

uptab = UpTable('xxx:',name='uptable')

class KBIC(Device):
    y = Component(EpicsMotor, 'm2', labels=('motor','kbic'))  # KB IC Y
    x = Component(EpicsMotor, 'm3', labels=('motor','kbic'))  # KB IC X

kbic = KBIC('xxx:',name='KBIC')


class XBPM(Device):
    y = Component(EpicsMotor, 'm4', labels=('motor','XBPM'))  # XBPM ver
    x = Component(EpicsMotor, 'm5', labels=('motor','XBPM'))  # XBPM hor

xbpm = XBPM('xxx:',name='XBPM')

# TODO: Maybe other things that can be here? Like the motors for flags?
