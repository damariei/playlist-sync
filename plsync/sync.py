# sync.py
# Dmitri Amariei
# May 2013

from gmusicapi import WebClient
from spotify.manager import SpotifySessionManager

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
        pass

      else:
        raise Exception('No credentials provided!')
    elif service == "gmusic":
      if options.has_key('username') and options.has_key('password'):

        # Login to GMusic
        gm = WebClient()
        if gm.login(options['username'],options['password']):
          self.services.append({service: 'spotify', session: gm})
        else:
          raise Exception('Authentication Failure')

      else:
        raise Exception('No credentials provided!')
    else:
      raise Exception('No such service!')
