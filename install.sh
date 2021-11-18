#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy qtile rofi brightnessctl pulseadio pavucontrol feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller
sudo mkdir /etc/skel/.config 2>/dev/null
sudo cp -r qtile /etc/skel/.config
sudo cp -r alacritty /etc/skel/.config
