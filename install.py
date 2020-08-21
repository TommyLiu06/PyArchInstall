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
import shutil
import linecache
import time

# Define colors
o = '\033[0m'       #---Original color
r = '\033[1;31m'	#---Red
g = '\033[1;32m'	#---Green
y = '\033[1;33m'	#---Yellow
lb = '\033[1;36m'	#---Light blue
w = '\033[1;37m'	#---White
db = '\033[1;34m'   #---Deep blue

# Make repository mirrorlist to back-file
try: # Check original repository mirrorlist file
    os.rename("/etc/pacman.d/mirrorlist", "/etc/pacman.d/mirrorlist.back")
except FileNotFoundError:
    # Copy back-file to original repository directory
    shutil.copy("mirrorlist.back", "/etc/pacman.d/irrorlist.back")
#Open the new repository mirrorlist file
os.mknod("/etc/pacman.d/mirrorlist")
mirrorlistRe = open("/etc/pacman.d/mirrorlist", "w")

os.system("clear")
print(db) #Deep blue
print("    _             _     _     _                  ")
print("   / \   _ __ ___| |__ | |   (_)_ __  _   ___  __")
print("  / _ \ | '__/ __| '_ \| |   | | '_ \| | | \ \/ /")
print(" / ___ \| | | (__| | | | |___| | | | | |_| |>  < ")
print("/_/   \_\_|  \___|_| |_|_____|_|_| |_|\__,_/_/\_\\")
print(lb) #Light blue
print(" ___           _        _ _       _   _             ")
print("|_ _|_ __  ___| |_ __ _| | | __ _| |_(_) ___  _ __  ")
print(" | || '_ \/ __| __/ _` | | |/ _` | __| |/ _ \| '_ \ ")
print(" | || | | \__ \ || (_| | | | (_| | |_| | (_) | | | |")
print("|___|_| |_|___/\__\__,_|_|_|\__,_|\__|_|\___/|_| |_|")
print(o) #Original color

