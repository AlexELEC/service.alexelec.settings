# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

import os
import glob
import xbmc
import xbmcgui

class ace:

    ENABLED=False
    D_ACE_DEBUG = None
    ACE_GET_SRC = None
    D_TORRSRV_PORT = None
    D_TORRSRV_DEBUG = None
    TORRSRV_GET_SRC = None
    PAZL_GET_SRC = None

    menu = {'92': {
        'name': 34000,
        'menuLoader': 'load_menu',
        'listTyp': 'list',
        'InfoText': 3400,
        }}

    def __init__(self, oeMain):
        try:
            oeMain.dbg_log('ace::__init__', 'enter_function', 0)
            self.struct = {
                'acestream': {
                    'order': 1,
                    'name': 34010,
                    'not_supported': [],
                    'settings': {
                        'enable_acestream': {
                            'order': 1,
                            'name': 34011,
                            'value': None,
                            'action': 'initialize_acestream',
                            'type': 'bool',
                            'InfoText': 3411,
                            },
                        'ace_debug': {
                            'order': 2,
                            'name': 34012,
                            'value': None,
                            'action': 'initialize_acestream',
                            'type': 'bool',
                            'parent': {
                                'entry': 'enable_acestream',
                                'value': ['1']
                                },
                            'InfoText': 3412,
                            },
                        },
                    },
                'torrserver': {
                    'order': 2,
                    'name': 34080,
                    'not_supported': [],
                    'settings': {
                        'enable_torrserver': {
                            'order': 1,
                            'name': 34011,
                            'value': None,
                            'action': 'initialize_torrserver',
                            'type': 'bool',
                            'InfoText': 3481,
                            },
                        'torrsrv_port': {
                            'order': 2,
                            'name': 34082,
                            'value': None,
                            'action': 'initialize_torrserver',
                            'type': 'num',
                            'parent': {
                                'entry': 'enable_torrserver',
                                'value': ['1']
                                },
                            'InfoText': 3482,
                            },
                        'torrsrv_debug': {
                            'order': 3,
                            'name': 34012,
                            'value': None,
                            'action': 'initialize_torrserver',
                            'type': 'bool',
                            'parent': {
                                'entry': 'enable_torrserver',
                                'value': ['1']
                                },
                            'InfoText': 3483,
                            },
                        },
                    },
                'ptv': {
                    'order': 3,
                    'name': 34090,
                    'not_supported': [],
                    'settings': {
                        'enable_ptv': {
                            'order': 1,
                            'name': 34011,
                            'value': None,
                            'action': 'initialize_ptv',
                            'type': 'bool',
                            'InfoText': 3491,
                            },
                        'empty_ptv': {
                            'order': 2,
                            'name': 34092,
                            'value': '0',
                            'action': 'clean_ptv',
                            'type': 'button',
                            'parent': {
                                'entry': 'enable_ptv',
                                'value': ['1']
                                },
                            'InfoText': 3492,
                            },
                        'upd_ptv': {
                            'order': 3,
                            'name': 34093,
                            'value': '0',
                            'action': 'update_ptv',
                            'type': 'button',
                            'parent': {
                                'entry': 'enable_ptv',
                                'value': ['1']
                                },
                            'InfoText': 3493,
                            },
                        },
                    },
            }

            self.oe = oeMain
            oeMain.dbg_log('ace::__init__', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::__init__', 'ERROR: (%s)' % repr(e))

    def start_service(self):
        try:
            self.oe.dbg_log('ace::start_service', 'enter_function', 0)
            self.load_values()
            self.initialize_acestream()
            self.initialize_torrserver()
            self.initialize_ptv()
            self.oe.dbg_log('ace::start_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::start_service', 'ERROR: (%s)' % repr(e))

    def stop_service(self):
        try:
            self.oe.dbg_log('ace::stop_service', 'enter_function', 0)
            self.oe.dbg_log('ace::stop_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::stop_service', 'ERROR: (' + repr(e) + ')')

    def do_init(self):
        try:
            self.oe.dbg_log('ace::do_init', 'exit_function', 0)
            self.load_values()
            self.oe.dbg_log('ace::do_init', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::do_init', 'ERROR: (%s)' % repr(e))

    def set_value(self, listItem):
        try:
            self.oe.dbg_log('ace::set_value', 'enter_function', 0)
            self.struct[listItem.getProperty('category')]['settings'][listItem.getProperty('entry')]['value'] = listItem.getProperty('value')
            self.oe.dbg_log('ace::set_value', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::set_value', 'ERROR: (' + repr(e) + ')')

    def load_menu(self, focusItem):
        try:
            self.oe.dbg_log('ace::load_menu', 'enter_function', 0)
            self.oe.winOeMain.build_menu(self.struct)
            self.oe.dbg_log('ace::load_menu', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::load_menu', 'ERROR: (%s)' % repr(e))

    def load_values(self):
        try:
            self.oe.dbg_log('ace::load_values', 'enter_function', 0)

            #ACESTREAM
            self.struct['acestream']['settings']['enable_acestream']['value'] = \
                    self.oe.get_service_state('acestream')

            self.struct['acestream']['settings']['ace_debug']['value'] = \
            self.oe.get_service_option('acestream', 'ACE_DEBUG', self.D_ACE_DEBUG).replace('"', '')

            #TORRSERVER
            self.struct['torrserver']['settings']['enable_torrserver']['value'] = \
                    self.oe.get_service_state('torrserver')

            self.struct['torrserver']['settings']['torrsrv_port']['value'] = \
            self.oe.get_service_option('torrserver', 'TORRSRV_PORT', self.D_TORRSRV_PORT).replace('"', '')

            self.struct['torrserver']['settings']['torrsrv_debug']['value'] = \
            self.oe.get_service_option('torrserver', 'TORRSRV_DEBUG', self.D_TORRSRV_DEBUG).replace('"', '')

            #PAZL TV
            self.struct['ptv']['settings']['enable_ptv']['value'] = \
                    self.oe.get_service_state('ptv')

            self.oe.dbg_log('ace::load_values', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::load_values', 'ERROR: (%s)' % repr(e))

    def initialize_acestream(self, **kwargs):
        try:
            self.oe.dbg_log('ace::initialize_acestream', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 0
            if self.struct['acestream']['settings']['enable_acestream']['value'] == '1':

                if not os.path.exists('/storage/.config/acestream/installed.acestream'):
                    ace_status = self.get_ace_source()
                    if ace_status == 'OK':
                        self.oe.notify(self.oe._(32363), 'Run AceStream engine...')
                    else:
                        self.struct['acestream']['settings']['enable_acestream']['value'] = '0'
                        self.oe.set_busy(0)
                        xbmcDialog = xbmcgui.Dialog()
                        answer = xbmcDialog.ok('Install AceStream',
                            'Error: The program is not installed, try again.')
                        return

                options['ACE_DEBUG'] = '"%s"' % self.struct['acestream']['settings']['ace_debug']['value']
                state = 1

            self.oe.set_service('acestream', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('ace::initialize_acestream', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('ace::initialize_acestream', 'ERROR: (%s)' % repr(e), 4)

    def get_ace_source(self, listItem=None, silent=False):
        try:
            self.oe.dbg_log('ace::get_ace_source', 'enter_function', 0)
            ace_url = self.oe.execute(self.ACE_GET_SRC + ' url', 1).strip()
            self.download_file = ace_url
            self.oe.set_busy(0)
            if hasattr(self, 'download_file'):
                downloaded = self.oe.download_file(self.download_file, self.oe.TEMP + self.download_file.split('/')[-1], silent)
                if not downloaded is None:
                    self.oe.notify(self.oe._(32363), 'Unpack AceStream...')
                    self.oe.set_busy(1)
                    self.oe.execute(self.ACE_GET_SRC + ' unpack', 0)
                    self.oe.dbg_log('ace::get_ace_source', 'exit_function', 0)
                    return 'OK'
            self.oe.dbg_log('ace::get_ace_source', 'exit_function', 0)
            return 'ERROR'
        except Exception, e:
            self.oe.dbg_log('ace::get_ace_source', 'ERROR: (%s)' % repr(e), 4)

    def initialize_torrserver(self, **kwargs):
        try:
            self.oe.dbg_log('ace::initialize_torrserver', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 0
            if self.struct['torrserver']['settings']['enable_torrserver']['value'] == '1':

                if not os.path.exists('/storage/.config/torrserver/bin/TorrServer'):
                    torrsrv_status = self.get_torrsrv_source()
                    if torrsrv_status == 'OK':
                        self.oe.notify(self.oe._(32363), 'Run TorrServer daemon...')
                    else:
                        self.struct['torrserver']['settings']['enable_torrserver']['value'] = '0'
                        self.oe.set_busy(0)
                        xbmcDialog = xbmcgui.Dialog()
                        answer = xbmcDialog.ok('Install TorrServer',
                            'Error: The program is not installed, try again.')
                        return

                options['TORRSRV_DEBUG'] = '"%s"' % self.struct['torrserver']['settings']['torrsrv_debug']['value']
                options['TORRSRV_PORT'] = '"%s"' % self.struct['torrserver']['settings']['torrsrv_port']['value']
                state = 1

            self.oe.set_service('torrserver', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('ace::initialize_torrserver', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('ace::initialize_torrserver', 'ERROR: (%s)' % repr(e), 4)

    def get_torrsrv_source(self, listItem=None, silent=False):
        try:
            self.oe.dbg_log('ace::get_torrsrv_source', 'enter_function', 0)
            torrsrv_url = self.oe.execute(self.TORRSRV_GET_SRC + ' url', 1).strip()
            self.download_file = torrsrv_url
            self.oe.set_busy(0)
            if hasattr(self, 'download_file'):
                downloaded = self.oe.download_file(self.download_file, self.oe.TEMP + self.download_file.split('/')[-1], silent)
                if not downloaded is None:
                    self.oe.notify(self.oe._(32363), 'Install TorrServer...')
                    self.oe.set_busy(1)
                    self.oe.execute(self.TORRSRV_GET_SRC + ' install', 0)
                    self.oe.dbg_log('ace::get_torrsrv_source', 'exit_function', 0)
                    return 'OK'
            self.oe.dbg_log('ace::get_torrsrv_source', 'exit_function', 0)
            return 'ERROR'
        except Exception, e:
            self.oe.dbg_log('ace::get_torrsrv_source', 'ERROR: (%s)' % repr(e), 4)

    def initialize_ptv(self, **kwargs):
        try:
            self.oe.dbg_log('ace::initialize_ptv', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 0
            if self.struct['ptv']['settings']['enable_ptv']['value'] == '1':

                if not os.path.exists('/storage/.config/ptv3/server.py'):
                    ptv_status = self.get_ptv_source()
                    if ptv_status == 'OK':
                        self.oe.notify(self.oe._(32363), 'Run Puzzle-TV IPTV aggregator...')
                    else:
                        self.struct['ptv']['settings']['enable_ptv']['value'] = '0'
                        self.oe.set_busy(0)
                        xbmcDialog = xbmcgui.Dialog()
                        answer = xbmcDialog.ok('Install Puzzle-TV',
                            'Error: The program is not installed, try again.')
                        return

                state = 1

            self.oe.set_service('ptv', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('ace::initialize_ptv', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('ace::initialize_ptv', 'ERROR: (%s)' % repr(e), 4)

    def get_ptv_source(self, listItem=None, silent=False):
        try:
            self.oe.dbg_log('ace::get_ptv_source', 'enter_function', 0)
            ptv_url = self.oe.execute(self.PAZL_GET_SRC + ' url', 1).strip()
            self.download_file = ptv_url
            self.oe.set_busy(0)
            if hasattr(self, 'download_file'):
                downloaded = self.oe.download_file(self.download_file, self.oe.TEMP + self.download_file.split('/')[-1], silent)
                if not downloaded is None:
                    self.oe.notify(self.oe._(32363), 'Install Puzzle-TV IPTV aggregator...')
                    self.oe.set_busy(1)
                    self.oe.execute(self.PAZL_GET_SRC + ' install', 0)
                    self.oe.set_busy(0)
                    self.oe.dbg_log('ace::get_ptv_source', 'exit_function', 0)
                    return 'OK'
            self.oe.dbg_log('ace::get_ptv_source', 'exit_function', 0)
            return 'ERROR'
        except Exception, e:
            self.oe.dbg_log('ace::get_ptv_source', 'ERROR: (%s)' % repr(e), 4)

    def update_ptv(self, listItem=None):
        try:
            self.oe.dbg_log('ace::update_ptv', 'enter_function', 0)
            if os.path.exists('/storage/.config/ptv3/latest'):
                self.oe.notify(self.oe._(32363), 'Check new version...')
                self.oe.set_busy(1)
                ver_update = self.oe.execute(self.PAZL_GET_SRC + ' new', 1).strip()
                self.oe.set_busy(0)
                if not ver_update == 'NOT UPDATE':
                    self.oe.set_busy(1)
                    ver_current = self.oe.execute(self.PAZL_GET_SRC + ' old', 1).strip()
                    self.oe.set_busy(0)
                    dialog = xbmcgui.Dialog()
                    ret = dialog.yesno('Update Puzzle-TV?', ' ', 'Current version:  %s' % ver_current,
                                                                 'Update  version:  %s' % ver_update)
                    if ret:
                        self.oe.set_busy(1)
                        self.oe.execute('systemctl stop ptv.service', 0)
                        self.oe.execute(self.PAZL_GET_SRC + ' backup', 0)
                        ptv_status = self.get_ptv_source()
                        self.oe.set_busy(0)
                        if ptv_status == 'OK':
                            self.oe.notify(self.oe._(32363), 'Run Puzzle-TV version: %s ...' % ver_update)
                        else:
                            self.oe.notify(self.oe._(32363), 'Updates is not installed, try again.')
                        self.oe.execute(self.PAZL_GET_SRC + ' restore', 0)
                        self.oe.execute('systemctl start ptv.service', 0)
                else:
                    self.oe.notify(self.oe._(32363), 'No updates available.')

        except Exception, e:
            self.oe.dbg_log('ace::update_ptv', 'ERROR: (' + repr(e) + ')')

    def clean_ptv(self, listItem=None):
        try:
            self.oe.dbg_log('ace::clean_ptv', 'enter_function', 0)
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Clean channel database?', ' ',
                               'This completely cleanse channels and settings!')
            if ret:
                self.oe.set_busy(1)
                self.oe.execute('systemctl stop ptv.service', 0)
                self.oe.execute(self.PAZL_GET_SRC + ' clean', 0)
                self.oe.execute('systemctl start ptv.service', 0)
                self.oe.set_busy(0)
                self.oe.notify(self.oe._(32363), 'Puzzle-TV channel database cleared.')

        except Exception, e:
            self.oe.dbg_log('ace::clean_ptv', 'ERROR: (' + repr(e) + ')')

    def exit(self):
        try:
            self.oe.dbg_log('ace::exit', 'enter_function', 0)
            self.oe.dbg_log('ace::exit', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('ace::exit', 'ERROR: (%s)' % repr(e), 4)
