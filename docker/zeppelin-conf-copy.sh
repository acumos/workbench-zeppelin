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

if [ -d "/opt/zeppelin/conf/notebook" ]; then
	echo "notebook folder was already copied in PV mounted folder"
	cp  /opt/zeppelin/confbackup/zeppelin-site.xml /opt/zeppelin/conf/zeppelin-site.xml
else
	echo "start copying config files from /opt/zeppelin/confbackup to /opt/zepppelin/conf"
	cp -r /opt/zeppelin/confbackup/* /opt/zeppelin/conf
fi

