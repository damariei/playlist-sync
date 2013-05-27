try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Playlist Sync',
    'author': 'Dmitri Amariei',
    'url': 'https://github.com/damariei/playlist-sync',
    'author_email': 'dmitri.amariei@gmail.com',
    'version': '0.1',
    'install_requires': ['gmusicapi', 'spotify'],
    'packages': ['plsync'],
    'scripts': [],
    'name': 'playlist-sync'
}

setup(**config)
