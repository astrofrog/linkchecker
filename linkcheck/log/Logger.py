# Copyright (C) 2000-2002  Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

class Logger:
    def __init__ (self, **args):
        self.logfields = None # all fields
        if args.has_key('fields'):
            if "all" not in args['fields']:
                self.logfields = args['fields']

    def logfield (self, name):
        if self.logfields is None:
            return 1
        return name in self.logfields

    def init (self):
        raise Exception, "abstract function"

    def newUrl (self, urlData):
        raise Exception, "abstract function"

    def endOfOutput (self, linknumber=-1):
        raise Exception, "abstract function"
