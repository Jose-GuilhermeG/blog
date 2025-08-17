from .apps import *
from .auth import *
from .basic_configs import *
from .database import *
from .rest_framework import *

#mysql
from pymysql import install_as_MySQLdb
install_as_MySQLdb()