"""
    AoC-Companion INIT IT and versioning :)
    Copyright (C) 2022  RedRem
"""

import os

with open(os.path.join(os.path.dirname(__file__), "version.txt"), "r") as f_in:
    __version__ = f_in.read().strip()


del os
