# -*- coding: utf-8 -*-
#  ________  ________  ________
# |\   __  \|\   __  \|\   ____\
# \ \  \|\  \ \  \|\  \ \  \___|	Asier Armenteros Cañibano
#  \ \   __  \ \   __  \ \  \		Custom Qtile Config
#   \ \  \ \  \ \  \ \  \ \  \____
#    \ \__\ \__\ \__\ \__\ \_______\
#     \|__|\|__|\|__|\|__|\|_______|

# The following comments are the copyright and licensing information from the default
# qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
# 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
#import arcobattery

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# FUNCTION KEYS

    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),

# SUPER + FUNCTION KEYS

   #Key([mod], "e", lazy.spawn('atom')),
   #Key([mod], "c", lazy.spawn('conky-toggle')),
   Key([mod], "f", lazy.spawn('thunar')), #FILE MANAGER
   #Key([mod], "m", lazy.spawn('pragha')),
   Key([mod], "q", lazy.spawn('qutebrowser')),
   Key([mod], "r", lazy.spawn('rofi-theme-selector')), #SELCTOR DE TEMA DE MENU
   #Key([mod], "t", lazy.spawn('urxvt')),
   #Key([mod], "v", lazy.spawn('pavucontrol')),
   #Key([mod], "w", lazy.spawn('vivaldi-stable')),
   Key([mod], "x", lazy.spawn('arcolinux-logout')),
   Key([mod], "b", lazy.spawn('firefox')),
   #Key([mod], "Escape", lazy.spawn('xkill')),
   Key([mod], "Return", lazy.spawn('termite')),
   #Key([mod], "KP_Enter", lazy.spawn('termite')),
   #Key([mod], "F1", lazy.spawn('vivaldi-stable')),
   #Key([mod], "F2", lazy.spawn('atom')),
   #Key([mod], "F3", lazy.spawn('inkscape')),
   #Key([mod], "F4", lazy.spawn('gimp')),
   #Key([mod], "F5", lazy.spawn('meld')),
   #Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
   #Key([mod], "F7", lazy.spawn('virtualbox')),
   #Key([mod], "F8", lazy.spawn('thunar')),
   #Key([mod], "F9", lazy.spawn('evolution')),
   #Key([mod], "F10", lazy.spawn("spotify")),
   #Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([mod], "m", lazy.spawn('rofi -show run')), #MENU

# SUPER + SHIFT KEYS

   #Key([mod, "shift"], "Return", lazy.spawn('thunar')),
   #Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    # Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS

    #Key(["mod1", "control"], "Next", lazy.spawn('conky-rotate -n')),
    #Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')),
    #Key(["mod1", "control"], "a", lazy.spawn('xfce4-appfinder')),
    #Key(["mod1", "control"], "b", lazy.spawn('thunar')),
    #Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    #Key(["mod1", "control"], "e", lazy.spawn('arcolinux-tweak-tool')),
    #Key(["mod1", "control"], "f", lazy.spawn('firefox')),
    #Key(["mod1", "control"], "g", lazy.spawn('chromium -no-default-browser-check')),
    #Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    #Key(["mod1", "control"], "k", lazy.spawn('arcolinux-logout')),
    #Key(["mod1", "control"], "l", lazy.spawn('arcolinux-logout')),
    #Key(["mod1", "control"], "m", lazy.spawn('xfce4-settings-manager')),
    #Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "p", lazy.spawn('pamac-manager')),
    #Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector')),
    #Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    #Key(["mod1", "control"], "t", lazy.spawn('termite')),
    #Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    #Key(["mod1", "control"], "v", lazy.spawn('vivaldi-stable')),
    #Key(["mod1", "control"], "w", lazy.spawn('arcolinux-welcome-app')),
    #Key(["mod1", "control"], "Return", lazy.spawn('termite')),

