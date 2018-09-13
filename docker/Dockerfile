# 
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

FROM ubuntu:16.04
MAINTAINER Apache Software Foundation <dev@zeppelin.apache.org>

ENV Z_VERSION="0.8.0"
#ENV Z_VERSION="0.7.3"
ENV LOG_TAG="[ZEPPELIN_${Z_VERSION}]:" \
    Z_HOME="/opt/zeppelin" \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

RUN echo "$LOG_TAG update and install basic packages" && \
    apt-get -y update && \
    apt-get install -y locales && \
    locale-gen $LANG && \
    apt-get install -y software-properties-common && \
    apt -y autoclean && \
    apt -y dist-upgrade && \
    apt-get install -y build-essential

RUN echo "$LOG_TAG install tini related packages" && \
    apt-get install -y wget curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
RUN echo "$LOG_TAG Install java8" && \
    apt-get -y update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

# should install conda first before numpy, matploylib since pip and python will be installed by conda
RUN echo "$LOG_TAG Install miniconda2 related packages" && \
    apt-get -y update && \
    apt-get install -y bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion && \
    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh
ENV PATH /opt/conda/bin:$PATH


RUN echo "$LOG_TAG Install python related packages" && \
    apt-get -y update && \
    apt-get install -y python-dev python-pip && \
    apt-get install -y gfortran && \
    # numerical/algebra packages
    apt-get install -y libblas-dev libatlas-dev liblapack-dev && \
    # font, image for matplotlib
    apt-get install -y libpng-dev libfreetype6-dev libxft-dev && \
    # for tkinter
    apt-get install -y python-tk libxml2-dev libxslt-dev zlib1g-dev && \
    pip install numpy && \
    pip install matplotlib && \
    # added more libraries (later read from requirements.txt file)
    pip install pyspark && \
    pip install scipy && \
    pip install pandas && \
    pip install pandasql && \
    pip install sklearn && \
    pip install xgboost

RUN echo "$LOG_TAG Install R related packages" && \
    echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list && \
    gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \
    gpg -a --export E084DAB9 | apt-key add - && \
    apt-get -y update && \
    apt-get -y install r-base r-base-dev && \
    R -e "install.packages('knitr', repos='http://cran.us.r-project.org')" && \
    R -e "install.packages('ggplot2', repos='http://cran.us.r-project.org')" && \
    R -e "install.packages('googleVis', repos='http://cran.us.r-project.org')" && \
    R -e "install.packages('data.table', repos='http://cran.us.r-project.org')" && \
    # for devtools, Rcpp
    apt-get -y install libcurl4-gnutls-dev libssl-dev && \
    R -e "install.packages('devtools', repos='http://cran.us.r-project.org')" && \
    R -e "install.packages('Rcpp', repos='http://cran.us.r-project.org')" && \
    Rscript -e "library('devtools'); library('Rcpp'); install_github('ramnathv/rCharts')"

# install kerberos client
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install krb5-user    

# install vi
RUN echo "$LOG_TAG Install vi"  && \
    DEBIAN_FRONTEND=noninteractive apt-get -y update && \
    apt-get -y install vim

RUN echo "$LOG_TAG Download Zeppelin binary" && \
    wget -O /tmp/zeppelin-${Z_VERSION}-bin-all.tgz http://archive.apache.org/dist/zeppelin/zeppelin-${Z_VERSION}/zeppelin-${Z_VERSION}-bin-all.tgz && \
    tar -zxvf /tmp/zeppelin-${Z_VERSION}-bin-all.tgz && \
    rm -rf /tmp/zeppelin-${Z_VERSION}-bin-all.tgz && \
    mv /zeppelin-${Z_VERSION}-bin-all ${Z_HOME}


RUN echo "$LOG_TAG Cleanup" && \
    apt-get autoclean && \
    apt-get clean

#Logging setup
RUN mkdir ${Z_HOME}/logs
ADD log4j.properties ${Z_HOME}/conf/log4j.properties
ADD log4j.properties ${Z_HOME}/confbackup/log4j.properties
RUN chmod 755 ${Z_HOME}/*

# add interpreter configuration with hive, HDFS and livy for spark
ADD interpreter.json ${Z_HOME}/conf/interpreter.json

#Create a landing page with selected notebooks
ADD notebook ${Z_HOME}/confbackup/notebook
ADD interpreter.json ${Z_HOME}/confbackup/interpreter.json
ADD notebook-authorization.json ${Z_HOME}/confbackup/notebook-authorization.json

#Add soft symbolic link to /etc/krb5.conf
RUN mv /etc/krb5.conf ${Z_HOME}/conf/krb5.conf
RUN cp ${Z_HOME}/conf/krb5.conf ${Z_HOME}/confbackup/krb5.conf
RUN ln -s ${Z_HOME}/conf/krb5.conf /etc/krb5.conf

#Specify where notebook directory is
ADD zeppelin-env.sh ${Z_HOME}/conf/zeppelin-env.sh
ADD zeppelin-env.sh ${Z_HOME}/confbackup/zeppelin-env.sh

#Copy other default config files
ADD interpreter-list ${Z_HOME}/confbackup/interpreter-list
ADD configuration.xsl ${Z_HOME}/confbackup/configuration.xsl

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
