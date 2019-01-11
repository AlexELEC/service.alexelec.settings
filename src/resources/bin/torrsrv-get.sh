#!/bin/sh

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

TORRSRV_VER="TorrServer-linux-arm7"
URL_MAIN="https://github.com/AlexELEC/TorrServer/raw/master"

TORRSRV_DIR="/storage/.config/torrserver"
TORRSRV_BIN="$TORRSRV_DIR/bin/TorrServer"
TEMP_DIR="/storage/.kodi/temp"

################################ MAIN ##########################################

# download URL
  if [ "$1" == "url" ] ; then
      echo "$URL_MAIN/$TORRSRV_VER"

# unpack
  elif [ "$1" == "install" ] ; then
      mkdir -p $TORRSRV_DIR
      mkdir -p $TORRSRV_DIR/bin
      mv -f $TEMP_DIR/$TORRSRV_VER $TORRSRV_BIN
      chmod +x $TORRSRV_BIN
  fi

exit 0
