#!/bin/bash
yay --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile python-pip python-psutil picom rofi brightnessctl playerctl pulseaudio pulseaudio-bluetooth pavucontrol volctl cbatticon notify-osd feh arandr gnome-keyring udiskie polkit-gnome networkmanager networkmanager-openvpn network-manager-applet blueman numlockx pacman-contrib matcha-gtk-theme papirus-icon-theme
yay --noconfirm -Sy brave-bin alacritty gnome-disk-utility nautilus nautilus-open-any-terminal vlc spotify ristretto
sudo systemctl enable bluetooth.service
sudo systemctl enable lightdm.service
yay --noconfirm -Sy papirus-folders
sudo papirus-folders -C green
yay --noconfirm -Rns papirus-folders
sudo cp -rv skel /etc
sudo touch /etc/skel/.config/picom.conf
sudo cp -rv lightdm /etc
