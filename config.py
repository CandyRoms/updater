import os

class Config(object):

    UPSTREAM_URL = os.environ.get('UPSTREAM_URL', 'https://sourceforge.net/projects/candyroms/files/Official/Pie/builds.json')
    DOWNLOAD_BASE_URL = os.environ.get('DOWNLOAD_BASE_URL', 'https://sourceforge.net/projects/candyroms/files/Official/Pie')
