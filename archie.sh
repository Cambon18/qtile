#!/bin/bash
yay --noconfirm -Sy $(cat list-packages)
sudo systemctl enable bluetooth.service
sudo systemctl enable cups.service
sudo cp -rv lightdm /etc

echo "greeter-session=lightdm-slick-greeter" >> /etc/lightdm/lightdm.conf
echo "greeter-show-manual-login=true" >> /etc/lightdm/lightdm.conf
echo "display-setup-script=cambonos-xrandr" >> /etc/lightdm/lightdm.conf
echo -e "[Desktop Entry]\nName=Qtile\nComment=Qtile Session\nExec=qtile start\nType=Application\nKeywords=wm;tiling" > /usr/share/xsessions/Proba.desktop

sudo systemctl enable lightdm.service
sudo papirus-folders -C green
yay --noconfirm -Rns papirus-folders
sudo cp -rv skel /etc
sudo touch /etc/skel/.config/picom.conf
