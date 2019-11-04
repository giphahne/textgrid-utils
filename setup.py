from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='textgrid_utils',
    version='1.0.0',
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
    install_requires=['argcomplete'],
    package_data={
        '': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'merge-and-mark-textgrid-tiers=textgrid_utils:merge_main',
        ],
    },
)
