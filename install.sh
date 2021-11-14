#!/bin/bash

echo -e "\n>>Instalando Qtile\c"
trizen --noconfirm -Sy qtile rofi brightnessctl feh xorg-xinit

sudo cp -r qtile/configs /etc/skel
