
from libqtile import hook
from os import path
import subprocess

## Autostart

@hook.subscribe.startup_once
def autostart():
  subprocess.call([os.path.expanduser('~/.config/qtile/autostart.sh')])
