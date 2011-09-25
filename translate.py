#!/usr/bin/env python

import re
import sys
import urllib
import json

from django.conf import settings

TRANSLATE_BASE_URL = 'https://www.googleapis.com/language/translate/v2'

def getSplits(text,splitLength=4500):
    '''
    Translate Api has a limit on length of text(4500 characters) that can be translated at once,
    '''
    return (text[index:index+splitLength] for index in xrange(0,len(text),splitLength))

def translate(text,src='', to='en'):
    '''
    A Python Wrapper for Google AJAX Language API:
    * Uses Google Language Detection, in cases source language is not provided with the source text
    * Splits up text if longer then 4500 characters, as a limit put up by the API
    '''

    params = ({'target': to,
               'key': settings.GOOGLE_TRANSLATE_API_KEY
               })
    if src:
        params['source'] = src
    retText=''
    for text in getSplits(text):
        print 'text:', text
        url = TRANSLATE_BASE_URL + '?' + urllib.urlencode(params) + '&q=' + text
        print 'url:', url
        rawResponse = urllib.urlopen(url).read()
        print 'response:', rawResponse
        resp = json.loads(rawResponse)
        try:
            retText += resp['data']['translations'][0]['translatedText']
        except:
            raise
    return retText

def test():
    msg = "      Write something You want to be translated to English,\n"\
          "      Enter ctrl+c to exit"
    print msg
    while True:
        text = raw_input('#>  ')
        retText = translate(text)
        print retText
            
if __name__=='__main__':
    try:
        test()
    except KeyboardInterrupt:
        print "\n"
        sys.exit(0)
                    
