# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

import os
import re
import glob
import time
import xbmc
import xbmcgui
import oeWindows
import threading
import subprocess

class htscam:

    ENABLED = False
    D_TVH_DEBUG = None
    D_TVH_FEINIT = None
    D_TVH_ANTPOWER = None
    ANTPOWER = None

    URL_LOGOS_FILE = None
    RUN_LOGOS = None
    GET_LOGO_COUNT = None
    GET_MISS_COUNT = None
    GET_TVH_STATUS = None
    LOGO_GET_LOG = None
    KILL_LOGO_SH = None
    D_LOGOS_CLEAR = None
    D_LOGOS_BG_COLOR = None
    D_LOGOS_FG_COLOR = None
    D_LOGOS_TEXT_COLOR = None

    menu = {'91': {
        'name': 43000,
        'menuLoader': 'load_menu',
        'listTyp': 'list',
        'InfoText': 4300,
        }}

    def __init__(self, oeMain):
        try:
            oeMain.dbg_log('tvserver::__init__', 'enter_function', 0)

            self.struct = {
                'oscam': {
                    'order': 1,
                    'name': 42020,
                    'not_supported': [],
                    'settings': {
                        'enable_oscam': {
                            'order': 1,
                            'name': 42021,
                            'value': '0',
                            'action': 'initialize_oscam',
                            'type': 'bool',
                            'InfoText': 4221,
                        },
                    },
                },
                'tvheadend': {
                    'order': 2,
                    'name': 42030,
                    'not_supported': [],
                    'settings': {
                        'enable_tvheadend': {
                            'order': 1,
                            'name': 42031,
                            'value': '0',
                            'action': 'initialize_tvheadend',
                            'type': 'bool',
                            'InfoText': 4231,
                        },
                        'tvh_feinit': {
                            'order': 2,
                            'name': 42032,
                            'value': '0',
                            'action': 'initialize_tvheadend',
                            'type': 'bool',
                            'parent': {'entry': 'enable_tvheadend','value': ['1']},
                            'InfoText': 4232,
                        },
                        'tvh_debug': {
                            'order': 3,
                            'name': 42033,
                            'value': '0',
                            'action': 'initialize_tvheadend',
                            'type': 'bool',
                            'parent': {'entry': 'enable_tvheadend','value': ['1']},
                            'InfoText': 4233,
                        },
                        'tvh_antpower': {
                            'order': 4,
                            'name': 42034,
                            'value': '0',
                            'action': 'initialize_tvheadend',
                            'type': 'bool',
                            'parent': {'entry': 'enable_tvheadend','value': ['1']},
                            'InfoText': 4234,
                        },
                    },
                },
                'logos': {
                    'order': 3,
                    'name': 43050,
                    'not_supported': [],
                    'settings': {
                        'logos_clear': {
                            'order': 1,
                            'name': 43052,
                            'value': '0',
                            'action': 'initialize_logos',
                            'type': 'bool',
                            'InfoText': 4352,
                        },
                        'logos_bg_color': {
                            'order': 2,
                            'name': 43053,
                            'value': 'Grey',
                            'values': ['Black', 'Blue', 'Green', 'Grey', 'GreyB', 'GreyBlue', 'GreyC', 'GreyM', 'Purple', 'Red', 'Vinous', 'White'],
                            'action': 'initialize_logos',
                            'type': 'multivalue',
                            'InfoText': 4353,
                        },
                        'logos_fg_color': {
                            'order': 3,
                            'name': 43054,
                            'value': '4',
                            'values': ['1', '2', '3', '4', '5'],
                            'action': 'initialize_logos',
                            'type': 'multivalue',
                            'InfoText': 4354,
                        },
                        'logos_text_color': {
                            'order': 4,
                            'name': 43055,
                            'value': 'black',
                            'values': ['white', 'black', 'red', 'blue', 'green', 'yellow'],
                            'action': 'initialize_logos',
                            'type': 'multivalue',
                            'InfoText': 4355,
                        },
                        'logos_create': {
                            'order': 5,
                            'name': 43056,
                            'value': None,
                            'action': 'execute_logos',
                            'type': 'button',
                            'InfoText': 4356,
                        },
                    },
                },
            }

            self.oe = oeMain

            oeMain.dbg_log('tvserver::__init__', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::__init__', 'ERROR: (%s)' % repr(e))

    def start_service(self):
        try:
            self.oe.dbg_log('tvserver::start_service', 'enter_function', 0)
            self.load_values()
            self.initialize_oscam()
            self.initialize_tvheadend()
            self.initialize_logos()
            self.oe.dbg_log('tvserver::start_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::start_service', 'ERROR: (%s)' % repr(e))

    def stop_service(self):
        try:
            self.oe.dbg_log('tvserver::stop_service', 'enter_function', 0)
            self.oe.dbg_log('tvserver::stop_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::stop_service', 'ERROR: (' + repr(e) + ')')

    def do_init(self):
        try:
            self.oe.dbg_log('tvserver::do_init', 'exit_function', 0)
            self.load_values()
            self.oe.dbg_log('tvserver::do_init', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::do_init', 'ERROR: (%s)' % repr(e))

    def set_value(self, listItem):
        try:
            self.oe.dbg_log('tvserver::set_value', 'enter_function', 0)
            self.struct[listItem.getProperty('category')]['settings'
                    ][listItem.getProperty('entry')]['value'] = \
                listItem.getProperty('value')

            self.oe.dbg_log('tvserver::set_value', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::set_value', 'ERROR: (' + repr(e) + ')')

    def load_menu(self, focusItem):
        try:
            self.oe.dbg_log('tvserver::load_menu', 'enter_function', 0)
            self.oe.winOeMain.build_menu(self.struct)
            self.oe.dbg_log('tvserver::load_menu', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::load_menu', 'ERROR: (%s)' % repr(e))

    def load_values(self):
        try:
            self.oe.dbg_log('tvserver::load_values', 'enter_function', 0)

            # OSCAM_DAEMON
            self.struct['oscam']['settings']['enable_oscam']['value'] = \
                    self.oe.get_service_state('oscam')

            # TVHEADEND
            self.struct['tvheadend']['settings']['enable_tvheadend']['value'] = \
                    self.oe.get_service_state('tvheadend')

            self.struct['tvheadend']['settings']['tvh_debug']['value'] = \
            self.oe.get_service_option('tvheadend', 'TVH_DEBUG', self.D_TVH_DEBUG).replace('"', '')

            self.struct['tvheadend']['settings']['tvh_feinit']['value'] = \
            self.oe.get_service_option('tvheadend', 'TVH_FEINIT', self.D_TVH_FEINIT).replace('"', '')

            # dvb-t2 antenna power
            if os.path.isfile(self.ANTPOWER):
                self.struct['tvheadend']['settings']['tvh_antpower']['value'] = \
                self.oe.get_service_option('tvheadend', 'TVH_ANTPOWER', self.D_TVH_ANTPOWER).replace('"', '')
            else:
                self.struct['tvheadend']['settings']['tvh_antpower']['hidden'] = 'true'

            # Logos
            self.struct['logos']['settings']['logos_clear']['value'] = \
            self.oe.get_service_option('logos', 'LOGOS_CLEAR', self.D_LOGOS_CLEAR).replace('"', '')

            self.struct['logos']['settings']['logos_bg_color']['value'] = \
            self.oe.get_service_option('logos', 'LOGOS_BG_COLOR', self.D_LOGOS_BG_COLOR).replace('"', '')

            self.struct['logos']['settings']['logos_fg_color']['value'] = \
            self.oe.get_service_option('logos', 'LOGOS_FG_COLOR', self.D_LOGOS_FG_COLOR).replace('"', '')

            self.struct['logos']['settings']['logos_text_color']['value'] = \
            self.oe.get_service_option('logos', 'LOGOS_TEXT_COLOR', self.D_LOGOS_TEXT_COLOR).replace('"', '')

            self.oe.dbg_log('tvserver::load_values', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::load_values', 'ERROR: (%s)' % repr(e))

    def initialize_oscam(self, **kwargs):
        try:
            self.oe.dbg_log('tvserver::initialize_oscam', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 0
            if self.struct['oscam']['settings']['enable_oscam']['value'] == '1':
                state = 1
            self.oe.set_service('oscam', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('tvserver::initialize_oscam', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('tvserver::initialize_oscam', 'ERROR: (%s)' % repr(e), 4)

    def initialize_tvheadend(self, **kwargs):
        try:
            self.oe.dbg_log('tvserver::initialize_tvheadend', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 0
            if self.struct['tvheadend']['settings']['enable_tvheadend']['value'] == '1':
                state = 1
                options['TVH_DEBUG']    = '"%s"' % self.struct['tvheadend']['settings']['tvh_debug']['value']
                options['TVH_FEINIT'] = '"%s"' % self.struct['tvheadend']['settings']['tvh_feinit']['value']
                options['TVH_ANTPOWER'] = '"%s"' % self.struct['tvheadend']['settings']['tvh_antpower']['value']
            self.oe.set_service('tvheadend', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('tvserver::initialize_tvheadend', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('tvserver::initialize_tvheadend', 'ERROR: (%s)' % repr(e), 4)

    def initialize_logos(self, **kwargs):
        try:
            self.oe.dbg_log('tvserver::initialize_logos', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 1
            options['LOGOS_CLEAR'] = '"%s"' % self.struct['logos']['settings']['logos_clear']['value']
            options['LOGOS_BG_COLOR'] = '"%s"' % self.struct['logos']['settings']['logos_bg_color']['value']
            options['LOGOS_FG_COLOR'] = '"%s"' % self.struct['logos']['settings']['logos_fg_color']['value']
            options['LOGOS_TEXT_COLOR'] = '"%s"' % self.struct['logos']['settings']['logos_text_color']['value']
            self.oe.set_service('logos', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('tvserver::initialize_logos', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('tvserver::initialize_logos', 'ERROR: (%s)' % repr(e), 4)

    def execute_logos(self, listItem=None, silent=False):
        try:
            self.oe.dbg_log('tvserver::execute_logos', 'enter_function', 0)

            # get TVH status
            tvh_status = self.oe.execute(self.GET_TVH_STATUS, 1).strip()
            if tvh_status == 'ERROR':
                xbmcDialog = xbmcgui.Dialog()
                answer = xbmcDialog.ok('Tvheadend logos',
                            'Error: Tvheadend is not running or can not be found a list of channels.')
                return

            self.download_file = self.URL_LOGOS_FILE
            if hasattr(self, 'download_file'):
                downloaded = self.oe.download_file(self.download_file, self.oe.TEMP + self.download_file.split('/')[-1], silent)
                if not downloaded is None:
                    self.oe.notify(self.oe._(32363), 'Unpack logos... Wait about 60 sec.')
                    self.oe.set_busy(1)
                    self.oe.execute(self.RUN_LOGOS + ' unpack', 0)

                    self.oe.execute(self.RUN_LOGOS + ' list', 0)
                    logo_count = self.oe.execute(self.GET_LOGO_COUNT, 1).strip()
                    logo_count = int(logo_count)
                    self.oe.set_busy(0)

                    self.oe.notify(self.oe._(32363), 'Conversion logos...')
                    subprocess.Popen(self.RUN_LOGOS + ' convert',
                                        shell=True,
                                        close_fds=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)

                    xbmcDialog = xbmcgui.DialogProgress()
                    xbmcDialog.create('Conversion logos', "",
                                'Number logos in list:  %d' % logo_count)

                    message = self.oe.execute(self.LOGO_GET_LOG, 1).strip()
                    message_tmp = message
                    i = 0
                    max_count = logo_count + 1
                    while not 'Conversion logos completed.' in message:
                        percent = int((i / float(logo_count)) * 100)
                        message = self.oe.execute(self.LOGO_GET_LOG, 1).strip()
                        if message_tmp != message:
                            message_tmp = message
                            if i < max_count:
                                i = i + 1
                        xbmcDialog.update(percent, "", "", message)
                        xbmc.sleep(500)
                        if xbmcDialog.iscanceled():
                            self.oe.execute(self.KILL_LOGO_SH, 0)
                            break

                    xbmc.sleep(1000)
                    xbmcDialog.close()

                    self.oe.notify(self.oe._(32363), 'Create missing logos list...')
                    self.oe.set_busy(1)
                    miss_msg = self.oe.execute(self.RUN_LOGOS + ' misslist', 1).strip()
                    self.oe.set_busy(0)

                    if miss_msg == 'YES':
                        logo_count = self.oe.execute(self.GET_MISS_COUNT, 1).strip()
                        logo_count = int(logo_count)
                        subprocess.Popen(self.RUN_LOGOS + ' missing',
                                        shell=True, 
                                        close_fds=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)

                        xbmcDialog = xbmcgui.DialogProgress()
                        xbmcDialog.create('Create missing logos', "",
                                'Number logos in list:  %d' % logo_count)

                        message = self.oe.execute(self.LOGO_GET_LOG, 1).strip()
                        message_tmp = message
                        i = 0
                        max_count = logo_count + 1
                        while not 'Create logos completed.' in message:
                            percent = int((i / float(logo_count)) * 100)
                            message = self.oe.execute(self.LOGO_GET_LOG, 1).strip()
                            if message_tmp != message:
                                message_tmp = message
                                if i < max_count:
                                    i = i + 1
                            xbmcDialog.update(percent, "", "", message)
                            xbmc.sleep(500)
                            if xbmcDialog.iscanceled():
                                self.oe.execute(self.KILL_LOGO_SH, 0)
                                break

                        xbmc.sleep(3000)
                        xbmcDialog.close()
                    else:
                        self.oe.notify(self.oe._(32363), 'Rename logos...')
                        self.oe.set_busy(1)
                        self.oe.execute(self.RUN_LOGOS + ' missing', 0)
                        self.oe.set_busy(0)
                        self.oe.notify(self.oe._(32363), 'Create logos completed.')

            self.oe.dbg_log('tvserver::execute_logos', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::execute_logos', 'ERROR: (' + repr(e) + ')')

    def exit(self):
        try:
            self.oe.dbg_log('tvserver::exit', 'enter_function', 0)
            self.oe.dbg_log('tvserver::exit', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('tvserver::exit', 'ERROR: (%s)' % repr(e), 4)
