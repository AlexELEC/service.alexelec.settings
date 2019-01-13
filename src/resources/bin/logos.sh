#!/bin/sh

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present Alex@ELEC (http://alexelec.in.ua)

. /storage/.cache/services/logos.conf

LOGOS_DIR="/storage/picons/tvh"
RNAME_DIR="/storage/picons/rename"

TVH_URL="http://127.0.0.1:9981"
[ -f /tmp/tvh-url.logos ] && . /tmp/tvh-url.logos
TVH_CH_COUNT=`curl -s $TVH_URL'/api/channel/grid?start=0&limit=1' | jq -r '.total'`
TVH_CH_COUNT=`expr $TVH_CH_COUNT - 1`

LOG_FILE="/tmp/logo_conv.log"
MISS_FILE="/tmp/miss_logo.log"
RENAME_FILE="/tmp/rename_logo.log"
TEMP_DIR="/storage/.kodi/temp"
SOURCE_DIR="$TEMP_DIR/logos_src" #logo source directory / путь к логотипам с прозрачными фонами
SOURCE_DIR_LOGOS="$SOURCE_DIR/logos" #logo source directory <logos>
SOURCE_DIR_BACKG="$SOURCE_DIR/backgrounds" #logo source directory <backgrounds>
SOURCE_FILE_NAMES="$SOURCE_DIR/src_file.tmp"
OUTPUT_DIR_TEMP="$LOGOS_DIR/tmp"
BACKGROUND="$SOURCE_DIR_BACKG/bg-${LOGOS_BG_COLOR}.png" #choose your background / путь к файлу фона логотипа
FOREGROUND="$SOURCE_DIR_BACKG/fg${LOGOS_FG_COLOR}.png" #choose your foreground / путь к файлу блика логотипа

RESIZE='220x164'
EXTENT='268x200'

#################################MAIN###########################################

# Unpack Logos
if [ "$1" == "unpack" ] ; then

  rm -rf $SOURCE_DIR
  mkdir -p $SOURCE_DIR
  tar -jxf $TEMP_DIR/logos.tar.bz2 -C $SOURCE_DIR
  rm -f $TEMP_DIR/logos.tar.bz2
  echo "Unpack logos completed."

# Create logos list file
elif [ "$1" == "list" ]; then
  rm -f $SOURCE_FILE_NAMES
  touch $SOURCE_FILE_NAMES

  # reading channels from TVH
  for channel in `seq 0 $TVH_CH_COUNT`; do
      ch_name=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .name' | sed 's/\// /; s/|//; s/://; s/  / /g; s/ test$//i; s/[ \t]*$//'`
      ch_icon=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .icon'  | awk -F\: '{print $1}'`
      if [ -z "$ch_name" -o "$ch_icon" != "picon" ]; then
          continue
      else
          IS_FILE=`find "$SOURCE_DIR_LOGOS" -iname "$ch_name.png" | grep -m1 .`
          if [ -n "$IS_FILE" ]; then
              IS_FILE_LIST=`grep -i -m1 -x "$IS_FILE" $SOURCE_FILE_NAMES`
              [ -z "$IS_FILE_LIST" ] && echo "$IS_FILE" >> $SOURCE_FILE_NAMES
          fi
      fi
  done
  echo "" > $LOG_FILE

# Convert downloaded logos
elif [ "$1" == "convert" ] ; then
  echo "" > $LOG_FILE
  mkdir -p $LOGOS_DIR
  [ "$LOGOS_CLEAR" == "1" ] && rm -rf $LOGOS_DIR/*

  cat $SOURCE_FILE_NAMES |
      while read -r FILE_NAMES ; do
          file=$(echo $FILE_NAMES)
          channel=$(basename "$file")
          echo_channel=$(echo "$channel" | sed -e 's/\.png$//')
          lcase_file=$(echo "$channel" | tr 'A-Z' 'a-z')
          target_file="$LOGOS_DIR/$lcase_file"
          echo "Convertion logo: $echo_channel" > $LOG_FILE
          if [ ! -e "$target_file" ] ; then
              convert +dither -background 'transparent' -resize $RESIZE -extent $EXTENT -gravity 'center' "$file" png:- 2> /dev/null | \
              composite - $BACKGROUND png:- 2> /dev/null | \
              composite -compose screen -blend 50x100 $FOREGROUND - "$target_file" 2> /dev/null
          fi
     done
  echo "Conversion logos completed." > $LOG_FILE

# Missing logos count
elif [ "$1" == "misslist" ] ; then
  rm -f $MISS_FILE

  # reading channels from TVH
  for channel in `seq 0 $TVH_CH_COUNT`; do
      ch_name=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .name' | sed 's/\// /; s/|//; s/://; s/  / /g; s/ test$//i; s/[ \t]*$//'`
      ch_icon=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .icon'  | awk -F\: '{print $1}'`
      if [ -z "$ch_name" -o "$ch_icon" != "picon" ]; then
          continue
      else
          lcase_name=$(echo "$ch_name" | tr 'A-Z' 'a-z' | sed 's/\// /')
          target_file="$LOGOS_DIR/$lcase_name.png"

          if [ ! -e "$target_file" ] ; then
              echo "$target_file" >> $MISS_FILE
          fi
      fi
  done
  if [ -f "$MISS_FILE" ]; then
      echo 'YES'
  else
      echo 'NONE'
  fi

# Generating the missing logos
elif [ "$1" == "missing" ] ; then
  rm -f $LOG_FILE
  touch $LOG_FILE
  rm -rf $OUTPUT_DIR_TEMP

  if [ -f "$MISS_FILE" ]; then
      mkdir -p $OUTPUT_DIR_TEMP

      # reading channels from TVH
      for channel in `seq 0 $TVH_CH_COUNT`; do
          ch_name=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .name' | sed 's/\// /; s/|//; s/://; s/  / /g; s/ test$//i; s/[ \t]*$//'`
          ch_icon=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .icon'  | awk -F\: '{print $1}'`
          if [ -z "$ch_name" -o "$ch_icon" != "picon" ]; then
              continue
          else
              lcase_name=$(echo "$ch_name" | tr 'A-Z' 'a-z' | sed 's/\// /')
              target_file="$LOGOS_DIR/$lcase_name.png"
              tmp_file="$OUTPUT_DIR_TEMP/$lcase_name.png"
              ch_text=$(echo "$ch_name" | sed 's/[ \t]*$//;s/ /\\n/g')

              if [ ! -e "$target_file" ] ; then
                  echo "Create missing logo: $ch_name" > $LOG_FILE
                  montage \
                      -size 268x200 \
                      -background none \
                      -gravity center \
                      -fill $LOGOS_TEXT_COLOR \
                      -font Open-Sans \
                      label:"$ch_text" +set label \
                      -shadow \
                      -background transparent \
                      -geometry +5+5 \
                      "$tmp_file" 2> /dev/null

                  convert +dither -background 'transparent' -resize $RESIZE -extent $EXTENT -gravity 'center' "$tmp_file" png:- 2> /dev/null | \
                  composite - $BACKGROUND png:- 2> /dev/null | \
                  composite -compose screen -blend 50x100 $FOREGROUND - "$target_file" 2> /dev/null
              fi
          fi
      done
      rm -rf $OUTPUT_DIR_TEMP
  fi

  rm -rf $SOURCE_DIR

  #rename
  echo "Rename logos..." > $LOG_FILE
  # reading channels from TVH
  rm -f $RENAME_FILE
  for channel in `seq 0 $TVH_CH_COUNT`; do
      ch_name=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .name' | sed 's/\// /; s/|//; s/://; s/  / /g; s/ test$//i; s/[ \t]*$//'`
      ch_icon=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .icon'  | awk -F\: '{print $1}'`
      if [ -z "$ch_name" -o "$ch_icon" != "picon" ]; then
          continue
      else
          ch_service=`curl -s $TVH_URL'/api/channel/grid?start='$channel'&limit=1' | jq -r '.entries | .[] | .icon' | sed 's/^picon:\/\///; s/\.png$//;'`
          echo "$ch_name -*- $ch_service" >> $RENAME_FILE
      fi
  done

  rm -rf $RNAME_DIR
  mkdir -p $RNAME_DIR
  cat $RENAME_FILE |
      while read -r RE_NAME ; do
          tmp_name=`echo "$RE_NAME" | awk -F' -\*-' '{print $1}' | sed 's/^[ \t]*//; s/[ \t]*$//'`
          old_name=$(echo "$tmp_name" | sed 's/\// /; s/|//; s/://' | tr 'A-Z' 'a-z')
          new_name=`echo "$RE_NAME" | awk -F'-\*- ' '{print $2}' | sed 's/^[ \t]*//; s/[ \t]*$//'`
          if [ -e "$LOGOS_DIR/$new_name.png" ] ; then
            continue
          fi
          cp -f "$LOGOS_DIR/$old_name.png" "$RNAME_DIR/$new_name.png"
      done

  rm -rf $LOGOS_DIR
  mv -f $RNAME_DIR $LOGOS_DIR

  echo "Create logos completed." > $LOG_FILE
fi

exit 0
