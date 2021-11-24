#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile rofi brightnessctl pulseaudio pavucontrol feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller networkmanager network-manager-applet volumeicon cbatticon
sudo systemctl enable lightdm.service
sudo mkdir /etc/skel/.config
sudo cp -r qtile /etc/skel/.config
sudo cp -r alacritty /etc/skel/.config
sudo cp -r .xprofile /etc/skel
sudo cp -r Imágenes /etc/skel
