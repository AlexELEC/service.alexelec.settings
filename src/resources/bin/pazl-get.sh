#!/bin/sh

# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

URL_MAIN="https://github.com/AlexELEC/puzzle-tv/releases/download"
URL_LAST="https://github.com/AlexELEC/puzzle-tv/releases/latest"

PTV_DIR="/storage/.config/puzzle"
TEMP_DIR="/storage/.kodi/temp"

BACKUP_DIR="/tmp/puzzle"

################################ MAIN ##########################################

UPD_VER=`curl -s "$URL_LAST" | sed 's|.*tag\/||; s|">redirected.*||')`

# download URL
  if [ "$1" == "url" ] ; then
      if curl --output /dev/null --silent --head --fail "$URL_MAIN/$UPD_VER/puzzle-$UPD_VER.tar.bz2"
      then
        echo "$URL_MAIN/$UPD_VER/puzzle-$UPD_VER.tar.bz2"
      else
        echo "error"
      fi

# unpack
  elif [ "$1" == "install" ] ; then
      rm -fR $PTV_DIR
      mkdir -p $PTV_DIR
      tar -jxf $TEMP_DIR/puzzle-$UPD_VER.tar.bz2 -C $PTV_DIR
      rm -f $TEMP_DIR/puzzle-$UPD_VER.tar.bz2

# current version
  elif [ "$1" == "old" ] ; then
      CURRENT_VER=`cat $PTV_DIR/version`
      echo "$CURRENT_VER"

# update version
  elif [ "$1" == "new" ] ; then
      CURRENT_VER=`cat $PTV_DIR/version`
      if [ "$CURRENT_VER" != "$UPD_VER" ]; then
        echo "$UPD_VER"
      else
        echo "NOT UPDATE"
      fi

# backup
  elif [ "$1" == "backup" ] ; then
      mkdir -p $BACKUP_DIR
      [ -d "$PTV_DIR/settings" ] && cp -rf $PTV_DIR/settings $BACKUP_DIR
      [ -d "$PTV_DIR/user" ] && cp -rf $PTV_DIR/user $BACKUP_DIR
      [ -d "$PTV_DIR/logo" ] && cp -rf $PTV_DIR/logo $BACKUP_DIR

# restore
  elif [ "$1" == "restore" ] ; then
      [ -d "$BACKUP_DIR/settings" ] && cp -rf $BACKUP_DIR/settings $PTV_DIR
      [ -d "$BACKUP_DIR/user" ] && cp -rf $BACKUP_DIR/user $PTV_DIR
      [ -d "$BACKUP_DIR/logo" ] && cp -rf $BACKUP_DIR/logo $PTV_DIR
      rm -fR $BACKUP_DIR

# clean DB
  elif [ "$1" == "clean" ] ; then
      mv -f $PTV_DIR/user $PTV_DIR/user.bk
	  mkdir -p $PTV_DIR/user
	  cp -f $PTV_DIR/user.bk/__init__.py $PTV_DIR/user
      mv -f $PTV_DIR/settings $PTV_DIR/settings.bk
      mv -f $PTV_DIR/DBcnl.py $PTV_DIR/DBcnl.py.bk
      mv -f $PTV_DIR/DefGR.py $PTV_DIR/DefGR.py.bk
      cp -f $PTV_DIR/DBcnl.empty $PTV_DIR/DBcnl.py
      cp -f $PTV_DIR/DefGR.empty $PTV_DIR/DefGR.py
      mkdir -p $PTV_DIR/settings
      rm -fR $PTV_DIR/serv/*.cl
	  rm -fR $PTV_DIR/serv/*.pyo
	  rm -fR $PTV_DIR/*.pyo
      rm -fR $PTV_DIR/temp

  fi

exit 0
