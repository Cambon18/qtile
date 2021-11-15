#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy qtile rofi brightnessctl feh
sudo cp -r qtile/skel /etc/skel || sudo cp -r Qtile/skel /etc/skel
cp -r qtile/skel/.config $HOME/.config || cp -r Qtile/skel/.config $HOME/.config
