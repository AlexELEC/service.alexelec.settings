#!/bin/sh

# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

. /etc/os-release

URL_MAIN="https://github.com/AlexELEC/AE-AML/releases/download"
URL_LAST="https://github.com/AlexELEC/AE-AML/releases/latest"

################################# MAIN #########################################

case "$1" in
  "ver-current")
      echo "$ALEXELEC_ARCH-$VERSION"
    ;;
  "ver-update")
      UPD_VER=`curl -s "$URL_LAST" | sed 's|.*tag\/||; s|">redirected.*||')`
      echo "$ALEXELEC_ARCH-$UPD_VER"
    ;;
  "check-url")
      UPD_VER=`curl -s "$URL_LAST" | sed 's|.*tag\/||; s|">redirected.*||')`
      if curl --output /dev/null --silent --head --fail "$URL_MAIN/$UPD_VER/$NAME-$ALEXELEC_ARCH-$UPD_VER.tar"
      then
        echo "$URL_MAIN/$UPD_VER/$NAME-$ALEXELEC_ARCH-$UPD_VER.tar"
      else
        echo "error"
      fi
    ;;
  "reboot")
      systemctl stop kodi
      if [ -f "/storage/.cache/services/acestream.conf" ]; then
        systemctl stop acestream
        mv -f /storage/.cache/services/acestream.conf /storage/.cache/services/acestream.disable
        rm -rf /storage/.config/acestream
      fi
      systemctl reboot
    ;;
esac

exit 0
