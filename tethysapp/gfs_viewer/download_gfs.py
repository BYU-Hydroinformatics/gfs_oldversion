import requests
import datetime

print('Beginning file download with requests')

today_date = '20190409'
today_date2 = datetime.date.today().strftime("%Y%m%d")
print(today_date2)

file_hour = ['006', '012', '018', '024', '030', '036', '042', '048', '054', '060', '066', '072', '078', '084', '090', '096', '102',
             '108', '114', '120', '126', '132', '138', '144', '150', '156', '162', '168', '174', '180', '186', '192', '198', '204',
             '210', '216', '222', '228', '234', '240', '252', '264', '276', '288', '300', '312', '324', '336', '348', '360', '372',
             '384']

# download gfs files by timestep using nomads.ncep.noaa.gov website
for i in range(0, len(file_hour)):
    url = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t00z.pgrb2.0p25.f' + str(file_hour[i]) + '&lev_surface=on&all_var=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.' + str(today_date) + '00'
    r = requests.get(url)

    with open('/Users/jasonbiesinger/Documents/GFS_0.25_data/raw/' + str(today_date) + '00_all/gfs.t00z.pgrb2.0p25.f' + str(file_hour[i]) + '.grb2', 'wb') as f:
        f.write(r.content)
    print('File timestep ' + str(file_hour[i]) + ' downloaded')

print('Finished downloading files')