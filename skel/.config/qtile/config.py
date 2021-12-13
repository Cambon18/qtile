
from libqtile import hook, layout, bar, widget
from libqtile.config import Key, Group, Drag, Click, Screen
from libqtile.command import lazy

## Atajos de teclado

mod = "mod4"

keys = [
  # Cambiar entre ventanas
  Key([mod], "j", lazy.layout.down()),
  Key([mod], "k", lazy.layout.up()),
  Key([mod], "h", lazy.layout.left()),
  Key([mod], "l", lazy.layout.right()),
  # Cambiar tamaño ventana
  Key([mod, "shift"], "l", lazy.layout.grow()),
  Key([mod, "shift"], "h", lazy.layout.shrink()),
  # Cambiar posicion ventana
  Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
  Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
  # Cambiar a flotante una ventana
  Key([mod, "shift"], "f", lazy.window.toggle_floating()),
  # Cambiar distribucion de ventanas
  Key([mod], "Tab", lazy.next_layout()),
  Key([mod, "shift"], "Tab", lazy.prev_layout()),
  # Cerrar ventana
  Key([mod], "w", lazy.window.kill()),
  # Cambiar de pantalla
  Key([mod], "period", lazy.next_screen()),
  Key([mod], "comma", lazy.prev_screen()),
  # Bloquear pantalla
  Key([mod, "control"], "l", lazy.spawn("dm-tool lock")),
  # Reiniciar Qtile
  Key([mod, "control"], "r", lazy.restart()),
  # Cerrar Qtile
  Key([mod, "control"], "q", lazy.shutdown()),
  # Apagar ordenador
  Key([mod, "control"], "s", lazy.spawn("shutdown -h now")),
  # Menu
  Key([mod], "d", lazy.spawn("rofi -show drun")),
  # Listar ventanas
  Key([mod, "shift"], "d", lazy.spawn("rofi -show")),
  # Menu ssh
  Key([mod], "s", lazy.spawn("rofi -show ssh")),
  # Browser
  Key([mod], "b", lazy.spawn("brave")),
  # File Explorer
  Key([mod], "f", lazy.spawn("thunar")),
  # Terminal
  Key([mod], "Return", lazy.spawn("alacritty")),
  # Volume
  Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
  Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
  Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
  # Brightness
  Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
  Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

## Teclas raton

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

## Grupos

groups = [Group(i) for i in [
    "1: ","2: ", "3: ", "4: ",  "5: ",  "6: ",  "7: "
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

## Distribuciones de ventanas

layout_conf = {
    'border_focus': '#39FF14',
    'border_width': 3,
    'margin': 7
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
#    layout.MonadWide(),
    layout.Matrix(**layout_conf),
#    layout.Bsp(),
#    layout.RatioTile(),
#    layout.Columns(),
#    layout.Tile(),
#    layout.TreeTab(),
#    layout.VerticalTile(),
#    layout.Zoomy(),
]

## Definimos Barra

config = {
    'font': 'Cantarell',
    'fontsize': 17
}

screens = [
  Screen(
    top=bar.Bar([
      widget.GroupBox(**config,hide_unused="True",highlight_method="line",urgent_alert_method="line",this_current_screen_border="#39FF14",this_screen_border="#39FF14"),
      widget.WindowName(**config),
      widget.CheckUpdates(**config,display_format=" Pacman: {updates} ",custom_command="checkupdates"),
      widget.CheckUpdates(**config,display_format=" AUR: {updates} ",custom_command="trizen -Qua"),
      widget.CPU(**config,format="   {load_percent}%"),
      widget.Memory(**config,format=" {MemUsed: .1f}{mm}/{MemTotal: .0f}{mm} ",measure_mem="G"),
#      widget.CurrentLayoutIcon(scale=0.6),
#      widget.CurrentLayout(**config),
      widget.Systray(icon_size=25),
      widget.Battery(**config,discharge_char=' ',charge_char=' ',full_char=' ',empty_char=' ',format='{char}  {percent:2.0%}',show_short_text='',update_interval=1),
      widget.Clock(**config)
      ], 30)),
]


## Variables

main = None
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
