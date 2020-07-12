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
# Torrents Module
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
    #PAZL TV
    'PAZL_GET_SRC'    : "%s/pazl-get.sh" % SCRIPT_DIR(),
    'D_STREAM_PTV'    : 'FFmpeg',
    'D_CACHE_PTV'     : '3',
    #ACEPROXY
    'D_ACEPROXY_DEBUG': 'INFO',
    }

################################################################################
# TV Service Module
################################################################################

htscam = {
    'ENABLED'        : True,
    #TVHEADEND
    'D_TVH_DEBUG'    : '0',
    'D_TVH_FEINIT'   : '0',
    'D_TVH_TVLINK'   : '0',
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
    # TVIP
    'D_TVIP_ACT_PATCH'  : '0',
    'D_TVIP_M3U'        : '',
    'D_TVIP_UPDATE'     : '0',
    'D_TVIP_TVH'        : '0',
    'D_TVIP_TVHIP'      : '',
    'D_TVIP_TVHEPG'     : '0',
    'D_TVIP_LAST'       : '0',
    'D_TVIP_RCTIME'     : '4',
    'D_TVIP_DEBUG'      : '0',
    'TVIP_DAEMON'       : '/home/tvip/tvip',
    # HomeBridge
    'HBR_GET_SRC'       : "%s/homebridge-get.sh" % SCRIPT_DIR(),
    'HBR_DAEMON'        : '/storage/.config/homebridge/config.json',
    'HBR_ISINSTALL'     : '/storage/.usr_local/bin/node',
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
    # UPDATE SYSTEM
    'LOCAL_UPDATE_DIR'  : '/storage/.update/',
    'RUN_UPDATE'        : "%s/update.sh" % SCRIPT_DIR(),
    # INSTALL TO NAND   
    'D_FULL_SET'        : '1',
    'NAND_INSTALL'      : "%s/installnand.sh" % SCRIPT_DIR(),
    'NAND_REMOTE'       : "%s/installrc.sh" % SCRIPT_DIR(),
    'NAND_REBOOT'       : "systemd-run %s/installfull.sh" % SCRIPT_DIR(),
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
    'homebridge': ['homebridge.service'],
    'iptables': ['iptables.service'],
    'acestream': ['acestream.service'],
    'torrserver': ['torrserver.service'],
    'ptv': ['ptv.service'],
    'aceproxy': ['aceproxy.service'],
    'dvbmode': ['dvbmode.service'],
    'oscam': ['oscam.service'],
    'tvheadend': ['tvheadend.service'],
    }
