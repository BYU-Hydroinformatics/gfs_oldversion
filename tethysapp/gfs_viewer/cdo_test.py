from cdo import *

i = 0
while (i < 5):
    ifile = '/Users/jasonbiesinger/thredds/gfs.t00z.pgrb2.0p25.f006.grb2'
    ofile = '/Users/jasonbiesinger/thredds/gfs.t00z.pgrb2.0p25.f006.nc'
    cdo = Cdo()
    cdo.copy(input=ifile, output=ofile, options='-f nc copy')
    i = i + 1