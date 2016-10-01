from server import import getApp
import config

import sys, os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

logging.basicConfig(stream=sys.stderr)

application = getApp()