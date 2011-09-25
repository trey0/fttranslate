#!/usr/bin/env python

import os
import sys
import json
from StringIO import StringIO

from authorization.clientlogin import ClientLogin
from sql.sqlbuilder import SQL
import ftclient
from fileimport.fileimporter import CSVImporter
from django.conf import settings

from translate import translate

# make sure we can do local imports
thisDir = os.path.dirname(__file__)
sys.path = [thisDir] + sys.path

token = ClientLogin().authorize(settings.USERNAME, settings.PASSWORD)
ft_client = ftclient.ClientLoginFTClient(token)

tableid = 575705
srcLanguage = 'ja'

resultText = ft_client.query('select * from %s limit 2' % tableid)
print 'sql result:', resultText
rows = StringIO(resultText)
rows.readline() # discard header
for row in rows:
    row = row[:-1]
    fields = row.split(',')
    print fields
    print translate(fields[0])
