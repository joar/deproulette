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

    _log.info('You got \n- %s\nas dependenc(y|ies). Good luck!',
              '\n- '.join(deps))

    return deps


def main(argv=None):
    if argv and (len(argv) == 0 or argv[1] in ['egg_info']):
        deps = get_deps()
    else:
        deps = None

    setup(
        name='deproulette',
        version='1.0.1',
        author='Joar Wandborg',
        author_email='name \\x40 lastname. se',
        url='https://github.com/joar/deproulette',
        description='You never know what you get. Such is life.',
        long_description=open('README.rst').read(),
        install_requires=deps
    )


if __name__ == '__main__':
    import os

    _log.setLevel(getattr(logging, os.environ.get('LOGLEVEL', 'INFO')))

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    def decorate_emit(fn):
    # add methods we need to the class
        def new(*args):
            levelno = args[0].levelno
            if levelno >= logging.CRITICAL:
                color = '\x1b[31;1m'
            elif levelno >= logging.ERROR:
                color = '\x1b[31;1m'
            elif levelno >= logging.WARNING:
                color = '\x1b[33;1m'
            elif levelno >= logging.INFO:
                color = '\x1b[32;1m'
            elif levelno >= logging.DEBUG:
                color = '\x1b[35;1m'
            else:
                color = '\x1b[0m'

            # add colored *** in the beginning of the message
            args[0].msg = "{0}***\x1b[0m {1}".format(color, args[0].msg)

            # new feature i like: bolder each args of message
            args[0].args = tuple('\x1b[1m' + arg + '\x1b[0m' for arg in args[0].args)
            return fn(*args)
        return new

    handler.emit = decorate_emit(handler.emit)

    _log.addHandler(handler)

    sys.exit(main(sys.argv))