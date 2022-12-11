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
    # @lru_cache()
    def _create_filter(years: List[int] = None, days: List[int] = None, tasks: List[int] = None):
        def _filter(_k):
            if years is not None and len(years) > 0 and _k[0] not in years:
                return False
            if days is not None and len(days) > 0 and _k[1] not in days:
                return False
            if tasks is not None and len(tasks) > 0 and _k[2] not in tasks:
                return False
            return True
        return _filter

    def filter_keys(
            self, years: List[int] = None, days: List[int] = None, tasks: List[int] = None
    ) -> List[Tuple[int, int, int]]:
        _filter = self._create_filter(years=years, days=days, tasks=tasks)
        return sorted((x for x in self._collection.keys() if _filter(_k=x)))

    def get(self, years: List[int] = None, days: List[int] = None, tasks: List[int] = None) -> List[Callable]:
        return [self._collection[k][0] for k in self.filter_keys(years=years, days=days, tasks=tasks)]

    def iterate(
            self, years: List[int] = None, days: List[int] = None, tasks: List[int] = None
    ) -> Generator[None, Tuple[Tuple[int, int, int], Callable, List[TestData]], None]:
        keys = self.filter_keys(years=years, days=days, tasks=tasks)
        for k in keys:
            yield k, *self._collection[k]

    def available_years(self) -> List[int]:
        return sorted(set(x[0] for x in self._collection.keys()))

    def available_days(self, years: List[int] = None) -> List[int]:
        _filter = self._create_filter(years=years)
        return sorted(set(x[1] for x in self._collection.keys() if _filter(_k=x)))

    def available_tasks(self, years: List[int] = None, days: List[int] = None) -> List[int]:
        _filter = self._create_filter(years=years, days=days)
        return sorted(set(x[2] for x in self._collection.keys() if _filter(_k=x)))


Collection = TaskCollection()
