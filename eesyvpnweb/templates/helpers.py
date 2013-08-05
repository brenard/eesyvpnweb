# -*- coding: utf-8 -*-


import os
import random
import datetime


def random_sequence(length):
    return [random.random() for idx in xrange(0, length)]


def relative_path(ctx, abs_path):
    return os.path.relpath(abs_path, ctx.req.path)

def expire_date(date):
	if date > datetime.datetime.now() and date < datetime.datetime.now()-datetime.timedelta(days=30):
		return '<span class="badge badge-warning">%s</span>' % date
	else:
		return '<span class="badge badge-info">%s</span>' % date
