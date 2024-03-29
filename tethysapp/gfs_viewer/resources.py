from .app import GfsViewer
import os

def gfs_variables():
    """
    List of plottable GFS variables
    """
    variables = {
        'Total Precipitation': 'tp',
        'Temperature': 't',
        'Best (4-Layer) Lifted Index': '4lftx',
        'Convective Precipitation': 'acpcp',
        'Albedo': 'al',
        'Convective Available Potential Energy': 'cape',
        'Categorical Freezing Rain': 'cfrzr',
        'Ice Cover': 'ci',
        'Categorical Ice Pellets': 'cicep',
        'Convective Inhibition': 'cin',
        'Percent Frozen Precipitation': 'cpofp',
        'Categorical Rain': 'crain',
        'Categorical Snow': 'csnow',
        'Downward Long-Wave Radiation Flux': 'dlwrf',
        'Downward Short-Wave Radiation Flux': 'dswrf',
        'Field Capacity': 'fldcp',
        'Ground Heat Flux': 'gflux',
        'Wind Speed (Gust)': 'gust',
        'Haines Index': 'hindex',
        'Planetary Boundary Layer Height': 'hpbl',
        #'Land-Sea Coverage (Nearest Neighbor) [Land=1, Sea=0]': 'landn',
        'Surface Lifted Index': 'lftx',
        'Latent Heat Net Flux': 'lhtfl',
        'Land Cover [Land=1, Sea=0]': 'lsm',
        'Geopotential Height': 'orog',
        'Potential Evaporation Rate': 'pevpr',
        #'Precipitation Rate': 'prate',
        'Snow Depth': 'sde',
        'Water Equivalent of Accumulated Snow Depth': 'sdwe',
        'Sensible Heat Net Flux': 'shtfl',
        'Pressure at Surface': 'sp',
        'Sunshine Duration': 'SUNSD',
        'Zonal Flux of Gravity Wave Stress': 'u-gwd',
        'Momentum Flux, U-Component': 'uflx',
        'Upward Long-Wave Radiation Flux': 'ulwrf',
        'Upward Short-Wave Radiation Flux': 'uswrf',
        'Meridional Flux of Gravity Wave Stress': 'v-gwd',
        'Momentum Flux, V-Component': 'vflx',
        'Visibility': 'vis',
        'Water Runoff': 'watr',
        'Wilting Point': 'wilt',
        }
    return variables


def wms_colors():
    """
    Color options usable by thredds wms
    """
    color_opts = [
        ('SST-36', 'sst_36'),
        ('Greyscale', 'greyscale'),
        ('Rainbox', 'rainbow'),
        ('OCCAM', 'occam'),
        ('OCCAM Pastel', 'occam_pastel-30'),
        ('Red-Blue', 'redblue'),
        ('NetCDF Viewer', 'ncview'),
        ('ALG', 'alg'),
        ('ALG 2', 'alg2'),
        ('Ferret', 'ferret'),
        # ('Probability', 'prob'),
        # ('White-Blue', whiteblue'),
        # ('Grace', 'grace'),
        ]
    return color_opts


def get_times():
    """
    Time intervals of GFS data
    """
    times = [
        #(2019, 2019),
        ('All Available Times', 'alltimes'),
    ]
    return times


def app_configuration():
    app_workspace = GfsViewer.get_app_workspace()
    app_wksp_path = os.path.join(app_workspace.path, '')
    thredds_wms_url = GfsViewer.get_custom_setting("Thredds WMS URL")
    thredds_data_dir = GfsViewer.get_custom_setting("Local Thredds Folder Path")

    settings = {
        'app_wksp_path': app_wksp_path,
        'thredds_wms_url': thredds_wms_url,
        'thredds_data_dir': thredds_data_dir,
    }

    return settings
