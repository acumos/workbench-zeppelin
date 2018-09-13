#!/usr/bin/env python2

#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements.  See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License.  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  Modifications Copyright © 2018 AT&T Intellectual Property.

import requests
import json
from base64 import b64encode

def help():
    print 'To load your model to model catalog'
    print 'Use function: modelmanager.loadtoAcumos(file,modelformat)'
    print 'For example: modelmanager.loadtoAcumos(\'regressionModel\',\'PMML\')'

def loadtoAcumos(file,format):

    catalog = {
        "key": "zeppelinnotebook",
        "namespace": 'MODELNAMESPACE',
        "name": file,
        "modelType": "PMML",
        "modelFormat": "PMML",
        "projectKey": "YOUR_PROJECT_KEY",
        "icon": "",
        "description": "",
        "sharedUsers": [],
        "sharedRoles": [],
        "isSharedAll": False,
        "modelComment": "",
        "documentComment": "",
        "metadata": [],
        "customMetadata": []
    }

    json.dump(catalog, open("catalog.json", "w"), indent=4)

    multi_files = {'catalog': open('catalog.json', 'rb'), 'file': open(file + '.' + format, 'r')}

    r = requests.post('URL', files=multi_files)
    print r.text

