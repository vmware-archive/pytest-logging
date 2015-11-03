# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2015 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.


    pytest_logging.plugin
    ~~~~~~~~~~~~~~~~~~~~~
'''

# Import python libs
from __future__ import absolute_import
import sys
import logging

# Import py libs
import py

if not hasattr(logging, 'TRACE'):
    logging.TRACE = 5
    logging.addLevelName(logging.TRACE, 'TRACE')
if not hasattr(logging, 'GARBAGE'):
    logging.GARBAGE = 1
    logging.addLevelName(logging.GARBAGE, 'GARBAGE')

LOG_FORMAT = '%(asctime)s,%(msecs)04.0f [%(name)-5s:%(lineno)-4d][%(levelname)-8s] %(message)s'
DATE_FORMAT = '%H:%M:%S'

HANDLED_LEVELS = {
    2: logging.WARN,    # -v
    3: logging.INFO,    # -vv
    4: logging.DEBUG,   # -vvv
    5: logging.TRACE,   # -vvvv
    6: logging.GARBAGE  # -vvvvv
}

TERMINAL = py.io.TerminalWriter(sys.stderr)  # pylint: disable=no-member
CONSOLEHANDLER = logging.StreamHandler(TERMINAL)
# Add the handler to logging
logging.root.addHandler(CONSOLEHANDLER)
# The root logging should have the lowest logging level to allow all messages
# to be logged
logging.root.setLevel(logging.GARBAGE)


def pytest_addoption(parser):
    '''
    Add CLI options to py.test
    '''
    group = parser.getgroup('logging', 'Logging Configuration')
    if parser.getgroup('capturelog', description='Nah!').description == 'Nah!':
        # We don't have capture log installed, let's add our format flags
        group.addoption('--log-format',
                        dest='log_format',
                        default=LOG_FORMAT,
                        help='log format as used by the logging module')
        group.addoption('--log-date-format',
                        dest='log_date_format',
                        default=DATE_FORMAT,
                        help='log date format as used by the logging module')

    parser.addini('log_format',
                  'log format as used by the logging module')
    parser.addini('log_date_format',
                  'log date format as used by the logging module')


def pytest_configure(config):
    '''
    Add the formatter to logging
    '''
    # Get the format options and add the formatter to the console handler
    formatter = logging.Formatter(
        config.getini('log_format') or config.getvalue('log_format'),
        config.getini('log_date_format') or config.getvalue('log_date_format'))
    CONSOLEHANDLER.setFormatter(formatter)


def pytest_cmdline_main(config):
    '''
    called for performing the main command line action. The default
    implementation will invoke the configure hooks and runtest_mainloop.
    '''
    verbosity = config.getoption('-v')
    if verbosity > 1:
        CONSOLEHANDLER.setLevel(
            HANDLED_LEVELS.get(verbosity,
                               HANDLED_LEVELS.get(verbosity > 6 and 6 or 2)))
    else:
        # The console handler defaults to the highest logging level
        CONSOLEHANDLER.setLevel(logging.FATAL)
    print(999, verbosity, CONSOLEHANDLER.level)
