# This is the setup file for pip
from setuptools import setup, find_packages
import os
import sys
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst')) as f:
    description_file = f.read()

setup(
    name = 'JARVIS',

    version = '1.0.0',

    description = 'An intelligent assistant for making your life easy',
    long_description = description_file,

    url = 'https://github.com/DarkmatterVale/JARVIS',

    author = 'Vale Tolpegin',
    author_email = 'valetolpegin@gmail.com',

    license = 'MIT',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',

        'License :: OSI Approved :: MIT License',

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",

        "Operating System :: OS Independent",
    ],

    packages = find_packages(),

    platforms=["any"],
    install_requires = ['ChatterBot'],

    keywords = [ 'NLP', 'assistant', 'intelligent', 'AI' ],
)
