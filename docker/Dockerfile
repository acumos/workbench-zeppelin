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

FROM dockercentral.it.att.com:5100/com.att.cmlp.public/zeppelin_opensource_base:1.0

ENV http_proxy http://one.proxy.att.com:8080
ENV https_proxy http://one.proxy.att.com:8080

ENV LOG_TAG="[ZEPPELIN_0.8]:" \
    Z_HOME="/opt/zeppelin" \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

#Zeppelin notebook settings for Codecloud or PV
ADD zeppelin-site.xml ${Z_HOME}/conf/zeppelin-site.xml
ADD zeppelin-site.xml ${Z_HOME}/confbackup/zeppelin-site.xml

#ADD modules for datasource api calls
ADD datasource ${Z_HOME}/interpreter/lib/python/datasource
ADD modelmanager ${Z_HOME}/interpreter/lib/python/modelmanager
ADD kerberos ${Z_HOME}/kerberos
RUN chmod 755 ${Z_HOME}/kerberos/*

#add necessary git config for notebook GITHUB setup
ADD git-config-setup.sh ${Z_HOME}/bin/git-config-setup.sh
RUN chmod 755 ${Z_HOME}/bin/git-config-setup.sh

ADD zeppelin.sh ${Z_HOME}/bin/zeppelin.sh
RUN chmod 755 ${Z_HOME}/bin/zeppelin.sh

#copy the conf copy script for PV
ADD zeppelin-conf-copy.sh ${Z_HOME}/bin/zeppelin-conf-copy.sh
RUN chmod 755 ${Z_HOME}/bin/zeppelin-conf-copy.sh

RUN chown root ${Z_HOME}

EXPOSE 8088
WORKDIR ${Z_HOME}
ENTRYPOINT [ "/opt/zeppelin/bin/zeppelin.sh", "start" ]

