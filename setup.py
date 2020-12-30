import os
import re
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Utility function to read version
def get_version():
    fname = 'src/binance/version.py'
    version_regex = "__version__ = (?P<version>.*)"
    string = read(fname)
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
    url = "https://git.villebros.com/rvillebro/binance",
    package_dir = {'': 'src'},
    packages = find_packages("src", exclude=['*tests*']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)