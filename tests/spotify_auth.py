# Test Spotify Authentication
import sys, os, getpass
sys.path.insert(1, os.path.join(sys.path[0], '../plsync/'))
from sync import SyncClient
import config

password = getpass.getpass()
keys =  open(config.spotify['keyfile'], 'rb').read()

ses = SyncClient()
ses.login('spotify', {'username': config.spotify['username'], 'password': password, 'keys': keys })
