#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
# from  dpdispatcher import NAME,SHORT_CMD
import setuptools, datetime

today = datetime.date.today().strftime("%b-%d-%Y")
# with open(path.join(NAME, '_date.py'), 'w') as fp :
#     fp.write('date = \'%s\'' % today)

install_requires=['apache-airflow>2.0']

setuptools.setup(
    name='deepti',
    use_scm_version={'write_to': 'deepti/_version.py'},
    setup_requires=['setuptools_scm'],
    author="Deep Modeling Team",
    author_email="",
    description="Python deepti for thermodynamics integration",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    python_requires=">3.7",
    packages=['deepti'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    ],
    keywords='free energy thermodynamics integration deepmd-kit',
    install_requires=install_requires,    
    # extras_require={
    #     'docs': ['sphinx', 'recommonmark', 'sphinx_rtd_theme'],
    # },
        entry_points={
        #   'console_scripts': [
        #       SHORT_CMD+'= dpdispatcher.dpdisp:main']
    }
)
