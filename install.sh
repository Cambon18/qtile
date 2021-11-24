#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy xorg xorg-server xorg-xrandr arandr qtile rofi brightnessctl pulseadio pavucontrol feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller networkmanager networkmanager-applet volumeicon cbatticon
sudo mkdir /etc/skel/.config
sudo cp -r qtile /etc/skel/.config
sudo cp -r alacritty /etc/skel/.config
sudo cp -r .xprofile /etc/skel
