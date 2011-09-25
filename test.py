#!/usr/bin/env python

import os
import sys

from authorization.clientlogin import ClientLogin
from sql.sqlbuilder import SQL
import ftclient
from fileimport.fileimporter import CSVImporter

from django.conf import settings

# make sure we can do local imports
thisDir = os.path.dirname(__file__)
sys.path = [thisDir] + sys.path

token = ClientLogin().authorize(settings.USERNAME, settings.PASSWORD)
ft_client = ftclient.ClientLoginFTClient(token)

tableid = 573451

print ft_client.query(SQL().select(tableid, None, ""))
