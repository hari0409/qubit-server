#!/bin/bash
data=timestamp=$(date +"%Y%m%d_%H%M%S")
docker run --rm -v "$1":/dumps cincan/volatility cmdline -f /dumps/"$2" >> /home/$USER/Downloads/vol_analysis.txt