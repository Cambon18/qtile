#!/bin/bash
trizen --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile picom rofi brightnessctl pulseaudio pavucontrol dunst feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller networkmanager network-manager-applet volumeicon
sudo systemctl enable lightdm.service
sudo cp -r skel /etc
