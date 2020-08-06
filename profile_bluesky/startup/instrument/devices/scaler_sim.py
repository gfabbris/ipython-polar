
"""
our diffractometer
"""

__all__ = [
    'scalerd',
    #'scalerb',
    ]

from ..session_logs import logger
logger.info(__file__)

from ophyd.scaler import ScalerCH

scalerd = ScalerCH('xxx:scaler1', name='scalerd', labels=('detectors','counters'))

dets_names = ['Time','ic1','ic2','ic3','ic4','ic5','APD']
for i,name in enumerate(dets_names):
    chan = getattr(scalerd.channels,'chan{:02d}'.format(i+1))
    chan.chname.put(name)

scalerd.select_channels(None)

#scalerb = ScalerCH('4idb:scaler1', name='scalerb', labels=('detectors','counters'))
#scalerb.select_channels(None)

# TODO: name the other channels, watch out for python keywords such as del!
# TODO: How should we handle the scalers? What is scaler3?
