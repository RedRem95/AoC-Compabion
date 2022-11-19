=============
AoC-Companion
=============

.. image:: https://img.shields.io/github/license/RedRem95/AoC-Companion?style=for-the-badge
        :target: https://github.com/RedRem95/AoC-Companion

.. image:: https://img.shields.io/pypi/v/AoC-Companion.svg?style=for-the-badge
        :target: https://pypi.python.org/pypi/AoC-Companion

.. image:: https://readthedocs.org/projects/AoC-Companion/badge/?version=latest&style=for-the-badge
        :target: https://AoC-Companion.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


Python library for easier development of Advent of code solutions in python


Features
--------

* Easy development for AoC solutions
* Based on annotations => no complicated inheritance and overwritten functions
* Input data is downloaded so future runs reuse this data
* Uses environment variable for access token

Install
-------

PyPi package is coming soon. Until then installation is done via

.. code-block::

    $ pip install git+https://github.com/RedRem95/AoC-Companion.git


Usage
-----

Session Token
#############

To set your session token for this application to use and download your specific input set the `AOC_SESSION` environment variable

Implementation
##############

The library gets your code via annotations, so you can write simple python functions. See the examples below for usage.
Because of the current import strategy it is easiest if you use realtive imports in your code

See here some examples to use this library.
For more detailed explanation see Usage_

Example
#######

Below you see an example implementation for this library to implement a simple day 1

.. code-block:: python

    from AoC_Companion.Day import Task
    from AoC_Companion.test import TestData
    from AoC_Companion.Preprocess import Preprocessor


    @Preprocessor(year=2022, day=1)
    def preproc_1(data):
        # process data
        return data


    @Task(year=2022, day=1, task=1)
    def task01(data, log: Callable[[AnyStr], None]):
        # create the result for day 1 task 1
        log("Some very interesting and useful logs")
        return res


    @Task(year=2022, day=1, task=2)
    def task02(data, log: Callable[[AnyStr], None]):
        # create the result for day 1 task 2
        return res

You can run your code using `AoC_run`

An example to run the above code would be

.. code-block:: bash

    AoC_run -s /path/to/py/file.py --year 2022 --day 1

you have to provide the ´-s´ flag to point to the file that contains all your code or imports all your code.
For all available flags use `-h`.

ToDo
----

* Better implementation for the test framework
* Real documentation
* Installable via pypi
* More options using AoC_run
