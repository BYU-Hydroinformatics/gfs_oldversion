from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting

class GfsViewer(TethysAppBase):
    """
    Tethys app class for GFS Viewer.
    """

    name = 'GFS Viewer'
    index = 'gfs_viewer:home'
    icon = 'gfs_viewer/images/globe.png'
    package = 'gfs_viewer'
    root_url = 'gfs-viewer'
    color = '#002366'
    description = 'To view GFS time series data'
    tags = 'GFS'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='gfs-viewer',
                controller='gfs_viewer.controllers.home'
            ),

            # url maps for ajax calls
            UrlMap(
                name='generatePlot',
                url='gfs-viewer/generatePlot',
                controller='gfs_viewer.ajaxhandlers.generatePlot',
            ),
            UrlMap(
                name='getBounds',
                url='gfs-viewer/getBounds',
                controller='gfs_viewer.ajaxhandlers.getBounds',
            ),
            UrlMap(
                name='getPaths',
                url='gfs-viewer/getConfigs',
                controller='gfs_viewer.ajaxhandlers.getConfigs'
            ),

            # url map for api calls
            UrlMap(
                name='tsPlotValues',
                url='gfs-viewer/api/tsPlotValues',
                controller='gfs_viewer.api.tsPlotValues',
            ),
            UrlMap(
                name='getTimes',
                url='gfs-viewer/api/getTimes',
                controller='gfs_viewer.api.getTimes',
            ),
        )
        return url_maps

    def custom_settings(self):
        CustomSettings = (
            CustomSetting(
                name='Local Thredds Folder Path',
                type=CustomSetting.TYPE_STRING,
                description="Path to data in the folder mounted by Thredds (e.g. /home/thredds/myDataFolder/)",
                required=True,
                # /home/rchales/thredds/gfs/
            ),
            CustomSetting(
                name='Thredds WMS URL',
                type=CustomSetting.TYPE_STRING,
                description="URL to the folder of GFS data and .ncml files on the thredds server (e.g. tethys.byu.edu/thredds/myDataFolder/)",
                required=True,
                # http://127.0.0.1:7000/thredds/wms/testAll/
            ),
        )
        return CustomSettings
