#!/bin/sh

# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

if cat /proc/cmdline | grep -qw 'BOOT_IMAGE=/dev/boot' ; then
  echo "Abort. System in NAND."
  exit 1
fi

/usr/sbin/nand-remote &>/dev/null
echo "Reconfigure remote control done."
exit 0
