from random import choice, randint
import sys
import logging
import re
from setuptools import setup

PY2 = False

if sys.version_info < (3, 0):
    PY2 = True


_log = logging.getLogger(__name__)


def get_py2(url):
    import urllib2

    return urllib2.urlopen(url)


def get_py3(url):
    from urllib.request import urlopen

    return urlopen(url)


def get_packages(url):
    if PY2:
        res = get_py2(url)
    else:
        res = get_py3(url)

    packages = []

    pkg_re = re.compile(r'<a href=\'([^\']*)\'')

    for line in res.readlines():
        if not PY2:
            line = line.decode('utf8')

        _log.debug('line: %s', line)

        matches = pkg_re.search(line)

        if matches:
            packages.append(matches.group(1))

    _log.debug('packages: %s', packages)

    return packages


def get_deps():
    _log.info('Getting possible dependencies. This may take a while if you '
              'are on a hotel wifi.')
    packages = get_packages('https://pypi.python.org/simple/')

    deps = []

    for i in range(1, randint(2, 6)):
        deps.append(choice(packages))

    return deps


def main(argv=None):
    deps = get_deps()
    _log.info('You got \n%s\nas dependencies. Good luck!', '\n- '.join(deps))

    setup(
        name='deproulette',
        version='0.1',
        author='Joar Wandborg',
        author_email='joar\\x40wandborg.se',
        description='You never know what you get. Such is life.',
        install_requires=deps
    )


if __name__ == '__main__':
    import os
    logging.basicConfig(level=getattr(logging,
                                      os.environ.get('LOGLEVEL', 'INFO')))
    sys.exit(main(sys.argv))