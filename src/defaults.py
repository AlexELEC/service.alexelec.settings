# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2009-2013 Stephan Raue (stephan@openelec.tv)
# Copyright (C) 2013 Lutz Fiebach (lufie@openelec.tv)
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

import os

################################################################################
# Base
################################################################################

XBMC_USER_HOME = os.environ.get('XBMC_USER_HOME', '/storage/.kodi')
CONFIG_CACHE = os.environ.get('CONFIG_CACHE', '/storage/.cache')
USER_CONFIG = os.environ.get('USER_CONFIG', '/storage/.config')

BIN_DIR_EXT = '%s/addons/service.alexelec.settings/resources/bin' % XBMC_USER_HOME
BIN_DIR_INT = '/usr/share/kodi/addons/service.alexelec.settings/resources/bin'
SCRIPT_DIR = lambda : (BIN_DIR_EXT if os.path.exists(BIN_DIR_EXT) else BIN_DIR_INT)

################################################################################
# Connamn Module
################################################################################

connman = {
    'CONNMAN_DAEMON': '/usr/sbin/connmand',
    'WAIT_CONF_FILE': '%s/alexelec/network_wait' % CONFIG_CACHE,
    'ENABLED': lambda : (True if os.path.exists(connman['CONNMAN_DAEMON']) else False),
    }

################################################################################
# Bluez Module
################################################################################

bluetooth = {
    'BLUETOOTH_DAEMON': '/usr/lib/bluetooth/bluetoothd',
    'OBEX_DAEMON': '/usr/lib/bluetooth/obexd',
    'ENABLED': lambda : (True if os.path.exists(bluetooth['BLUETOOTH_DAEMON']) else False),
    'D_OBEXD_ROOT': '/storage/downloads/',
    }

################################################################################
# AceStream, TorrServer Module
################################################################################

ace = {
    'ENABLED': True,
    #ACESTREAM
    'D_ACE_DEBUG'     : '0',
    'ACE_GET_SRC'     : "%s/ace-get.sh" % SCRIPT_DIR(),
    #TORRSERVER
    'D_TORRSRV_PORT'  : '8090',
    'D_TORRSRV_DEBUG' : '0',
    'TORRSRV_GET_SRC' : "%s/torrsrv-get.sh" % SCRIPT_DIR(),
    }

aceplist = {
    'ENABLED'        : True,
    #TTV-LIST
    'D_CAT_SHOW'     : '1',
    'D_CAT_COMM'     : '1',
    'D_CAT_FILMS'    : '1',
    'D_CAT_EROS'     : '1',
    'D_CAT_NEWS'     : '1',
    'D_CAT_REGION'   : '0',
    'D_CAT_MUSIC'    : '0',
    'D_CAT_CHILDREN' : '0',
    'D_CAT_SPORT'    : '0',
    'D_CAT_RELIGION' : '0',
    'D_CAT_MAN'      : '0',
    'D_CAT_LEARN'    : '0',
    'D_CAT_ALLFON'   : '0',
    'D_ACETTV_IP'    : '0',
    'D_TTV_LOGIN'    : '',
    'D_TTV_PASSW'    : '',
    'D_TRANSLATE'    : 'Trash-TTV',
    'D_ACETTV_UPD'   : '0',
    'TTV_DEL_LIST'   : "rm -f /storage/.config/acestream/ttv-m3u/update.status",
    'TTV_RUN_LIST'   : "/usr/bin/ttvget-live",
    }

################################################################################
# TV Service Module
################################################################################

htscam = {
    'ENABLED'        : True,
    #TVHEADEND
    'D_TVH_DEBUG'    : '0',
    'D_TVH_FEINIT'   : '0',
    'D_TVH_ANTPOWER' : '0',
    'ANTPOWER'       : '/proc/aml_fe/antoverload',

    #CH LOGOS
    'URL_LOGOS_FILE'      : 'https://github.com/AlexELEC/channel-logos/releases/download/v1.0/logos.tar.bz2',
    'RUN_LOGOS'           : "%s/logos.sh" % SCRIPT_DIR(),
    'GET_CH_COUNT'        : "cat /tmp/tvh-count.logos",
    'GET_LOGO_COUNT'      : "wc -l /storage/.kodi/temp/logos_src/src_file.tmp | awk '{print $1}'",
    'GET_MISS_COUNT'      : "wc -l /tmp/miss_logo.log | awk '{print $1}'",
    'GET_TVH_STATUS'      : "%s/tvh-status.sh" % SCRIPT_DIR(),
    'LOGO_GET_LOG'        : "tail -n1 /tmp/logo_conv.log",
    'KILL_LOGO_SH'        : "killall -9 logos.sh",
    'D_LOGOS_CLEAR'       : '0',
    'D_LOGOS_BG_COLOR'    : 'GreyB',
    'D_LOGOS_FG_COLOR'    : '5',
    'D_LOGOS_TEXT_COLOR'  : 'black',
    }

################################################################################
# Service Module
################################################################################

services = {
    'ENABLED': True,
    'KERNEL_CMD': '/proc/cmdline',
    'SAMBA_NMDB': '/usr/sbin/nmbd',
    'SAMBA_SMDB': '/usr/sbin/smbd',
    'D_SAMBA_WORKGROUP': 'WORKGROUP',
    'D_SAMBA_SECURE': '0',
    'D_SAMBA_USERNAME': 'alexelec',
    'D_SAMBA_PASSWORD': 'alexelec',
    'D_SAMBA_MINPROTOCOL': 'SMB2',
    'D_SAMBA_MAXPROTOCOL': 'SMB3',
    'D_SAMBA_AUTOSHARE': '1',
    'SSH_DAEMON': '/usr/sbin/sshd',
    'OPT_SSH_NOPASSWD': "-o 'PasswordAuthentication no'",
    'D_SSH_DISABLE_PW_AUTH': '0',
    'AVAHI_DAEMON': '/usr/sbin/avahi-daemon',
    'CRON_DAEMON': '/sbin/crond',
    }

system = {
    'ENABLED': True,
    'KERNEL_CMD': '/proc/cmdline',
    'SET_CLOCK_CMD': '/sbin/hwclock --systohc --utc',
    'XBMC_RESET_FILE': '%s/reset_xbmc' % CONFIG_CACHE,
    'ALEXELEC_RESET_FILE': '%s/reset_oe' % CONFIG_CACHE,
    'KEYBOARD_INFO': '/usr/share/X11/xkb/rules/base.xml',
    'UDEV_KEYBOARD_INFO': '%s/xkb/layout' % CONFIG_CACHE,
    'NOX_KEYBOARD_INFO': '/usr/lib/keymaps',
    'BACKUP_DIRS': [
        XBMC_USER_HOME,
        USER_CONFIG,
        CONFIG_CACHE,
        '/storage/.ssh',
        ],
    'BACKUP_DESTINATION': '/storage/backup/',
    'RESTORE_DIR': '/storage/.restore/',
    }

about = {'ENABLED': True}

xdbus = {'ENABLED': True}

_services = {
    'sshd': ['sshd.service'],
    'avahi': ['avahi-daemon.service'],
    'samba': ['nmbd.service', 'smbd.service'],
    'bluez': ['bluetooth.service'],
    'obexd': ['obex.service'],
    'crond': ['cron.service'],
    'eventlircd': ['eventlircd.service'],
    'iptables': ['iptables.service'],
    'acestream': ['acestream.service'],
    'torrserver': ['torrserver.service'],
    'oscam': ['oscam.service'],
    'tvheadend': ['tvheadend.service'],
    }
