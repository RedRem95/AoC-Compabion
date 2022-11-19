#  Copyright (c) 2022  RedRem
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from unittest import TestCase

from AoC_Companion.Day import Collection, Result
from AoC_Companion.test import TestData


def _check_day(ydt, fnc, test_data):
    res: Result = fnc(test_data.test_in, log=lambda x: None, **test_data.test_config)
    assert res.data == test_data.test_out, \
        f"Test in {'/'.join(str(x) for x in ydt)}. Expected {test_data.test_out}, got {res.data}"


def test_days():
    for ydt, fnc, test_data in Collection.iterate():
        for td in test_data:
            yield _check_day, ydt, fnc, td
