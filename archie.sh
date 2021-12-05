#!/bin/bash
trizen --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile python-pip python-psutil picom rofi brightnessctl pulseaudio pavucontrol dunst feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller ristretto networkmanager networkmanager-openvpn network-manager-applet volumeicon blueman numlockx pacman-contrib matcha-gtk-theme papirus-icon-theme papirus-folders
sudo systemctl enable bluetooth.service
sudo systemctl enable lightdm.service
sudo papirus-folders -C green
trizen --noconfirm -Rns papirus-folders
sudo cp -r skel /etc
sudo cp -r lightdm /etc
