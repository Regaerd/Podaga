#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
from ast import literal_eval
try:    from ConfigParser import RawConfigParser
except: from configparser import RawConfigParser

class ArgConfParser(ArgumentParser):
    kCONFIG_EXTENSION = '.conf'
    kCONFIG_SECTION = 'Settings'
    kCONFIG_HEADER = '[{}]\n'.format(kCONFIG_SECTION)
    kARG_SAVE_SHORT, kARG_SAVE_LONG, kKEY_SAVE = ('-s', '--save-config', 'save_config')

    def __init__(self, can_save=True, prog=None, description=None):
        super(ArgConfParser, self).__init__(prog=prog, description=description)
        self.can_save = can_save
        if can_save:
            self.add_argument(self.kARG_SAVE_SHORT, self.kARG_SAVE_LONG, action='store_true', default=False, help='save settings to config file', dest=self.kKEY_SAVE)

    def parse_args(self, args=None, namespace=None):
        # config file detection
        config_bases = [os.path.expanduser('~/.')]
        try: from xdg.BaseDirectory import xdg_config_home; config_bases.append(xdg_config_home+'/')
        except: config_bases.append(os.environ.get('XDG_CONFIG_HOME') if os.environ.get('XDG_CONFIG_HOME', None) else os.path.expanduser('~/.config/'))
        config_file = '{}{}'.format(self.prog.lower(), self.kCONFIG_EXTENSION)
        possible_configs = [dir + config_file for dir in [item for base in config_bases for item in [base, '{}{}/'.format(base,self.prog)]]]
        possible_configs.append("{}/{}".format(os.path.dirname(os.path.realpath(__file__)), config_file))

        # config parsing
        config = RawConfigParser()
        found_config = config.read(possible_configs)
        settings = dict(config.items(self.kCONFIG_SECTION)) if config.has_section(self.kCONFIG_SECTION) else {}
        for i, item in settings.items(): settings[i] = literal_eval(item) # fix values that might not be stored correctly (i.e bools)
        self.set_defaults(**settings)
        parsed_args = super(ArgConfParser, self).parse_args(args=args, namespace=namespace)

        # save config file
        if self.can_save and parsed_args.save_config:
            dict_args = vars(parsed_args)
            del dict_args[self.kKEY_SAVE] # don't want this one saved

            with open(found_config[0] if found_config else possible_configs[0] ,"w") as f:
                f.write(self.kCONFIG_HEADER+'\n'.join(['%s = \'%s\'' % (key, value) for (key, value) in dict_args.items()]))

        return parsed_args
