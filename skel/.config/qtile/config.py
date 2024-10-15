
import psutil
import subprocess
from libqtile import hook, layout, bar, widget
from libqtile.config import Key, Group, Drag, Click, Screen
from libqtile.lazy import lazy

## Atajos de teclado

mod = "mod4"

keys = [
  # Ocultar barra
  Key([mod], "f11", lazy.hide_show_bar()),
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
  # Playerctl
  Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
  Key([], "XF86AudioPause", lazy.spawn("playerctl play-pause")),
  Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
  Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
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
    'margin': 3
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
#    layout.TreeTab(),
#    layout.MonadWide(),
#    layout.Matrix(),
#    layout.Bsp(),
#    layout.RatioTile(),
#    layout.Columns(),
#    layout.Tile(),
#    layout.VerticalTile(),
#    layout.Zoomy(),
]

floating_layout = layout.Floating(border_width=0)

## Definimos Pantallas

config = {
    'font': 'Cantarell',
    'fontsize': 17
}

battery = psutil.sensors_battery()
if battery:
      widgets_principal = [
            widget.GroupBox(**config,hide_unused="True",highlight_method="line",urgent_alert_method="line",this_current_screen_border="#39FF14",this_screen_border="#39FF14"),
            widget.WindowName(**config),
            widget.CheckUpdates(**config,display_format=" Pacman: {updates} ",custom_command="checkupdates"),
            widget.CheckUpdates(**config,display_format=" AUR: {updates} ",custom_command="yay -Qua"),
            widget.CheckUpdates(**config,display_format=" Service: {updates} ",custom_command="systemctl list-units --failed | grep failed"),
            widget.CPU(**config,format="   {load_percent}%"),
            widget.ThermalSensor(**config),
            widget.Memory(**config,format=" {MemUsed: .1f}{mm}/{MemTotal: .0f}{mm} ",measure_mem="G"),
            widget.Systray(icon_size=25),
            widget.Battery(**config,discharge_char=' ',charge_char=' ',full_char=' ',empty_char=' ',format='{char}  {percent:2.0%}',show_short_text='',update_interval=1),
            widget.Clock(**config)
      ]
      widgets_secundaria = [
            widget.GroupBox(**config,hide_unused="True",highlight_method="line",urgent_alert_method="line",this_current_screen_border="#39FF14",this_screen_border="#39FF14"),
            widget.WindowName(**config),
            widget.Battery(**config,discharge_char=' ',charge_char=' ',full_char=' ',empty_char=' ',format='{char}  {percent:2.0%}',show_short_text='',update_interval=1),
            widget.Clock(**config)
      ]
else:
      widgets_principal = [
            widget.GroupBox(**config,hide_unused="True",highlight_method="line",urgent_alert_method="line",this_current_screen_border="#39FF14",this_screen_border="#39FF14"),
            widget.WindowName(**config),
            widget.CheckUpdates(**config,display_format=" Pacman: {updates} ",custom_command="checkupdates"),
            widget.CheckUpdates(**config,display_format=" AUR: {updates} ",custom_command="yay -Qua"),
            widget.CheckUpdates(**config,display_format=" Service: {updates} ",custom_command="systemctl list-units --failed | grep failed"),
            widget.CPU(**config,format="   {load_percent}%"),
            widget.ThermalSensor(**config),
            widget.Memory(**config,format=" {MemUsed: .1f}{mm}/{MemTotal: .0f}{mm} ",measure_mem="G"),
            widget.Systray(icon_size=25),
            widget.Clock(**config)
      ]
      widgets_secundaria = [
            widget.GroupBox(**config,hide_unused="True",highlight_method="line",urgent_alert_method="line",this_current_screen_border="#39FF14",this_screen_border="#39FF14"),
            widget.WindowName(**config),
            widget.Clock(**config)
      ]

screens = [Screen(top=bar.Bar(widgets_principal, 30))]

salida = subprocess.check_output("xrandr -d :0 | grep \ connected | wc -l", shell=True)

n = int(salida.decode('UTF-8'))

if n > 1:
    for i in range(1, n):
        screens.append(Screen(top=bar.Bar(widgets_secundaria, 30)))


## Variables

main = None
dgroups_key_binder = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
