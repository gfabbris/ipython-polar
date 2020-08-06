"""
Phase retarders
"""

__all__ = [
    'pr1','pr2','pr3'
    ]

from ..session_logs import logger
logger.info(__file__)

from ophyd import Device, EpicsMotor, FormattedComponent

class PRDevice(Device):

    x = FormattedComponent(EpicsMotor,'{self.prefix}:{_motorsDict[x]}',
                           labels=('motor','phase retarders'))

    y = FormattedComponent(EpicsMotor,'{self.prefix}:{_motorsDict[y]}',
                           labels=('motor','phase retarders'))

    th = FormattedComponent(EpicsMotor,'{self.prefix}:{_motorsDict[th]}',
                            labels=('motor','phase retarders'))

    def __init__(self,prefix,name,motorsDict,**kwargs):
        self._motorsDict = motorsDict
        super().__init__(prefix=prefix, name=name, **kwargs)

pr1 = PRDevice('xxx','pr1',{'x':'m1','y':'m2','th':'m3'})
pr2 = PRDevice('xxx','pr2',{'x':'m4','y':'m5','th':'m6'})
pr3 = PRDevice('xxx','pr3',{'x':'m7','y':'m8','th':'m9'})

# TODO: add other stuff to pr's, like lock-in PVS, and screen position.
