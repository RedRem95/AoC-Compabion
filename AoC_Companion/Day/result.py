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

from typing import Any


class Result(object):

    def __init__(self, data: Any, exec_time: float, year: int, day: int, task: int):
        self._data = data
        self._year = year
        self._day = day
        self._task = task
        self._exec_time = exec_time

    @property
    def data(self) -> Any:
        return self._data

    @property
    def year(self) -> int:
        return self._year

    @property
    def day(self) -> int:
        return self._day

    @property
    def task(self) -> int:
        return self._task

    @property
    def exec_time(self) -> float:
        return self._exec_time
