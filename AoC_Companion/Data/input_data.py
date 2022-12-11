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
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from typing import Optional, Tuple, Any

from AoC_Companion.Data.download import download, input_url
from AoC_Companion.Preprocess import Collection

__NOT_RELEASED = "Please don't repeatedly request this endpoint before it unlocks! " \
                 "The calendar countdown is synchronized with the server time; " \
                 "the link will be enabled on the calendar the instant this puzzle becomes available."
__NOT_LOGGED_IN = "Puzzle inputs differ by user.  Please log in to get your puzzle input."


def get_data(year: int, day: int, task: Optional[int] = None) -> Tuple[Any, int]:
    resource_folder = os.path.join(os.path.abspath("resources"), str(year))
    data_file = os.path.join(resource_folder, f"{day}.txt")
    os.makedirs(resource_folder, exist_ok=True)
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f_read:
            ret = f_read.read()
    else:
        ret = download(input_url(year=year, day=day), session_id=os.environ.get("AOC_SESSION", None), verbose=False)
        if ret.strip() not in (__NOT_RELEASED, __NOT_LOGGED_IN):
            with open(data_file, "w", encoding="utf-8") as f_write:
                f_write.write(ret)
    ret = ret.strip()
    ret, count = Collection.preprocess(data=ret, year=year, day=day, task=task)
    return ret, count