#Select operations
while True:
    print("Choose a option: (1-5, 6, 7)")
    print("1. Operate the disks")
    print("2. Choose repository mirror")
    print("3. Install base system")
    print("4. Install other packages")
    print("5. Install bootstrap")
    print("6. About")
    print("7. Exit and remove temporary configuration")
    opr = input(g+"(1/2/3/4/5/6/7): "+o) # (opr = operation)

    # 1. Operate the disks
    if opr == '1':
        os.system("clear")
        # Edit disk parts (by hand)
        print(r) # Red
        print("1. Operate the disks")
        print("First, partition the disks"+o) 
        anotherDisk = 'y'
        while anotherDisk == 'y':
            print(r+"Here is the \"lsblk\" information:"+o)
            os.system("lsblk")
            print("")
            disk = input(g+"Choose a disk (default: \"sda\"): "+o) # Green
            # /dev/sd* = sd*
            if '/dev/' in disk:
                disk = disk.replace("/dev/","")
            # Default: sda
            elif disk == '':
                disk = 'sda'
            # Green
            tool = input("Choose your tool:\nfdisk\ncfdisk\ngdisk\ncgdisk\n"+g+"[(c)fdisk for MBR disk, (c)gdisk for GPT disk]: "+o)
            os.system("clear")
            print(r+"Running "+tool+" /dev/"+disk+o) # Red
            os.system(tool+" /dev/"+disk)
            anotherDisk = input(g+"Partition another disk?\n(y/n): "+o) # Green
            time.sleep(2)
            os.system("clear")
        else:
            pass
        os.system("clear")
        # Make filesystems
        os.system("clear")
        print(r) # Red
        print("Make filesystems")
        print("Here is the \"lsblk\" information:")
        print(o) # Original color
        os.system("lsblk")
        print("")
        anotherPart = 'y'
        part = input(g+"Choose a disk part (example: \"sda1\"): "+o) # Green
        while anotherPart == 'y':
            # /dev/sd** = sd**
            if '/dev/' in part:
                part = part.replace("/dev/","")
            # Green (fsType = filesystem type)
            fsType = input("Choose the filesystem type\n1. fat32\n2. ext2\n3. ext3\n4. ext4\n5. swap\n"+g+"(Fat32/ext2/...): "+o)
            if fsType == 'fat32':
                print(r+"Running \"mkfs.vfat -F 32 /dev/\""+part+o) # Red
                os.system("mkfs.vfat -F 32 /dev/"+part)
            elif fsType == 'swap':
                print(r+"Running \"mkswap /dev/\""+part+" && swapon /dev/"+part+o) # Red
                os.system("mkswap /dev/"+part+" && swapon /dev/"+part)
            else:
                print(r+"Running mkfs."+fsType+" /dev/"+part+o) # Red
                os.system("mkfs."+fsType+" /dev/"+part)
            time.sleep(1)
            os.system("clear")
            part = input(g+"choose another disk part or enter \"n\" to next step? : "+o) # Green
            if part == 'n':
                anotherPart = 'n'
        else:
            pass
        # Mount filesystems
        os.system("clear")
        print(r+"Mount filesystems") # Red
        print("Here is the \"lsblk\" information:"+o)
        os.system("lsblk")
        # (fs = filesystem)
        fs = input(g+"Choose a disk part (example: \"sda1\"): "+o) # Green
        anotherFs = 'y'
        while anotherFs == 'y':
            # /dev/sd** = sd**
            if '/dev/' in part:
                fs = fs.replace("/dev/","")
            mountPoint = input(g+"mount point(example: \"/\"): "+o) # Green
            if mountPoint != '/':
                os.makedirs("/mnt"+mountPoint)
            print(r+"Running \"mount /dev/\""+fs+" /mnt"+mountPoint+o)
            os.system("mount /dev/"+fs+" /mnt"+mountPoint)
            os.system("clear")
            fs = input(g+"Choose another disk part or enter \"n\" to next step? : "+o)
            if fs == 'n':
                anotherFs = 'n'
            time.sleep(2)
        else:
            pass
        os.system("clear")
    
    # 2. Choose repository mirror
    elif opr == '2':
        os.system("clear")
        country = input("Enter your country: ")
        countryNotFound = True
        while countryNotFound == True:
            if country == '':
                continue
            # Capital the first letter
            elif country.istitle() == False:
                country = country.capitalize()
            country = "## "+country+"\n"
            line = 1
            while line != 256:
                theLine = linecache.getline("mirrorlist-remake", line)
                if theLine == country:
                    countryNotFound = False
                    break
                elif line == 254:
                    countryNotFound = True
                    print(y+"Error: Country not found"+o)
                    country = input(g+"Enter your country again or press \"ENTER\" to use the default mirror: "+o)
                    break
                else:
                    line = line+1
        connectionMethod = input(g+"Use (1)HTTP or (2)HTTPS ? (1/2): "+o)
        if connectionMethod == '1':
            line = line+1
            url = linecache.getline("mirrorlist-remake", line)
        elif connectionMethod == '2':
            line = line+2
            url = linecache.getline("mirrorlist-remake", line)
            if url == 'No https url\n':
                print(y+"No https url!\nHTTP is automatically selected"+o)
                line = line-1
                url = linecache.getline("mirrorlist-remake", line)
        url = url.replace("\n", "") # remove "\n"
        print(r+"Your repository mirror is:\n"+db+url+o)
        print(url, file=mirrorlistRe)
        mirrorlistRe.close()
        print(r+"Updating pacman"+o)
        os.system("pacman -Sy")

    # 3. Install base system
    elif opr == '3':
        os.system("clear")
        print(r+"Installing base, base-devel, linux"+o)
        time.sleep(1)
        os.system("pacstrap /mnt base base-devel linux")
        print(r+"Installing linux-firmware, linux-headers, networkmanager, net-tools, dhcpcd, python3"+o)
        time.sleep(3)
        os.system("pacstrap /mnt linux-firmware linux-headers networkmanager net-tools dhcpcd python3")

    # 4. Install other packages
    elif opr == '4':
        print(r+"Install other packages"+o)
        print(g+"Choose packages: (y/n, default \"y\")"+o)
        xf86_video_intel = input("\nXf86-video-intel : ")
        vim = input("\nVim : ")
        emacs = input("\nEmacs : ")
        ntfs_3g = input("\nNtfs-3g : ")
        git = input("\nGit : ")
        python2 = input("\nPython2 : ")
        docker = input("\nDocker : ")
        neofetch = input("\nNeofetch : ")

        if xf86_video_intel == 'n':
            xf86_video_intel = ''
        else:
            xf86_video_intel = 'xf86-video-intel '
        if vim == 'n':
            vim = ''
        else:
            vim = 'vim '
        if emacs == 'n':
            emacs = ''
        else:
            emacs = 'emacs '
        if ntfs_3g == 'n':
            ntfs_3g = ''
        else:
            ntfs_3g = 'ntfs_3g '
        if git == 'n':
            git = ''
        else:
            git = 'git '
        if python2 == 'n':
            python2 = ''
        else:
            python2 = 'python2 '
        if neofetch == 'n':
            neofetch = ''
        else:
            neofetch = 'neofetch '

        print(r+"Installing "+xf86_video_intel+vim+emacs+ntfs_3g+git+python2+docker+neofetch+o)
        os.system("pacstrap /mnt "+xf86_video_intel+vim+emacs+ntfs_3g+git+python2+docker+neofetch)

    # 5. Install bootstrap
    elif opr == '5':
        shutil.copy("install_chroot.py", "/mnt/install_chroot.py")
        os.system("arch-chroot /mnt /usr/bin/python3 /install_chroot.py")

    # 6. About
    elif opr == '6':
        os.system("clear")
        print(y+"PyArchInstall") # Yellow
        print("   https://github.com/TommyLiu06/PyArchInstall")
        print("ArchLinux installation script based on Python.")
        print("License: GPL v3")
        print("")
        print("Script write by Tommy Liu")
        print("QQ: 1781880032 / 3611142393")
        print("Email: 1781880032@qq.com / 3611142393@qq.com")
        input(g+"Press \"ENTER\" to back to main menu"+o) # Original color
        os.system("clear")

    # 7. Exit and remove temporary configuration
    else:
        break
os.system("umount -R /mnt")
os.remove("/etc/pacman.d/mirrorlist")
os.rename("/etc/pacman.d/mirrorlist.back", "/etc/pacman.d/mirrorlist")
exit()

