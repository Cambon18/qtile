#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy qtile rofi brightnessctl feh
sudo cp -r qtile/qtile /etc/skel/.config/ || sudo cp -r Qtile/qtile /etc/skel/.config/
cp -r qtile/qtile $HOME/.config/ || cp -r Qtile/qtile $HOME/.config/
