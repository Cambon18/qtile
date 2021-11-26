#!/bin/bash
trizen --noconfirm -Sy xorg-server xorg-xinit lightdm lightdm-slick-greeter light-locker qtile picom rofi brightnessctl pulseaudio pavucontrol dunst feh brave-bin alacritty thunar gvfs gvfs-smb thunar-volman thunar-archive-plugin file-roller networkmanager network-manager-applet volumeicon papirus-icon-theme
sudo sed -i '/#greeter-session/c greeter-session=lightdm-slick-greeter' /etc/lightdm/lightdm.conf
sudo sed -i '/greeter-session/c greeter-session=lightdm-slick-greeter' /etc/lightdm/lightdm.conf
sudo systemctl enable lightdm.service
sudo cp -r skel /etc
