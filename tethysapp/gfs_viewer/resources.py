from .app import GfsViewer
import os

def gfs_variables():
    """
    List of plottable GFS variables
    """
    variables = {
        'Total Precipitation': 'tp',
        #'Air Temperature': 'Tair_f_inst',
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
