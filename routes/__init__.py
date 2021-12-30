from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .login import *
from .register import *
from .logout import *
from .aboutus import *
from .contactus import *
from .cropdisease import *
from .result import *
from .livechat import *
from .loghistory import *
from .profile import *
from .dashboard import *