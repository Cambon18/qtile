#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
sudo pacman --noconfirm -S xorg-server xorg-xinit
trizen --noconfirm -Sy qtile rofi brightnessctl pulseadio pavucontrol feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller networkmanager networkmanager-applet
sudo mkdir /etc/skel/.config
sudo cp -r qtile /etc/skel/.config
sudo cp -r alacritty /etc/skel/.config
echo "qtile start" > /etc/skel/.xprofile
