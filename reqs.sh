#!/bin/bash

green="\e[32m"
yellow="\e[33m"

clear && echo -e $yellow
echo "[!] Checking Requirements." && sleep 2
chmod +x entity.py
sleep 2 && echo -e $green
echo "[!] Requirements Good to GO."
