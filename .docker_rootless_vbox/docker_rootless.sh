#!/bin/bash
# Author: 	3x3cut0r <executor55@gmx.de>
# Version:	0.1
# Date:		2021-02-19
#
# Description:
#  this script installs a rootless docker-host on a debian 10 virtualbox
#

# Virtualbox Settings:
#
# VM Name:          docker-host
# VM Typ:           Linux
# VM Version:       Debian (64-bit)
# VM optical img:   e.g.: debian-10.8.0-amd64-netinst.iso
# VM Boot-order:    optical, hard disk
# VM RAM:           4 GB
# VM CPU-Cores:     2
# VM CPU-Options:   PAE/NX activated
# VM GPU-RAM:       32MB
# VM Netwerk:       network-bridge
#

# Debian 10 Installation:
#
# Graphical install (Debian 10)
# language:         <choose your own>
# hostname:         docker-host
# root username:    root
# root password:    root
# username:         docker
# password:         docker
# ip:               dhcp
#
# Software to install:
# x SSH server
# x Standard-Systemtools
#

# set up static ip address in /etc/network/interfaces
#
# auto lo
# iface lo inet loopback
# iface enp0s3 inet static
#   address 192.168.15.254/24
#   gateway 192.168.15.1
#   dns-servers 8.8.8.8 8.8.4.4
#
# The primary network interface
# This is an autoconfigured IPv6 interface
# allow-hotplug enp0s3
# iface enp0s3 inet6 auto
#

# run as root first without args
if [ "$#" = "0" ]; then
    # check root
    if [ $UID -ne 0 ]; then echo -e "run as root (uid=0) to install prerequisites\nif you want do install docker, do:\n./docker_rootless.sh install"; exit 1; fi

    # check first run
    printf '\n\e[0;33m%-6s\e[m\n' " ==> APT: install prerequisites ... \n"
    read -p "do you want to continue? (y/N): " -n 1 -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]
    then
        echo "exited by user"
        exit 1
    fi

    # APT: prerequisites
    apt update && apt upgrade -y
    apt install \
            build-essential \
            curl \
            dkms \
            linux-headers-$(uname -r) \
            openssh-server \
            sudo \
            uidmap \
            unzip \
            wget \
            -y

    # VI: arrow key fix
    printf '\n\e[0;33m%-6s\e[m\n' " ==> VI: arrow key fix ... \n"
    sed -i s/set\ compatible/set\ nocompatible/g /etc/vim/vimrc.tiny

    # SSH: PermitRootLogin (optional)
    printf '\n\e[0;33m%-6s\e[m\n' " ==> SSH: PermitRootLogin ... \n"
    read -p "do you want to permit root login via ssh? (y/N): " -n 1 -r
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        sed -i s/#PermitRootLogin\ prohibit-password/PermitRootLogin\ yes/g /etc/ssh/sshd_config
        systemctl restart sshd
    fi

    # VBoxGuestTools: attach virtualbox guest tools to /dev/cdrom
    printf '\n\e[0;33m%-6s\e[m\n' " ==> VBoxGuestTools: attach virtualbox guest tools to /dev/cdrom ... \n"
    read -n 1 -s -r -p "attach virtualbox guest tools -> then press any key to continue ..."
    mount /dev/cdrom /mnt
    /mnt/VBoxLinuxAdditions.run

    # docker: prerequisites
    echo -e "# docker rootless mode prerequisites:\nkernel.unprivileged_userns_clone=1" >> /etc/sysctl.d/docker_rootless.conf
    sysctl --system
    modprobe overlay permit_mounts_in_userns=1

    # reboot
    printf '\n\e[0;33m%-6s\e[m\n' " ==> reboot, then login as docker to continue with './docker_rootless.sh install'\n"
    read -n 1 -s -r -p "press any key to continue ..."
    reboot

elif [ ! "$#" = "0" ]; then
    # install rootless docker
    printf '\n\e[0;33m%-6s\e[m\n' " ==> Docker: install rootless docker ... \n"
    if [ $UID -eq 0 ]; then echo "you need to login (via ssh) as docker (uid=1000) to install rootless docker!"; exit 1; fi
    curl -fsSL https://get.docker.com/rootless | sh
    sudo loginctl enable-linger docker
    echo -e "\n# Docker environment variables" >> ~/.bashrc
    echo "export PATH=/home/docker/bin:$PATH" >> ~/.bashrc
    echo "export DOCKER_HOST=unix:///run/user/1000/docker.sock" >> ~/.bashrc

    # reboot
    printf '\n\e[0;33m%-6s\e[m\n' " ==> reboot again, now you can use 'docker ...'\n"
    read -n 1 -s -r -p "press any key to continue ..."
    reboot
fi
