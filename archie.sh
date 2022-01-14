#!/bin/bash
trizen --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile python-pip python-psutil picom rofi brightnessctl pulseaudio pulseaudio-bluetooth pavucontrol volctl dunst feh arandr brave-bin alacritty gnome-disk-utility thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller vlc networkmanager networkmanager-openvpn network-manager-applet blueman numlockx pacman-contrib matcha-gtk-theme papirus-icon-theme papirus-folders
sudo systemctl enable bluetooth.service
sudo systemctl enable lightdm.service
sudo papirus-folders -C green
trizen --noconfirm -Rns papirus-folders
sudo cp -rv skel /etc
sudo cp -rv lightdm /etc
