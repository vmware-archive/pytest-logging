pytest-logging
==============

.. image:: https://travis-ci.org/saltstack/pytest-logging.svg?branch=master
    :target: https://travis-ci.org/saltstack/pytest-logging
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/saltstack/pytest-logging?branch=master
    :target: https://ci.appveyor.com/project/saltstack-public/pytest-logging/branch/master
    :alt: See Build Status on AppVeyor

Configures logging and allows tweaking the log level with a py.test flag

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

* Configures python's logging to output log messages to the console(You need to tell `PyTest`_ not to capture output).
* Increases the logging verbosity by lowering the log level by passing `-v` to `PyTest`_


Requirements
------------

* None!


Installation
------------

You can install "pytest-logging" via `pip`_ from `PyPI`_::

    $ pip install pytest-logging


Usage
-----

* Simply pass one or more `-v` flag(s) to `PyTest`_ to increase logging verbosity


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `Apache 2.0`_ license, "pytest-logging" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/saltstack/pytest-logging/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`Apache 2.0`: http://www.apache.org/licenses/LICENSE-2.0
