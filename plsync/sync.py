# sync.py
# Dmitri Amariei
# May 2013

from gmusicapi import Webclient
from spotify.manager import SpotifySessionManager

class SpotifyManager(SpotifySessionManager):

  result = None

  def __init__(self, keys, *a, **kw):
    self.application_key = keys 
    SpotifySessionManager.__init__(self, *a, **kw)
  
  def logged_in(self, session, error):
    if error:
      self.result = 'error'
    self.disconnect()

  def test(self):
    self.connect()

    if self.result=='error':
      self.result = None
      return False
    else:
      return True

class SyncClient:
  """ Manages and allows auth/syncing from different music streaming services.
  Currently supports Google Music and Spotify.
  """

  def __init__(self):
    self.services = []
    self.playlists = []


  def login(self, service, options):
    if service == "spotify":
      if options.has_key('username') and options.has_key('password') and options.has_key('keys'):
        # Login to Spotify
        sm = SpotifyManager(options['keys'], options['username'], options['password'])
        if sm.test():
          self.services.append({'service': 'spotify', 'session': sm})
        else:
          raise Exception('Authentication Failure')
      else:
        raise Exception('No credentials provided!')


    elif service == "gmusic":
      if options.has_key('username') and options.has_key('password'):
        # Login to GMusic
        gm = WebClient()
        if gm.login(options['username'], options['password']):
          self.services.append({'service': 'gmusic', 'session': gm})
        else:
          raise Exception('Authentication Failure')
      else:
        raise Exception('No credentials provided!')


    else:
      raise Exception('No such service!')

  
  def sync_playlists(self, playlist1, playlist2):

    if playlist1['service']==playlist2['service']:
      raise Exception('Cannot sync playlists from the same service')

