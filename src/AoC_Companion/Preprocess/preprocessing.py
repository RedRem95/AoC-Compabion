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

from typing import Callable

from AoC_Companion.Preprocess.preprocessCollection import Collection


# noinspection PyPep8Naming
def Preprocessor(year: int = None, day: int = None, task: int = None):

    def decorate(function: Callable):
        def wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            return res

        Collection.add(year=year, day=day, task=task, preprocess_fnc=wrapper)

        return wrapper

    return decorate
