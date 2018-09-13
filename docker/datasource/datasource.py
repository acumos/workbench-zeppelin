#  Acumos
#  ===================================================================================
#  Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
#  ===================================================================================
#  This Acumos software file is distributed by AT&T
#  under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  This file is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import requests
import json
import pandas as pd
import io

def help():
    print 'username - your datasource username'
    print 'password - your datasource password'
    print 'Get all datasource'
    print 'Use function: datasource.get_datasource()'
    print 'For example: datasource.get_datasource()'
    print '--------'
    print 'Get content of specific datasource'
    print 'Use function: datasource.get_content(datasourceKey)'
    print 'For example: datasource.get_content(\'key1\')'
    print '--------'
    print 'Get sample of specific datasource'
    print 'Use function: datasource.get_sample(datasourceKey)'
    print 'For example: datasource.get_sample(\'key1\')'
    print '--------'
    print 'Get detail of specific datasource'
    print 'Use function: datasource.get_detail(datasourceKey)'
    print 'For example: datasource.get_detail(\'key1\')'
    print '--------'
    print 'Search for datasource based specific keyword or regular expression string'
    print 'Use function: datasource.search(keyword/regex)'
    print 'For example: datasource.search(\'[a-z]*\')'


def get_datasource():
    r = requests.get('URL', auth=('BASICUSER', 'BASICPASS'))
    if len(r.text) == 0:
        print 'There are no datasource available'
    else:
        try:
            k = r.json()
            for text in k:
                print 'datasource Key:', text['datasourceKey'], '\n', 'datasource Name:', text[
                'datasourceName'], '\n', '--------'
        except Exception:
            format = pd.read_csv(io.StringIO(r.text))
            print format

def get_content(key):
    url = 'URL' + key + '/contents'
    r = requests.get(url, auth=('BASICUSER', 'BASICPASS'))
    try:
        format = pd.read_csv(io.StringIO(r.text))
        print format
    except Exception, e:
        print 'Cannot read ' + key
        print e

def get_sample(key):
    url = 'URL' + key + '/samples'
    r = requests.get(url, auth=('BASICUSER', 'BASICPASS'))
    try:
        format = pd.read_csv(io.StringIO(r.text))
        print format
    except Exception, e:
        print 'Cannot read ' + key
        print e

def get_detail(key):
    url = 'URL' + key
    r = requests.get(url, auth=('BASICUSER', 'BASICPASS'))
    if len(r.text) == 0:
        print 'Result not found'
    else:
        try:
            k = r.json()
            t = json.dumps(k, indent=1, encoding='ascii')
            print t
        except Exception:
            format = pd.read_csv(io.StringIO(r.text))
            print format

def search(searchText):
    url = 'URL' +searchText
    r = requests.get(url, auth=('BASICUSER', 'BASICPASS'))
    if len(r.text) == 0:
        print 'Result not found'
    else:
        try:
            k = r.json()
            for text in k:
                print 'datasource Key:', text['datasourceKey'], '\n', 'datasource Name:', \
                    text['datasourceName'], '\n', '--------'
        except Exception:
            format = pd.read_csv(io.StringIO(r.text))
            print format
