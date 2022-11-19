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

from typing import Dict, Tuple, Callable, List, Iterable, Generator
from threading import Lock
from functools import lru_cache

from AoC_Companion.test import TestData


class TaskCollection(object):

    def __init__(self):
        self._lock = Lock()
        self._collection: Dict[Tuple[int, int, int], Tuple[Callable, List[TestData]]] = {}

    def add(self, year: int, day: int, task: int, task_fnc: Callable, test_data: List[TestData]):
        k = (year, day, task)
        with self._lock:
            if k in self._collection:
                raise KeyError(f"Already registered task for {year}/{day}/{task}")
            self._collection[k] = (task_fnc, test_data)

    @staticmethod
    @lru_cache()
    def _create_filter(year: int = None, day: int = None, task: int = None):
        def _filter(_k):
            if year is not None and not year == _k[0]:
                return False
            if day is not None and not day == _k[1]:
                return False
            if task is not None and task == _k[2]:
                return False
            return True
        return _filter

    def filter_keys(self, year: int = None, day: int = None, task: int = None) -> List[Tuple[int, int, int]]:
        _filter = self._create_filter(year=year, day=day, task=task)
        return sorted((x for x in self._collection.keys() if _filter(_k=x)))

    def get(self, year: int = None, day: int = None, task: int = None) -> List[Callable]:
        return [self._collection[k][0] for k in self.filter_keys(year=year, day=day, task=task)]

    def iterate(
            self, year: int = None, day: int = None, task: int = None
    ) -> Generator[None, Tuple[Tuple[int, int, int], Callable, List[TestData]], None]:
        keys = self.filter_keys(year=year, day=day, task=task)
        for k in keys:
            yield k, *self._collection[k]

    def available_years(self) -> List[int]:
        return sorted(set(x[0] for x in self._collection.keys()))

    def available_days(self, year: int = None) -> List[int]:
        _filter = self._create_filter(year=year)
        return sorted(set(x[1] for x in self._collection.keys() if _filter(_k=x)))

    def available_tasks(self, year: int = None, day: int = None) -> List[int]:
        _filter = self._create_filter(year=year, day=day)
        return sorted(set(x[2] for x in self._collection.keys() if _filter(_k=x)))


Collection = TaskCollection()
