import os
from .exceptions import ThemeNotFoundError
from .repositories import require_repo
from .config import Config


themes_dir = '_themes'
default_theme = 'default'


def list_themes(directory=None):
    """Gets a list of the installed themes."""
    repo = require_repo(directory)
    path = os.path.join(repo, themes_dir)
    return os.listdir(path) if os.path.isdir(path) else None


def use_theme(theme, directory=None):
    """Switches to the specified theme. This returns False if switching to the already active theme."""
    repo = require_repo(directory)
    if theme not in list_themes(directory):
        raise ThemeNotFoundError(theme)
    return Config(repo).set('theme', theme) != theme
