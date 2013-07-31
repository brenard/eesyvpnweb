#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""EesyVPN web application."""


from setuptools import setup, find_packages


doc_lines = __doc__.split('\n')


setup(
    author=u'Benjamin Renard',
    author_email=u'brenard@zionetrix.net',
    description=doc_lines[0],
    entry_points="""
        [paste.app_factory]
        main = eesyvpnweb.application:make_app
        """,
    include_package_data=True,
    install_requires=[
        'Biryani1 >= 0.9dev',
        'MarkupSafe >= 0.15',
        'WebError >= 0.10',
        'WebHelpers >= 1.3',
        'WebOb >= 1.1',
        ],
#    keywords='',
#    license=u'http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    long_description='\n'.join(doc_lines[2:]),
    name=u'EesyVPNWeb',
    packages=find_packages(),
    paster_plugins=['PasteScript'],
    setup_requires=['PasteScript >= 1.6.3'],
#    url=u'',
    version='0.1',
    zip_safe=False,
    )
