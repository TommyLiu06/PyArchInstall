#! /usr/bin/python3
# Coding: UTF-8

#PyArchInstall
#   https://github.com/TommyLiu06/PyArchInstall
#ArchLinux installation script based on Python.
#License: GPL v3

#Script write by Tommy Liu
#QQ: 1781880032 / 3611142393
#Email: 1781880032@qq.com / 3611142393@qq.com

import os

# Define colors
o = '\033[0m'       #---Original color
r = '\033[1;31m'	#---Red
g = '\033[1;32m'	#---Green
y = '\033[1;33m'	#---Yellow
lb = '\033[1;36m'	#---Light blue
w = '\033[1;37m'	#---White
db = '\033[1;34m'   #---Deep blue

print(r+"5. Install bootstrap"+o)
ifBios = input(g+"Install GRUB for BIOS(y) or by hand(n) (y/n): "+o)
if ifBios == 'y':
    print(r+"Installing grub"+o)
    os.system("pacmac -S grub")
    dev = input("Where GRUB was installed? (default:/dev/sda): ")
    if dev == '':
        dev = 'sda'
    elif '/dev/' in dev:
        dev = dev.replace("/dev/","")
    os.system("grub-install --target=i386-pc /dev/"+dev)
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")
    print(r+"Now, umount filesystems and reboot."+o)
else:
    print(r+"Please install bootstrap by hand"+o)
os.system("umount -R /mnt")
os.remove("/etc/pacman.d/mirrorlist")
os.rename("/etc/pacman.d/mirrorlist.back", "/etc/pacman.d/mirrorlist")
exit()
