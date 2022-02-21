#!/bin/bash
yay --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter qtile python-pip python-psutil picom rofi brightnessctl playerctl pulseaudio pulseaudio-bluetooth pavucontrol volctl notify-osd feh arandr gnome-keyring udiskie polkit-gnome networkmanager networkmanager-openvpn network-manager-applet blueman numlockx pacman-contrib matcha-gtk-theme papirus-icon-theme papirus-folders
yay --noconfirm -Sy brave-bin alacritty gnome-disk-utility nautilus nautilus-open-any-terminal vlc spotify ristretto
sudo systemctl enable bluetooth.service
sudo systemctl enable lightdm.service
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal alacritty
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal keybindings '<Ctrl><Alt>t'
gsettings set com.github.stunkymonkey.nautilus-open-any-terminal new-tab true
sudo mkdir -p /etc/skel/.config/dconf
sudo cp .config/dconf/user
sudo papirus-folders -C green
yay --noconfirm -Rns papirus-folders
sudo cp -rv skel /etc
sudo cp -rv lightdm /etc
abc123
