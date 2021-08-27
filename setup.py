#!/usr/bin/env python3
import re
import pathlib

from setuptools import setup, find_packages

# Utility function to read version
def get_version():
    fname = 'src/binance/version.py'
    string = pathlib.Path(fname).read_text()
    version_regex = "__version__ = (?P<version>.*)"
    match = re.search(version_regex, string)
    version = match.group('version')

    if version:
        return version
    else:
        raise ValueError('Version not found!')

setup(
    name = "binance",
    version = get_version(),
    author = "Rasmus Villebro",
    author_email = "rasmus-villebro@hotmail.com",
    description = 'A binance asynchronious API package',
    license = "MIT",
    keywords = "binance api",
    url = "https://github.com/rvillebro/binance",
    package_dir = {'': 'src'},
    packages = find_packages("src", exclude=['*tests*']),
    long_description=pathlib.Path('README.md').read_text(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)