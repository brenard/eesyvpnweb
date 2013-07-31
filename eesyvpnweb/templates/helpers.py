# -*- coding: utf-8 -*-


import os
import random


def random_sequence(length):
    return [random.random() for idx in xrange(0, length)]


def relative_path(ctx, abs_path):
    return os.path.relpath(abs_path, ctx.req.path)
