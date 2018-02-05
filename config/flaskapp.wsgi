import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/LiveLyrics/")

from run import app as application
application.secret_key = '\xcb\x15\xf7K40\xd4\xd0\x85"\xc7\x9c5\xcf\x8flZ\xed'
