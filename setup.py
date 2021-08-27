#!/usr/bin/env python3
import re
import pathlib

from setuptools import setup, find_packages


def get_version():
    """
    Utility function to read version
    """
    filepath = 'src/binance/version.py'
    string = pathlib.Path(filepath).read_text()
    version_regex = r'__version__ = "(?P<version>.*)"'
    match = re.search(version_regex, string)
    version = match.group('version')

    if version:
        return version
    else:
        raise ValueError('Version not found!')


def get_requirements():
    """
    Utility function to read requirements
    """
    filepath = 'requirements.txt'
    string = pathlib.Path(filepath).read_text()
    requirements_list = string.split('\n')
    return requirements_list


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
    install_requires=get_requirements(),
)