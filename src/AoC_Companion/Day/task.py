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


from typing import Callable, Dict, Any, List, Tuple
from time import perf_counter
from threading import Lock

from AoC_Companion.Day import Result, Collection
from AoC_Companion.test import TestData


# noinspection PyPep8Naming
def Task(year: int, day: int, task: int, extra_config: Dict[str, Any] = None, test_data: List[TestData] = None):
    if extra_config is None:
        extra_config = {}
    if test_data is None:
        test_data = []

    def decorate(function: Callable):
        def wrapper(*args, **kwargs):
            if "log" in kwargs:
                log = kwargs["log"]
            else:
                def log(*_args, **_kwargs):
                    return None
            all_keys = set().union(kwargs.keys(), extra_config.keys())
            kwargs_upd = {k: kwargs.get(k, extra_config.get(k, None)) for k in all_keys}
            try:
                del kwargs_upd["log"]
            except KeyError:
                pass
            t1 = perf_counter()
            res = function(*args, log=log, **kwargs_upd)
            t2 = perf_counter()
            return Result(data=res, exec_time=t2-t1, year=year, day=day, task=task)

        Collection.add(year=year, day=day, task=task, task_fnc=wrapper, test_data=test_data)

        return wrapper

    return decorate

