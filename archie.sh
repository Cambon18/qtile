#!/bin/bash
n=$(cat list-packages | wc -l)
i=1
while [[ $i -le $n ]]
do
	yay --noconfirm -Sy $(head -n $i list-packages | tail -n 1)
	i=$(( $i + 1 ))
done
sudo sed -i 's/\"qtile/\"\/usr\/bin\/qtile/g' /usr/lib/udev/rules.d/99-qtile.rules
sudo sed -i 's/\bqtile start\b/dbus-run-session qtile start/g' /usr/share/xsessions/qtile.desktop
sudo systemctl enable rtkit-daemon.service
sudo systemctl enable upower.service
sudo systemctl enable pipewire pipewire-pulse wireplumber
sudo systemctl enable bluetooth.service
sudo systemctl enable cups.service
sudo sed -i 's/\bresolve\b/mdns_minimal [NOTFOUND=return] resolve/g' /etc/nsswitch.conf
sudo cp -rv lightdm /etc
sudo systemctl enable lightdm.service
sudo papirus-folders -C green
sudo cp -rv skel /etc
sudo mkdir -p /usr/share/backgrounds
sudo mkdir -p /usr/share/slick-greeter/badges
sudo cp imagenes/wallpaper.jpeg /usr/share/backgrounds/
sudo cp imagenes/background.jpg /usr/share/backgrounds/
sudo cp imagenes/cambonos.png /usr/share/pixmaps/
sudo cp imagenes/qtile.png /usr/share/slick-greeter/badges/
sudo cp imagenes/qtile-wayland.png /usr/share/slick-greeter/badges/
