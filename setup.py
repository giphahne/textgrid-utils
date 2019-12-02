from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='textgrid_utils',
    version='2.0.0',
    description='utilities for working with textgrid files',
    url='https://github.com/giphahne/textgrid-utils',
    author='Dan Hahne',
    author_email='contact@danhahne.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='linguistics textgrid praat',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['argcomplete', 'textgrid'],
    package_data={
        '': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'tg-add-type-tier=textgrid_utils:add_type_tier_main',
            'tg-add-merged-tier=textgrid_utils:add_merged_tier_main',
            'tg-copy-tiers=textgrid_utils:copy_tiers_main',
            'tg-remove-tiers=textgrid_utils:remove_tiers_main',
            'tg-list-tiers=textgrid_utils:list_main',
            'tg-rename-tier=textgrid_utils:rename_tier_main',
        ],
    },
)
