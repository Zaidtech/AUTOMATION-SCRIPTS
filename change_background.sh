# This script in bash changes wallpaper of the system after 30m time interval
# More work can be done as by fething live wallpapers form the net.
#!/bin/bash
while True; do
  for image in *.jpg; do
  #set image as wallpaper
  #echo "----------"
  #echo $image
  #echo "That was an image Setting it as wallpaper"
    gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/$image
    sleep 30m
done
done

