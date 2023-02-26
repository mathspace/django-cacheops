__version__ = '6.2'
VERSION = tuple(map(int, __version__.split('.')))

from .simple import *  # noqa
from .query import *  # noqa
from .invalidation import *  # noqa
from .reaper import *  # noqa
from .templatetags.cacheops import *  # noqa
