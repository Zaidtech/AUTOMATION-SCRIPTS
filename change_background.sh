#!/bin/bash
while 1>0; do
  for image in *.jpg; do
  #set image as wallpaper
  #echo "----------"
  #echo $image
  #echo "That was an image Setting it as wallpaper"
    gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/$image
    sleep 30m
done
done

