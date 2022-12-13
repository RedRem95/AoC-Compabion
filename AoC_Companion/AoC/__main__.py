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

import argparse
import enum
import uuid


def main():

    from AoC_Companion.AoC import SpecialType

    def _my_type(inp: str):
        if inp is None:
            return None
        try:
            inp_int = int(inp)
            if inp_int <= 0:
                raise argparse.ArgumentTypeError(f"Only positive numbers supported. {inp_int} given")
            return inp_int
        except ValueError:
            if inp in [x.name for x in SpecialType]:
                return SpecialType[inp]
            raise argparse.ArgumentTypeError(f"Could not understand input '{inp}'")

    parser = argparse.ArgumentParser(prog="AoC_run", description="Run your AoC code")
    parser.add_argument("-s", "--source", dest="source", type=str, required=True, metavar="SOURCE",
                        help="Pass path to a python file that should be imported. From this you should import all"
                             "your other code. You can use relative imports in these codes")
    parser.add_argument("-l", "--log", dest="log", action="store_true", required=False,
                        help="If set will include logs defined in tasks")
    parser.add_argument("--year", dest="year", default=[], required=False, type=_my_type, nargs="+",
                        help=f"Define year of tasks you want to run. "
                             f"{', '.join([str(x) for x in SpecialType])} and a positive number supported")
    parser.add_argument("--day", dest="day", default=[], required=False, type=_my_type, nargs="+",
                        help=f"Define day of tasks you want to run. Options influenced by --year. "
                             f"{', '.join([str(x) for x in SpecialType])} and a positive number supported")
    parser.add_argument("--task", dest="task", default=[], required=False, type=_my_type, nargs="+",
                        help=f"Define tasks you want to run. Options influenced by --year and --day. "
                             f"{', '.join([str(x) for x in SpecialType])} and a positive number supported")

    args = parser.parse_args()

    from AoC_Companion.AoC import run, import_stuff
    from AoC_Companion.Day import Collection
    import_stuff(args.source)

    years = args.year
    days = args.day
    tasks = args.task

    years = SpecialType.apply(elements=years, coll=Collection.available_years())
    days = SpecialType.apply(elements=days, coll=Collection.available_days(years=years))
    tasks = SpecialType.apply(elements=tasks, coll=Collection.available_tasks(years=years, days=days))

    run(log=args.log, years=years, days=days, tasks=tasks)


if __name__ == "__main__":
    main()
