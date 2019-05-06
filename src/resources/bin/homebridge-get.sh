#!/bin/sh

# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

URL_MAIN="https://github.com/AlexELEC/homebridge/releases/download"
URL_LAST="https://github.com/AlexELEC/homebridge/releases/latest"

HBR_DIR="/storage/.usr_local"
TMP_DIR="/storage/.kodi/temp"

################################ MAIN ##########################################

UPD_VER=`curl -s "$URL_LAST" | sed 's|.*tag\/||; s|">redirected.*||')`

# download URL
  if [ "$1" == "url" ] ; then
      if curl --output /dev/null --silent --head --fail "$URL_MAIN/$UPD_VER/homebridge-$UPD_VER.tar.bz2"
      then
        echo "$URL_MAIN/$UPD_VER/homebridge-$UPD_VER.tar.bz2"
      else
        echo "error"
      fi

# unpack
  elif [ "$1" == "install" ] ; then
      rm -fR $HBR_DIR
      mkdir -p $HBR_DIR
      tar -jxf $TEMP_DIR/homebridge-$UPD_VER.tar.bz2 -C $HBR_DIR
      rm -f $TEMP_DIR/homebridge-$UPD_VER.tar.bz2

  fi

exit 0
