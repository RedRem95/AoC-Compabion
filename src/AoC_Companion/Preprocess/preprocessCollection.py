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

from typing import Dict, Tuple, Callable, Optional, Any, Tuple
from threading import Lock


class PreprocessCollection(object):

    def __init__(self):
        self._lock = Lock()
        self._collection: Dict[Tuple[Optional[int], Optional[int], Optional[int]], Callable] = {}

    def add(self, preprocess_fnc: Callable, year: int = None, day: int = None, task: int = None):
        if year is None and day is not None:
            raise ValueError("When year is none you cant put a none day")
        if year is None and task is not None:
            raise ValueError("When year is none you cant put a none task")
        if day is None and task is not None:
            raise ValueError("When day is none you cant put a none task")
        k = (year, day, task)
        with self._lock:
            if k in self._collection:
                raise KeyError(f"Already registered preprocessor for {year}/{day}/{task}")
            self._collection[k] = preprocess_fnc

    def preprocess(self, data: Any, year: int = None, day: int = None, task: int = None) -> Tuple[Any, int]:
        keys = [(None, None, None)]
        if year is not None:
            keys.append((year, None, None))
            if day is not None:
                keys.append((year, day, None))
                if task is not None:
                    keys.append((year, day, task))

        i = 0
        for k in keys:
            if k in self._collection:
                data = self._collection[k](data)
                i += 1

        return data, i


Collection = PreprocessCollection()
