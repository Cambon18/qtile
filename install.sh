#!/bin/bash
trizen --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-gtk-greeter light-locker materia-gtk-theme qtile picom rofi brightnessctl pulseaudio pavucontrol dunst feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller networkmanager network-manager-applet volumeicon matcha-gtk-theme papirus-icon-theme papirus-folders
sudo systemctl enable lightdm.service
trizen --noconfirm -Sy lightdm-slick-greeter 
sudo sed -i '/#greeter-session/c greeter-session=lightdm-slick-greeter' /etc/lightdm/lightdm.conf
sudo sed -i '/^greeter-session/c greeter-session=lightdm-slick-greeter' /etc/lightdm/lightdm.conf
sudo cp -r lightdm /etc
sudo papirus-folders -C green
trizen --noconfirm -Rns papirus-folders lightdm-gtk-greeter
sudo cp -r skel /etc
