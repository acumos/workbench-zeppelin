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
from base64 import b64encode

def help():
    print 'To load your model to model catalog'
    print 'Use function: modelmanager.loadtoCMLP(file,modelformat)'
    print 'For example: modelmanager.loadtoCMLP(\'regressionModel\',\'PMML\')'

def loadtoCMLP(file,format):

    basicAuth = b64encode('%s:%s' % ('BASICUSER', 'BASICPASS'))
    CCAuth = b64encode('%s:%s' % ('CCUSER', 'CCPASS'))

    catalog = {
        "key": "zeppelinnotebook",
        "namespace": 'MODELNAMESPACE',
        "name": file,
        "modelType": "PMML",
        "modelFormat": "PMML",
        "projectKey": "ST_CMLP",
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

    header = {'Authorization': 'Basic %s' % basicAuth,
              'CodeCloud-Authorization': 'Basic %s' % CCAuth

              }

    r = requests.post('URL', headers=header, files=multi_files)
    print r.text

