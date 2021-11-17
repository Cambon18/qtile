#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy qtile rofi brightnessctl pulseadio pavucontrol feh firefox alacritty thunar xdg-user-dirs gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller
cp -r qtile $HOME/.config/
