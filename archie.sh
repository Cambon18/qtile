#!/bin/bash
yay --noconfirm -Sy $(cat list-packages)
sudo systemctl enable bluetooth.service
sudo systemctl enable lightdm.service
sudo papirus-folders -C green
yay --noconfirm -Rns papirus-folders
sudo cp -rv skel /etc
sudo touch /etc/skel/.config/picom.conf
sudo cp -rv lightdm /etc
