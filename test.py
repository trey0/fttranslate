#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
newTableConfig = {
    'tablename': {
    'address_japanese':'LOCATION',
    'address_english':'STRING'
    }
    }

#newTableId = ft_client.query(SQL().createTable(newTableConfig)).split("\n")[1]
newTableId = 1614172

print 'newTableId:', newTableId
resultText = ft_client.query('SELECT * FROM %s LIMIT 1' % tableid)
print 'sql result:', resultText
resultUnicode = unicode(resultText, encoding='utf-8')
rows = StringIO(resultUnicode)
rows.readline() # discard header
for row in rows:
    row = row[:-1]
    fields = row.split(',')
    print fields
    jploc = fields[0]
    enloc = translate(jploc, u'ja')
    print 'enloc:', enloc
    ftResponse = ft_client.query(u"INSERT INTO %s ('address_japanese', 'address_english') VALUES ('%s', '%s')"
                                 % (newTableId, jploc, enloc))
    rowid = int(ftResponse.split("\n")[1])
    print 'Inserted %d' % rowid
