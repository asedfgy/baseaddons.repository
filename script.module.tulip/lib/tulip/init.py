# -*- coding: utf-8 -*-

'''
    Tulip routine libraries, based on lambda's lamlib
    Author Twilight0

        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from __future__ import absolute_import

import sys
from tulip.compat import parse_qsl

argv = sys.argv

try:
    syshandle = int(argv[1])
except IndexError:
    syshandle = -1

sysaddon = argv[0]

try:

    params_tuple = parse_qsl(argv[2].replace('?',''))
    params = dict(params_tuple)

except IndexError:

    params = {'action': None}

__all__ = ["syshandle", "sysaddon", "params"]
