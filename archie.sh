#!/bin/bash
yay --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile python-pip python-psutil picom rofi brightnessctl pulseaudio pulseaudio-bluetooth pavucontrol volctl dunst feh arandr brave-bin alacritty gnome-disk-utility nautilus nautilus-open-any-terminal udiskie polkit-gnome vlc ristretto networkmanager networkmanager-openvpn network-manager-applet blueman numlockx pacman-contrib matcha-gtk-theme papirus-icon-theme papirus-folders
sudo systemctl enable bluetooth.service
sudo systemctl enable lightdm.service
sudo papirus-folders -C green
yay --noconfirm -Rns papirus-folders
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal alacritty
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal keybindings '<Ctrl><Alt>t'
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal new-tab true
sudo cp -rv skel /etc
sudo cp -rv lightdm /etc
