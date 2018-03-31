import os
import platform
from seaborn_flask_server.setup.config import (ProductionConfig,
                                               LocalDebugConfig)
from seaborn_file.file import relative_path


if platform.platform() == \
        "Linux-3.13.0-106-generic-x86_64-with-debian-jessie-sid":
    Config = ProductionConfig # this is my AWS linux box
else:
    Config = LocalDebugConfig

flask_folder = os.path.dirname(relative_path())
configuration = LocalDebugConfig(domain='demo.BenChristenson.com',
                                 name='Demo',
                                 flask_folder=flask_folder,
                                 data_folder=os.path.dirname(flask_folder),
                                 database_source='sqlite')
configuration.setup_logging()
