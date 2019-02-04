#!/bin/sh

# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

SERVICE_DIR="/storage/.cache/services"
ACE_RUN="$SERVICE_DIR/acestream.conf"

[ -f "$SERVICE_DIR/nand.conf" ] && . $SERVICE_DIR/nand.conf
[ -z "$FULL_SET" ] && FULL_SET="1"

sleep 2
systemctl stop kodi

if [ "$FULL_SET" == "1" ]; then
  [ -f "$ACE_RUN" ] && systemctl stop acestream
  mkdir -p /tmp/data
  mount -o rw /dev/data /tmp/data
  cp -a /storage/. /tmp/data/
  umount /tmp/data
fi

echo "reboot from internal memory..."
/usr/sbin/rebootfromnand
systemctl reboot
