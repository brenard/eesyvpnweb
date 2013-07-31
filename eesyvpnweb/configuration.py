# -*- coding: utf-8 -*-


"""Paste INI configuration"""


import os

from biryani1 import strings
from biryani1.baseconv import (check, default, guess_bool, pipe, struct)


def load_configuration(global_conf, app_conf):
    """Build the application configuration dict."""
    app_dir = os.path.dirname(os.path.abspath(__file__))
    conf = {}
    conf.update(strings.deep_decode(global_conf))
    conf.update(strings.deep_decode(app_conf))
    conf.update(check(struct(
        {
            'app_conf': default(app_conf),
            'app_dir': default(app_dir),
            'cache_dir': default(os.path.join(os.path.dirname(app_dir), 'cache')),
            'debug': pipe(guess_bool, default(False)),
            'global_conf': default(global_conf),
            },
        default='drop',
        drop_none_values=False,
        ))(conf))
    return conf
