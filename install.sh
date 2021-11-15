#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy qtile rofi brightnessctl feh
sudo cp -r qtile/.config /etc/skel/.config || sudo cp -r Qtile/.config /etc/skel/.config
cp -r qtile/.config $HOME/.config || cp -r Qtile/.config $HOME/.config
