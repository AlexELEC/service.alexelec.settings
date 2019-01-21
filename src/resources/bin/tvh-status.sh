#!/bin/sh

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

LOCAL_TVH_CFG="/storage/.cache/services/tvheadend.conf"
EXT_TVH_CFG="/storage/.kodi/userdata/addon_data/pvr.hts/settings.xml"

  if [ -f "$LOCAL_TVH_CFG" ]; then
      TVH_URL="http://127.0.0.1:9981"
  elif [ -f "$EXT_TVH_CFG" ]; then
      HOST_EXT=`cat $EXT_TVH_CFG | grep 'setting id=\"host\"' | sed 's|^.*<setting id=\"host\" value=\"||; s|\".*$||'`
      PORT_EXT=`cat $EXT_TVH_CFG | grep 'setting id=\"http_port\"' | sed 's|^.*<setting id=\"http_port\" value=\"||; s|\".*$||'`
      TVH_URL="http://$HOST_EXT:$PORT_EXT"
  else
      echo 'ERROR'
      exit 1
  fi

ch_count=`curl -s $TVH_URL'/api/channel/grid?start=0&limit=1' | jq -r '.total'`
if [ -n "$ch_count" -a "$ch_count" -gt 0 ]; then
  echo "TVH_URL=\"$TVH_URL\"" > /tmp/tvh-url.logos
  echo "$ch_count" > /tmp/tvh-count.logos
  echo 'OK'
else
  echo 'ERROR'
fi
exit 0
