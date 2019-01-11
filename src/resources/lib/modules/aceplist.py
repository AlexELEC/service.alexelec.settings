# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright (C) 2011-present AlexELEC (http://alexelec.in.ua)

import os
import glob
import xbmc
import xbmcgui

class aceplist:

    ENABLED=False

    D_CAT_SHOW = None
    D_CAT_COMM = None
    D_CAT_FILMS = None
    D_CAT_EROS = None
    D_CAT_NEWS = None
    D_CAT_REGION = None
    D_CAT_MUSIC = None
    D_CAT_CHILDREN = None
    D_CAT_SPORT = None
    D_CAT_RELIGION = None
    D_CAT_MAN = None
    D_CAT_LEARN = None
    D_CAT_ALLFON = None
    D_ACETTV_IP = None
    D_TTV_LOGIN = None
    D_TTV_PASSW = None
    D_TRANSLATE = None
    D_ACETTV_UPD = None
    TTV_DEL_LIST = None
    TTV_RUN_LIST = None

    menu = {'92': {
        'name': 34050,
        'menuLoader': 'load_menu',
        'listTyp': 'list',
        'InfoText': 3450,
        }}

    def __init__(self, oeMain):
        try:
            oeMain.dbg_log('aceplist::__init__', 'enter_function', 0)
            self.struct = {
                'acettv': {
                    'order': 1,
                    'name': 34051,
                    'not_supported': [],
                    'settings': {
                        'cat_show': {
                            'order': 1,
                            'name': 'Развлекательные',
                            'value': '1',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_comm': {
                            'order': 2,
                            'name': 'Общие',
                            'value': '1',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_films': {
                            'order': 3,
                            'name': 'Фильмы',
                            'value': '1',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_eros': {
                            'order': 4,
                            'name': 'Эротика',
                            'value': '1',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_news': {
                            'order': 5,
                            'name': 'Новостные',
                            'value': '1',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_region': {
                            'order': 6,
                            'name': 'Региональные',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_music': {
                            'order': 7,
                            'name': 'Музыка',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_children': {
                            'order': 8,
                            'name': 'Детские',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_sport': {
                            'order': 9,
                            'name': 'Спорт',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_religion': {
                            'order': 10,
                            'name': 'Религиозные',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_man': {
                            'order': 11,
                            'name': 'Мужские',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_learn': {
                            'order': 12,
                            'name': 'Познавательные',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        'cat_allfon': {
                            'order': 13,
                            'name': 'Allfon',
                            'value': '0',
                            'action': 'initialize_acettv',
                            'type': 'bool',
                            'InfoText': 3451,
                            },
                        },
                    },
                'acerun': {
                    'order': 2,
                    'name': 34060,
                    'not_supported': [],
                    'settings': {
                        'acettv_ip': {
                            'order': 1,
                            'name': 34061,
                            'value': '0',
                            'action': 'initialize_acerun',
                            'type': 'bool',
                            'InfoText': 3461,
                            },
                        'ttv_login': {
                            'order': 2,
                            'name': 34064,
                            'value': None,
                            'action': 'initialize_acerun',
                            'type': 'text',
                            'InfoText': 3464,
                            },
                        'ttv_passw': {
                            'order': 3,
                            'name': 34065,
                            'value': None,
                            'action': 'initialize_acerun',
                            'type': 'text',
                            'InfoText': 3465,
                            },
                        'translate': {
                            'order': 5,
                            'name': 34066,
                            'value': 'Trash-TTV',
                            'values': ['Trash-All', 'Trash-Ace', 'Trash-TTV', 'Site-TTV'],
                            'action': 'initialize_acerun',
                            'type': 'multivalue',
                            'InfoText': 3466,
                            },
                        'acettv_upd': {
                            'order': 6,
                            'name': 34067,
                            'value': '0',
                            'action': 'initialize_acerun',
                            'type': 'bool',
                            'InfoText': 3467,
                            },
                        'acettv_run': {
                            'order': 7,
                            'name': 34063,
                            'value': '0',
                            'action': 'execute_acettv',
                            'type': 'button',
                            'InfoText': 3463,
                            },
                        },
                    },
            }

            self.oe = oeMain
            oeMain.dbg_log('aceplist::__init__', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::__init__', 'ERROR: (%s)' % repr(e))

    def start_service(self):
        try:
            self.oe.dbg_log('aceplist::start_service', 'enter_function', 0)
            self.load_values()
            self.initialize_acettv_onerun()
            self.initialize_acerun()
            self.oe.dbg_log('aceplist::start_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::start_service', 'ERROR: (%s)' % repr(e))

    def stop_service(self):
        try:
            self.oe.dbg_log('aceplist::stop_service', 'enter_function', 0)
            self.oe.dbg_log('aceplist::stop_service', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::stop_service', 'ERROR: (' + repr(e) + ')')

    def do_init(self):
        try:
            self.oe.dbg_log('aceplist::do_init', 'exit_function', 0)
            self.load_values()
            self.oe.dbg_log('aceplist::do_init', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::do_init', 'ERROR: (%s)' % repr(e))

    def set_value(self, listItem):
        try:
            self.oe.dbg_log('aceplist::set_value', 'enter_function', 0)
            self.struct[listItem.getProperty('category')]['settings'][listItem.getProperty('entry')]['value'] = listItem.getProperty('value')
            self.oe.dbg_log('aceplist::set_value', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::set_value', 'ERROR: (' + repr(e) + ')')

    def load_menu(self, focusItem):
        try:
            self.oe.dbg_log('aceplist::load_menu', 'enter_function', 0)
            self.oe.winOeMain.build_menu(self.struct)
            self.oe.dbg_log('aceplist::load_menu', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::load_menu', 'ERROR: (%s)' % repr(e))

    def load_values(self):
        try:
            self.oe.dbg_log('aceplist::load_values', 'enter_function', 0)

            # TTV-LIST
            self.struct['acettv']['settings']['cat_show']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_SHOW', self.D_CAT_SHOW).replace('"', '')

            self.struct['acettv']['settings']['cat_comm']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_COMM', self.D_CAT_COMM).replace('"', '')

            self.struct['acettv']['settings']['cat_films']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_FILMS', self.D_CAT_FILMS).replace('"', '')

            self.struct['acettv']['settings']['cat_eros']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_EROS', self.D_CAT_EROS).replace('"', '')

            self.struct['acettv']['settings']['cat_news']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_NEWS', self.D_CAT_NEWS).replace('"', '')

            self.struct['acettv']['settings']['cat_region']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_REGION', self.D_CAT_REGION).replace('"', '')

            self.struct['acettv']['settings']['cat_music']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_MUSIC', self.D_CAT_MUSIC).replace('"', '')

            self.struct['acettv']['settings']['cat_children']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_CHILDREN', self.D_CAT_CHILDREN).replace('"', '')

            self.struct['acettv']['settings']['cat_sport']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_SPORT', self.D_CAT_SPORT).replace('"', '')

            self.struct['acettv']['settings']['cat_religion']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_RELIGION', self.D_CAT_RELIGION).replace('"', '')

            self.struct['acettv']['settings']['cat_man']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_MAN', self.D_CAT_MAN).replace('"', '')

            self.struct['acettv']['settings']['cat_learn']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_LEARN', self.D_CAT_LEARN).replace('"', '')

            self.struct['acettv']['settings']['cat_allfon']['value'] = \
            self.oe.get_service_option('acettv', 'CAT_ALLFON', self.D_CAT_ALLFON).replace('"', '')

            # TTV-LIST Create
            self.struct['acerun']['settings']['ttv_login']['value'] = \
            self.oe.get_service_option('acerun', 'TTV_LOGIN', self.D_TTV_LOGIN).replace('"', '')

            self.struct['acerun']['settings']['ttv_passw']['value'] = \
            self.oe.get_service_option('acerun', 'TTV_PASSW', self.D_TTV_PASSW).replace('"', '')

            self.struct['acerun']['settings']['acettv_ip']['value'] = \
            self.oe.get_service_option('acerun', 'ACETTV_IP', self.D_ACETTV_IP).replace('"', '')

            self.struct['acerun']['settings']['translate']['value'] = \
            self.oe.get_service_option('acerun', 'TRANSLATE', self.D_TRANSLATE).replace('"', '')

            self.struct['acerun']['settings']['acettv_upd']['value'] = \
            self.oe.get_service_option('acerun', 'ACETTV_UPD', self.D_ACETTV_UPD).replace('"', '')

            self.oe.dbg_log('aceplist::load_values', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::load_values', 'ERROR: (%s)' % repr(e))

    def initialize_acettv_onerun(self, **kwargs):
        try:
            self.oe.dbg_log('aceplist::initialize_acettv_onerun', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 1
            options['CAT_SHOW'] = '"%s"' % self.struct['acettv']['settings']['cat_show']['value']
            options['CAT_COMM'] = '"%s"' % self.struct['acettv']['settings']['cat_comm']['value']
            options['CAT_FILMS'] = '"%s"' % self.struct['acettv']['settings']['cat_films']['value']
            options['CAT_EROS'] = '"%s"' % self.struct['acettv']['settings']['cat_eros']['value']
            options['CAT_NEWS'] = '"%s"' % self.struct['acettv']['settings']['cat_news']['value']
            options['CAT_REGION'] = '"%s"' % self.struct['acettv']['settings']['cat_region']['value']
            options['CAT_MUSIC'] = '"%s"' % self.struct['acettv']['settings']['cat_music']['value']
            options['CAT_CHILDREN'] = '"%s"' % self.struct['acettv']['settings']['cat_children']['value']
            options['CAT_SPORT'] = '"%s"' % self.struct['acettv']['settings']['cat_sport']['value']
            options['CAT_RELIGION'] = '"%s"' % self.struct['acettv']['settings']['cat_religion']['value']
            options['CAT_MAN'] = '"%s"' % self.struct['acettv']['settings']['cat_man']['value']
            options['CAT_LEARN'] = '"%s"' % self.struct['acettv']['settings']['cat_learn']['value']
            options['CAT_ALLFON'] = '"%s"' % self.struct['acettv']['settings']['cat_allfon']['value']
            self.oe.set_service('acettv', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('aceplist::initialize_acettv_onerun', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('aceplist::initialize_acettv_onerun', 'ERROR: (%s)' % repr(e), 4)

    def initialize_acettv(self, **kwargs):
        try:
            self.oe.dbg_log('aceplist::initialize_acettv', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 1
            options['CAT_SHOW'] = '"%s"' % self.struct['acettv']['settings']['cat_show']['value']
            options['CAT_COMM'] = '"%s"' % self.struct['acettv']['settings']['cat_comm']['value']
            options['CAT_FILMS'] = '"%s"' % self.struct['acettv']['settings']['cat_films']['value']
            options['CAT_EROS'] = '"%s"' % self.struct['acettv']['settings']['cat_eros']['value']
            options['CAT_NEWS'] = '"%s"' % self.struct['acettv']['settings']['cat_news']['value']
            options['CAT_REGION'] = '"%s"' % self.struct['acettv']['settings']['cat_region']['value']
            options['CAT_MUSIC'] = '"%s"' % self.struct['acettv']['settings']['cat_music']['value']
            options['CAT_CHILDREN'] = '"%s"' % self.struct['acettv']['settings']['cat_children']['value']
            options['CAT_SPORT'] = '"%s"' % self.struct['acettv']['settings']['cat_sport']['value']
            options['CAT_RELIGION'] = '"%s"' % self.struct['acettv']['settings']['cat_religion']['value']
            options['CAT_MAN'] = '"%s"' % self.struct['acettv']['settings']['cat_man']['value']
            options['CAT_LEARN'] = '"%s"' % self.struct['acettv']['settings']['cat_learn']['value']
            options['CAT_ALLFON'] = '"%s"' % self.struct['acettv']['settings']['cat_allfon']['value']
            self.oe.set_service('acettv', options, state)
            self.oe.execute(self.TTV_DEL_LIST, 0)
            self.oe.set_busy(0)
            self.oe.dbg_log('aceplist::initialize_acettv', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('aceplist::initialize_acettv', 'ERROR: (%s)' % repr(e), 4)

    def initialize_acerun(self, **kwargs):
        try:
            self.oe.dbg_log('aceplist::initialize_acerun', 'enter_function', 0)
            self.oe.set_busy(1)
            if 'listItem' in kwargs:
                self.set_value(kwargs['listItem'])
            options = {}
            state = 1
            options['ACETTV_IP'] = '"%s"' % self.struct['acerun']['settings']['acettv_ip']['value']
            options['TTV_LOGIN'] = '"%s"' % self.struct['acerun']['settings']['ttv_login']['value']
            options['TTV_PASSW'] = '"%s"' % self.struct['acerun']['settings']['ttv_passw']['value']
            options['TRANSLATE'] = '"%s"' % self.struct['acerun']['settings']['translate']['value']
            options['ACETTV_UPD'] = '"%s"' % self.struct['acerun']['settings']['acettv_upd']['value']
            self.oe.set_service('acerun', options, state)
            self.oe.set_busy(0)
            self.oe.dbg_log('aceplist::initialize_acerun', 'exit_function', 0)
        except Exception, e:
            self.oe.set_busy(0)
            self.oe.dbg_log('aceplist::initialize_acerun', 'ERROR: (%s)' % repr(e), 4)

    def execute_acettv(self, listItem=None):
        try:
            self.oe.dbg_log('aceplist::execute_acettv', 'enter_function', 0)
            if os.path.exists(self.TTV_RUN_LIST):
                self.oe.notify(self.oe._(32363), 'Create TTV playlist...')
                self.oe.set_busy(1)
                message = self.oe.execute(self.TTV_RUN_LIST, 1).strip()
                self.oe.set_busy(0)
                if message == 'Done! Playlist created.':
                    dialog = xbmcgui.Dialog()
                    ret = dialog.yesno('TTV playlist', 'Playlist created. Restart Kodi?')
                    if ret:
                        xbmc.executebuiltin('RestartApp')
                else:
                    dialog = xbmcgui.Dialog()
                    dialog.notification('TTV playlist',
                                        '%s' % message,
                                        xbmcgui.NOTIFICATION_INFO, 3000)
        except Exception, e:
            self.oe.dbg_log('aceplist::execute_acettv', 'ERROR: (' + repr(e) + ')')

    def exit(self):
        try:
            self.oe.dbg_log('aceplist::exit', 'enter_function', 0)
            self.oe.dbg_log('aceplist::exit', 'exit_function', 0)
        except Exception, e:
            self.oe.dbg_log('aceplist::exit', 'ERROR: (%s)' % repr(e), 4)
