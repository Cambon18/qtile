
from libqtile import hook
from os import path
import subprocess

from libqtile.config import Key
from libqtile.command import lazy

## Autostart

@hook.subscribe.startup_once
def autostart():
  home = path.expanduser('~')
  subprocess.Popen([home + '/.config/qtile/autostart.sh'])

## Atajos de teclado

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
  # Cambiar entre ventanas
  ([mod], "j", lazy.layout.down()),
  ([mod], "k", lazy.layout.up()),
  ([mod], "h", lazy.layout.left()),
  ([mod], "l", lazy.layout.right()),
  # Cambiar tamaño ventana
  ([mod, "shift"], "l", lazy.layout.grow()),
  ([mod, "shift"], "h", lazy.layout.shrink()),
  # Cambiar posicion ventana
  ([mod, "shift"], "j", lazy.layout.shuffle_down()),
  ([mod, "shift"], "k", lazy.layout.shuffle_up()),
  # Cambiar distribucion de ventanas
  ([mod], "Tab", lazy.next_layout()),
  ([mod, "shift"], "Tab", lazy.prev_layout()),
  # Cerrar ventana
  ([mod], "w", lazy.window.kill()),
  # Cambiar de pantalla
  ([mod], "period", lazy.next_screen()),
  ([mod], "comma", lazy.prev_screen()),
  # Reiniciar Qtile
  ([mod, "control"], "r", lazy.restart()),
  # Cerrar Qtile
  ([mod, "control"], "q", lazy.shutdown()),
  # Line de comandos en el panel
  ([mod], "r", lazy.spawncmd()),
  # Menu
  ([mod], "m", lazy.spawn("rofi -show drun")),
  # Listar ventanas
  ([mod, "shift"], "m", lazy.spawn("rofi -show")),
  # Browser
  ([mod], "b", lazy.spawn("firefox")),
  # File Explorer
  ([mod], "f", lazy.spawn("thunar")),
  # Terminal
  ([mod], "Return", lazy.spawn("alacritty")),
  # Volume
  ([], "XF86AudioLowerVolume", lazy.spawn(
      "pactl set-sink-volume @DEFAULT_SINK@ -5%"
  )),
  ([], "XF86AudioRaiseVolume", lazy.spawn(
      "pactl set-sink-volume @DEFAULT_SINK@ +5%"
  )),
  ([], "XF86AudioMute", lazy.spawn(
      "pactl set-sink-mute @DEFAULT_SINK@ toggle"
  )),
  # Brightness
  ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
  ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
  
## Variables

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
