#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

-----------------------------------------------------------------------------
  Copyright (C) 2015 University of Dundee. All rights reserved.


  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

------------------------------------------------------------------------------

"""

import omero.cli
import omero
import omero.scripts as scripts
from omero.gateway import BlitzGateway


def runAsScript():
    """
    The main entry point of the script, as called by the client via the
    scripting service, passing the required parameters.
    """

    client = scripts.client('CLI Test.py', "Test script/CLI interactions")

    try:
        conn = BlitzGateway(client_obj=client)

        cli = omero.cli.CLI()
        cli.loadplugins()

        cmd = []
        cmd.extend(["login"])
        cmd.extend(["-s", "localhost"])
        # cmd.extend(["-g", conn.getGroupFromContext().getName()])
        cmd.extend(["-p", "4064"])
        cmd.extend(["-k", conn._getSessionId()])

        cli.invoke(cmd, strict=True)

    finally:
        client.closeSession()

if __name__ == "__main__":
    runAsScript()
