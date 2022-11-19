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

from typing import Any, Dict
from copy import deepcopy


class TestData(object):

    def __init__(self, test_in: Any, test_out: Any, extra_config: Dict[str, Any] = None):
        if extra_config is None:
            extra_config = {}

        self._test_in = test_in
        self._test_out = test_out
        self._extra_config = extra_config

    @property
    def test_in(self) -> Any:
        return self._test_in

    @property
    def test_out(self) -> Any:
        return self._test_out

    @property
    def test_config(self) -> Dict[str, Any]:
        return {x: deepcopy(y) for x, y in self._extra_config.items()}
