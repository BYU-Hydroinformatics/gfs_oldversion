from .resources import app_configuration
import netCDF4, numpy, datetime, os, calendar

# generates the plotable points based on the user inputs
def ts_plot(data):
    """
    Description: generates a timeseries for a given point and given variable defined by the user.
    Arguments: A dictionary object from the AJAX-ed JSON object that contains coordinates and the variable name.
    Author: Riley Hales
    Dependencies: netcdf4, numpy, datetime, random
    Last Updated: Oct 11 2018
    """
    values = []
    variable = str(data['variable'])
    coords = data['coords']
    tperiod = data['time']

    configs = app_configuration()
    data_dir = configs['thredds_data_dir']

    if tperiod == 'alltimes':
        path = os.path.join(data_dir, 'raw')
        files = os.listdir(path)
        files.sort()
    #else:
    #    path = os.path.join(data_dir, 'raw')
    #    allfiles = os.listdir(path)
    #    files = [nc for nc in allfiles if nc.startswith("GLDAS_NOAH025_M.A" + str(tperiod))]
    #    files.sort()

    # delete Mac's hidden .DS_Store file inside data directory
    path = os.path.join(data_dir, 'raw')
    my_list = os.listdir(path)

    for file in my_list:
        if file == ".DS_Store":
            os.remove(os.path.join(path, file))
            print(str(file) + " file deleted")

    # find the point of data array that corresponds to the user's choice, get the units of that variable
    dataset = netCDF4.Dataset(path + '/' + str(files[0]), 'r')
    nc_lons = dataset['lon'][:]
    nc_lats = dataset['lat'][:]

    adj_lon_ind = (numpy.abs(nc_lons - coords[0])).argmin()
    adj_lat_ind = (numpy.abs(nc_lats - coords[1])).argmin()

    units = dataset[variable].__dict__['units']
    dataset.close()


    # extract values at each timestep
    for nc in files:
        # set the time value for each file
        dataset = netCDF4.Dataset(path + '/' + nc, 'r')
        t_value = (dataset['time'].__dict__['units'])
        t_value = t_value[12:]
        t_step = datetime.datetime.strptime(t_value, "%Y-%m-%d %H:%M:%S")
        t_step = t_step + datetime.timedelta(hours=float(dataset['time'][:]))
        t_step = calendar.timegm(t_step.utctimetuple()) * 1000

        for time, var in enumerate(dataset['time'][:]):
            # get the value at the point
            val = float(dataset[variable][0, adj_lat_ind, adj_lon_ind].data)
            values.append((t_step, val))
        dataset.close()

    return_items = [units, values]

    return return_items
