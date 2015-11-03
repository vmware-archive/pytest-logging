# -*- coding: utf-8 -*-


def _test_bar_fixture(testdir):
    '''Make sure that pytest accepts our fixture.'''

    # create a temporary pytest test module
    testdir.makepyfile('''
        def test_sth(bar):
            assert bar == 'europython2015'
    ''')

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--foo=europython2015',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_sth PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'Logging Configuration:',
    ])


def test_log_format_ini_setting(testdir):
    testdir.makeini('''
        [pytest]
        log_format = %(asctime)s,%(msecs)03.0f [%(name)-5s:%(lineno)-4d][%(levelname)-8s] %(message)s
    ''')

    testdir.makepyfile('''
        import pytest
        from pytest_logging.plugin import CONSOLEHANDLER
        LOG_FORMAT = '%(asctime)s,%(msecs)03.0f [%(name)-5s:%(lineno)-4d][%(levelname)-8s] %(message)s'

        def test_log_format():
            assert CONSOLEHANDLER.formatter._fmt == LOG_FORMAT
    ''')

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_log_format PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_log_date_format_ini_setting(testdir):
    testdir.makeini('''
        [pytest]
        log_date_format = %H:%S
    ''')

    testdir.makepyfile('''
        import pytest
        from pytest_logging.plugin import CONSOLEHANDLER
        LOG_DATE_FORMAT = '%H:%S'

        def test_log_date_format():
            assert CONSOLEHANDLER.formatter.datefmt == LOG_DATE_FORMAT
    ''')

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_log_date_format PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_logging_level_fatal(testdir):
    testdir.makepyfile('''
        import pytest
        import logging

        def test_logging_level():
            from pytest_logging.plugin import CONSOLEHANDLER
            assert CONSOLEHANDLER.level == logging.FATAL
    ''')

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_logging_level PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_logging_level_warn(testdir):
    testdir.makepyfile('''
        import pytest
        import logging

        def test_logging_level():
            from pytest_logging.plugin import CONSOLEHANDLER
            assert CONSOLEHANDLER.level == logging.WARN
    ''')

    result = testdir.runpytest('-vv')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_logging_level PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_logging_level_info(testdir):
    testdir.makepyfile('''
        import pytest
        import logging

        def test_logging_level():
            from pytest_logging.plugin import CONSOLEHANDLER
            assert CONSOLEHANDLER.level == logging.INFO
    ''')

    result = testdir.runpytest('-vv', '-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_logging_level PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_logging_level_debug(testdir):
    testdir.makepyfile('''
        import pytest
        import logging

        def test_logging_level():
            from pytest_logging.plugin import CONSOLEHANDLER
            assert CONSOLEHANDLER.level == logging.DEBUG
    ''')

    result = testdir.runpytest('-vv', '-vv')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_logging_level PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_logging_level_trace(testdir):
    testdir.makepyfile('''
        import pytest
        import logging

        def test_logging_level():
            from pytest_logging.plugin import CONSOLEHANDLER
            assert CONSOLEHANDLER.level == logging.TRACE
    ''')

    result = testdir.runpytest('-vvvvv')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_logging_level PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_logging_level_garbage(testdir):
    testdir.makepyfile('''
        import pytest
        import logging

        def test_logging_level():
            from pytest_logging.plugin import CONSOLEHANDLER
            assert CONSOLEHANDLER.level == logging.GARBAGE
    ''')

    for idx in range(6, 10):
        result = testdir.runpytest('-' + 'v'*idx)

        # fnmatch_lines does an assertion internally
        result.stdout.fnmatch_lines([
            '*::test_logging_level PASSED',
        ])

        # make sure that that we get a '0' exit code for the testsuite
        assert result.ret == 0
