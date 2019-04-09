from cdo import *
import datetime
import os

print('Beginning to convert gfs files from grb2 to nc')

today_date = '20190409'
today_date2 = datetime.date.today().strftime("%Y%m%d")
print(today_date2)

file_hour = ['006', '012', '018', '024', '030', '036', '042', '048', '054', '060', '066', '072', '078', '084', '090', '096', '102',
             '108', '114', '120', '126', '132', '138', '144', '150', '156', '162', '168', '174', '180', '186', '192', '198', '204',
             '210', '216', '222', '228', '234', '240', '252', '264', '276', '288', '300', '312', '324', '336', '348', '360', '372',
             '384']

# converts grb2 to netcdf
for i in range(0, len(file_hour)):
    ifile = '/Users/jasonbiesinger/Documents/GFS_0.25_data/raw/' + str(today_date) + '00_all/gfs.t00z.pgrb2.0p25.f' + str(file_hour[i]) + '.grb2'
    ofile = '/Users/jasonbiesinger/thredds/GFS_0.25_data/raw/gfs.t00z.pgrb2.0p25.f' + str(file_hour[i]) + '.nc'
    cdo = Cdo()
    cdo.copy(input=ifile, output=ofile, options='-f nc')
    print('File timestep ' + str(file_hour[i]) + ' converted')

print('Finished converting files')