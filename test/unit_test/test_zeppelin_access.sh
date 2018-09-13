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


YOUR_DEPLOYED_HOST=$1
zeppelin_url=$YOUR_DEPLOYED_HOST:8088

retcode=0
host_port=`echo $zeppelin_url|sed -e 's/:/ /g'`
echo exit | telnet $host_port 2>/dev/null | grep "Connected to" >/dev/null 2>&1
if [ $? -ne 0 ]; then
   echo "Failure - Zeppelin is NOT accessible"
   retcode=1
else
   echo "Success - Zeppelin is accesisble"
fi

