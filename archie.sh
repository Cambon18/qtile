#!/bin/bash
n=$(wc -l list-packages)
i=1
while [[ $i -le $n ]]
do
	yay --noconfirm -Sy $(head -n $i list-packages | tail -n 1)
done
sudo systemctl enable bluetooth.service
sudo systemctl enable cups.service
sudo cp -rv lightdm /etc
sudo systemctl enable lightdm.service
sudo papirus-folders -C green
yay --noconfirm -Rns papirus-folders
sudo cp -rv skel /etc
sudo cp -rv slick-greeter /usr/share
sudo touch /etc/skel/.config/picom.conf
