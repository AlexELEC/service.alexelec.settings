#!/bin/sh

# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

if cat /proc/cmdline | grep -qw 'BOOT_IMAGE=/dev/boot' ; then
  echo "Abort. System in NAND."
  exit 1
fi

if [ -f /etc/os-release ]; then
  . /etc/os-release
else
  echo "Abort. Unknown system."
  exit 1
fi

if [ "$ALEXELEC_ARCH" == "S905.arm" -o "$ALEXELEC_ARCH" == "S912.arm" ] ; then
  if [ ! -e /dev/boot -o ! -e /dev/system -o ! -e /dev/data -o ! -e /dev/dtb ]; then
    echo "Abort. BOOT, SYTEM, DATA or DTB partitions is missing."
    exit 1
  fi
fi

IMAGE_KERNEL="/flash/kernel.img"
IMAGE_SYSTEM="/flash/SYSTEM"
IMAGE_DTB="/flash/dtb.img"
IMAGE_LOGO="/usr/share/bootloader/logo.img"

install_to_nand() {
  if [ -f "$IMAGE_KERNEL" -a -f "$IMAGE_SYSTEM" ]; then

    if grep -q /dev/system /proc/mounts ; then
      umount -f /dev/system
    fi
    if systemctl is-active storage-nand.mount &>/dev/null ; then
      systemctl stop storage-nand.mount
    fi
    mkdir -p /tmp/system

    mount -o rw,remount /flash

    # Writing kernel image
    dd if="$IMAGE_KERNEL" of=/dev/boot bs=64k status=none &>/dev/null

    # Formatting SYSTEM partition
    mke2fs -F -q -t ext4 -m 0 /dev/system > /dev/null
    e2fsck -n /dev/system &> /dev/null

    # Copying SYSTEM files
    mount -o rw /dev/system /tmp/system
    cp "$IMAGE_SYSTEM" /tmp/system && sync
    umount /tmp/system

    if [ "$ALEXELEC_ARCH" == "S905.arm" -o "$ALEXELEC_ARCH" == "S912.arm" ]; then
      if [ -f "$IMAGE_DTB" ]; then
        dd if=/dev/zero of=/dev/dtb bs=256k count=1 &>/dev/null
        dd if="$IMAGE_DTB" of=/dev/dtb bs=256k &>/dev/null
      fi
      [ -f "$IMAGE_LOGO" ] && dd if="$IMAGE_LOGO" of=/dev/logo bs=64k status=none &>/dev/null
    fi

    # Formatting DATA partition
    mke2fs -F -q -t ext4 -m 0 /dev/data > /dev/null
    e2fsck -n /dev/data &> /dev/null

    echo "Done! Install AlexELEC completed."
  else
    echo "No AlexELEC image found on /flash! Exiting..."
    exit 1
  fi
}

install_to_nand
exit 0
