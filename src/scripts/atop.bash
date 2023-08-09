#!/bin/bash
# sudo apt-get install atop
# systemctl enable atop
# systemctl start atop
timeout 1 atop -pv > /home/$USER/Downloads/proc.txt
