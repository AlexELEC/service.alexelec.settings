#!/bin/sh

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

URL_LAST="https://raw.githubusercontent.com/AlexELEC/acestream-aml/master/latest"
URL_MAIN="https://github.com/AlexELEC/acestream-aml/releases/download"

ACE_DIR="/storage/.config/acestream"
TEMP_DIR="/storage/.kodi/temp"

################################ MAIN ##########################################

VER=$(curl -s "$URL_LAST")

# download URL
  if [ "$1" == "url" ] ; then
      echo "$URL_MAIN/$VER/acestream-aml-$VER.tar.bz2"

# unpack
  elif [ "$1" == "unpack" ] ; then
      mkdir -p $ACE_DIR
      tar -jxf $TEMP_DIR/acestream-aml-$VER.tar.bz2 -C $ACE_DIR
      rm -f $TEMP_DIR/acestream-aml-$VER.tar.bz2
      touch $ACE_DIR/installed.acestream
  fi

exit 0
