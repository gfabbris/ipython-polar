from glob import glob
import re

files = glob('*.py')
files.remove('__init__.py')
files.remove('spec_config.py')
files.remove('convert_devices.py')

for fname in files:
    if '_sim' not in fname:
        file = open(fname,'r').read()

        match = re.findall(r'(m[1-9][0-9])', file, re.I)
        pos = [file.find(mt) for mt in match]

        match_1 = re.findall(r'(m[1-9])', file, re.I)
        pos_1 = [file.find(mt) for mt in match_1]

        for i,p in enumerate(pos_1):
            if p not in pos:
                match += [match_1[i]]

        for i,mt in enumerate(match):
            file = file.replace(mt,'m{}'.format(i+1))

        for iocs in ['4iddx','4idb','4idd','4id']:
            file = file.replace(iocs,'xxx')

        out = open(fname.split('.')[0]+'_sim.py','w')
        out.write(file)
        out.close()
