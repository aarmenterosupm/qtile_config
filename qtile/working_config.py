# Qtile Config File
# http://www.qtile.org/
# https://www.youtube.com/channel/UCzTi9I3zApECTkukkMOpEEA/featured

import os
import subprocess

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

mod = "mod4"

keys = [
    # Window Configs

    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Change window sizes (MonadTall)
    Key([mod], "h", lazy.layout.grow(), lazy.layout.increase_nmaster()),
    Key([mod], "l", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),

    # Kill window
    Key([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Launch Apps

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show run")),

    # Browser
    Key([mod], "b", lazy.spawn("chromium")),

    # File Manager
    Key([mod], "f", lazy.spawn("thunar")),

    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Hardware (for laptops)

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Lock screen
    Key([mod], "l", lazy.spawn("dm-tool lock")),
]

colors = {
    "dark":  ["#282a36", "#282a36"],
    "grey":  ["#434758", "#434758"],
    "white": ["#ffffff", "#ffffff"],
    "pink":  ["#A77AC4", "#A77AC4"],
    "blue":  ["#7197E7", "#7197E7"]
}

widgets_list = [
    widget.Sep(
        linewidth=0,
        padding=6,
        foreground=colors["white"],
        background=colors["dark"]
    ),
    widget.GroupBox(
        font="Ubuntu Bold",
        fontsize=9,
        margin_y=0,
        margin_x=0,
        padding_y=9,
        padding_x=5,
        borderwidth=1,
        active=colors["white"],
        inactive=colors["white"],
        rounded=False,
        highlight_method="block",
        this_current_screen_border=colors["pink"],
        this_screen_border=colors ["grey"],
        other_current_screen_border=colors["dark"],
        other_screen_border=colors["dark"],
        foreground=colors["white"],
        background=colors["dark"]
    ),
    widget.Sep(
        linewidth=0,
        padding=10,
        foreground=colors["white"],
        background=colors["dark"]
    ),
    widget.WindowName(font="Ubuntu",
        fontsize=11,
        foreground=colors["pink"],
        background=colors["dark"],
        padding=5
    ),
    widget.Sep(
        linewidth=0,
        padding=5,
        foreground=colors["white"],
        background=colors["dark"]
    ),
    widget.Systray(
        background=colors["dark"],
        padding=5
    ),
    widget.Sep(
        linewidth=0,
        padding=5,
        foreground=colors["white"],
        background=colors["dark"]
    ),
    widget.Image(
        scale=True,
        filename="~/.config/qtile/img/bluedarkbar.png",
        background=colors["dark"]
    ),
    widget.TextBox(
        font="Ubuntu Bold",
        text=" ⟳",
        padding=5,
        foreground=colors["white"],
        background=colors["blue"],
        fontsize=14
    ),
    widget.Pacman(
        execute="alacritty",
        update_interval=1800,
        foreground=colors["white"],
        background=colors["blue"]
    ),
    widget.Image(
        scale=True,
        filename="~/.config/qtile/img/pinkbar.png",
        background=colors["dark"]
    ),
    widget.TextBox(
        text=" ↯",
        foreground=colors["white"],
        background=colors["pink"],
        padding=5,
        fontsize=14
    ),
    widget.Net(
        interface="wlp60s0",
        foreground=colors["white"],
        background=colors["pink"],
    ),
    widget.Image(
        scale=True,
        filename="~/.config/qtile/img/bluebar.png",
        background=colors["dark"]
    ),
    widget.Battery(
        charge_char='',
        full_char='',
        empty_char='',
        discharge_char='',
        unknown_char='',
        foreground=colors["white"],
        background=colors["blue"]
    ),
    widget.Image(
        scale=True,
        filename="~/.config/qtile/img/pinkbar.png",
        background=colors["dark"]
    ),
    widget.TextBox(
        font="Ubuntu Bold",
        text=" ☵",
        padding=5,
        foreground=colors["white"],
        background=colors["pink"],
        fontsize=14
    ),
    widget.CurrentLayout(
        foreground=colors["white"],
        background=colors["pink"],
        padding=5
    ),
    widget.Image(
        scale=True,
        filename="~/.config/qtile/img/bluebar.png",
        background=colors["dark"]
    ),
    widget.TextBox(
        font="Ubuntu Bold",
        text=" 🕒",
        foreground=colors["white"],
        background=colors["blue"],
        padding=5,
        fontsize=14
    ),
    widget.Clock(
        foreground=colors["white"],
        background=colors["blue"],
        format="%A, %B %d - %H:%M"
    ),
]

# Workspaces

groups = [Group(i) for i in ["NET", "DEV", "TERM", "MEDIA", "MISC"]]

for i in range(len(groups)):
    # Each workspace is identified by a number starting at 1
    actual_key = i + 1 
    keys.extend([
        # Switch to workspace N (actual_key)
        Key([mod], str(actual_key), lazy.group[groups[i].name].toscreen()),
        # Send window to workspace N (actual_key)
        Key([mod, "shift"], str(actual_key), lazy.window.togroup(groups[i].name)),
    ])

layouts = [
    layout.Max(),
    layout.MonadTall(border_focus=colors["pink"][0], border_width=1, margin=4)
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            widgets_list,
            24,
            opacity=0.95
        ),
    ),
    Screen(

    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},  # gitk
        {'wmclass': 'makebranch'},  # gitk
        {'wmclass': 'maketag'},  # gitk
        {'wname': 'branchdialog'},  # gitk
        {'wname': 'pinentry'},  # GPG key password entry
        {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ],
    border_focus=colors["blue"][0]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