# ALT + ... KEYS

    #Key(["mod1"], "f", lazy.spawn('variety -f')),
    Key(["mod1"], "h", lazy.spawn('termite -e bashtop')),
    #Key(["mod1"], "n", lazy.spawn('variety -n')),
    #Key(["mod1"], "p", lazy.spawn('variety -p')),
    #Key(["mod1"], "t", lazy.spawn('variety -t')),
    #Key(["mod1"], "Up", lazy.spawn('variety --pause')),
    #Key(["mod1"], "Down", lazy.spawn('variety --resume')),
    #Key(["mod1"], "Left", lazy.spawn('variety -p')),
    #Key(["mod1"], "Right", lazy.spawn('variety -n')),
    #Key(["mod1"], "F2", lazy.spawn('gmrun')),
    Key(["mod1"], "m", lazy.spawn('xfce4-appfinder')),

# VARIETY KEYS WITH PYWAL

    #Key(["mod1", "shift"], "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    #Key(["mod1", "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    #Key(["mod1", "shift"], "n", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    #Key(["mod1", "shift"], "u", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

# CONTROL + SHIFT KEYS

    #Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

# SCREENSHOTS

    #Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]


##### GROUPS #####
group_names = [
        ("", {'layout': 'monadtall'}),
        ("", {'layout': 'monadtall'}),
        ("", {'layout': 'monadtall'}),
        ("", {'layout': 'max'}),
        ("ﱲ", {'layout': 'monadtall'}),
        ("", {'layout': 'monadtall'}),
        ("", {'layout': 'monadtall'}),
        ("", {'layout': 'monadtall'})

        ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
     layout.Floating(**layout_theme)
]


##### COLORS #####
colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name




##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Hack Nerd Font Bold",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

##### WIDGETS #####

def init_widgets_list():
    widgets_list = [
               widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 33,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.Prompt(
                        prompt=prompt,
                        font="Hack Nerd Font Bold",
                        padding=10,
                        foreground = colors[3],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 40,
                        foreground = colors[2],
                        background = colors[0]
                        ),
               widget.WindowName(
                        foreground = colors[6],
                        background = colors[0],
                        padding = 0
                        ),
               widget.TextBox(
                        text='◢',
                        background = colors[0],
                        foreground = colors[4],
                        padding=0,
                        fontsize=70
                        ),
               widget.TextBox(
                        text=" 🖬",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 0,
                        fontsize=14
                        ),
               widget.Memory(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='◢',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=70
                        ),
               widget.Net(
                        interface = "wlp60s0",
                        format = '{down} ↓↑ {up}',
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
               widget.TextBox(
                        text='◢',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=70
                        ),
               widget.TextBox(
                       text=" Vol:",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 0
                        ),
               widget.Volume(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='◢',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=70
                        ),
               widget.Battery(
                        charge_char='',
                        full_char='',
                        empty_char='',
                        discharge_char='',
                        unknown_char='',
                        format= '{char} {percent: 1.0%}',
                        foreground=colors[2],
                        background=colors[5]
                        ),
               widget.TextBox(
                        text='◢',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=70
                        ),
               widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[0],
                        background = colors[4],
                        padding = 0,
                        scale=0.7
                        ),
               widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[4],
                        padding = 5
                        ),
               widget.TextBox(
                        text='◢',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=70
                        ),
               widget.Clock(
                        foreground = colors[2],
                        background = colors[5],
                        format="%A, %B %d  [ %H:%M ]"
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[0],
                        background = colors[5]
                        ),
               widget.Systray(
                        background=colors[0],
                        padding = 5
                        ),
              ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

#ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
#BEGIN

#@hook.subscribe.client_new
#def assign_app_group(client):
#   d = {}
#
#   #########################################################
#   ################ assgin apps to groups ##################
#   #########################################################
#
#   d["1"] = []
#   d["2"] = ["qutebrowser", "firefox"]
#   d["3"] = []
#   d["4"] = []
#   d["5"] = []
#   d["6"] = []
#   d["7"] = []
#   ##########################################################
#   wm_class = client.window.get_wm_class()[0]
#
#   for i in range(len(d)):
#       if wm_class in list(d.values())[i]:
#           group = list(d.keys())[i]
#           client.togroup(group)
#           client.group.cmd_toscreen()
#
# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
