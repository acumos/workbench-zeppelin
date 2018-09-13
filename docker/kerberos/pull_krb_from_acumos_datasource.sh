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


#check number of input parameters
if [ "$#" -ne 5 ]; then
    echo "Usage: $0 \${configure_mgt_url} \${configure_mgt_uid} \${configure_mgt_password} \${datasource_ns} \${acumos_datasource_id}" 
    echo "      \${configure_mgt_uid}: the user id to access configurement management"
    echo "      \${configure_mgt_password}: the user password to access configure management"
    echo "      \${configure_mgt_url}: the spring cloud URL"
    echo "      \${datasource_namespace}: Acumos datasource namespace"
    echo "      \${acumos_datasource_id}:  Acumos datasource id"
    exit 1
fi

configure_management_url=$1
configure_mgt_uid=$2
configure_mgt_password=$3
datasource_ns=$4
datasource_id=$5

echo "configure_mgt_url: ${configure_management_url}"
echo "configure_mgt_uid: ${configure_mgt_uid}"
ehco "configure_mgt_uid: ${configure_mgt_password}"
echo "datasource_ns: ${datasource_ns}"
echo "datasource_id: ${datasource_id}"

# pull configure management map object to a tmp file /tmp/configure_map_$timestamp.properties
request_url=${configure_management_url}/${datasource_ns}_config-${datasource_id}.properties
current_timestamp=`date +%Y%m%d%H%M%S`
tmp_output_file="/tmp/conf_map_${current_timestamp}.properties"

echo "request_url: ${request_url}"
echo "tmp_output_file: ${tmp_output_file}"

curl -u "${configure_mgt_uid}:${configure_mgt_password}" --insecure ${request_url} > ${tmp_output_file}

# parse out krb5.conf and keytab files 
keyconf_tmp_file="/tmp/krb5_${current_timestamp}.conf"
keytab_tmp_file="/tmp/user_${current_timestamp}.keytab"

keyconf_prefix="KerberosConfigFileContents: "
keytab_prefix="KerberosKeyTabContent: "
krbusr_prefix="KerberosLoginUser:"

while IFS= read -r line
do 
	if [[ $line == $keyconf_prefix* ]]; then
		echo $line | sed "s/$keyconf_prefix//" > ${keyconf_tmp_file}
	fi
done < $tmp_output_file

cp $tmp_output_file ${keytab_tmp_file}

sed -i "/${keyconf_prefix}/d" ${keytab_tmp_file}
sed -i "/${krbusr_prefix}/d" ${keytab_tmp_file}
sed -i "s/${keytab_prefix}//" ${keytab_tmp_file}


# process krb5.conf file and replace the default krb5.conf file
cat ${keyconf_tmp_file} | sed 's/&#123;/{/g' | sed 's/&#125;/}/g' | sed 's/&#91;/[/g' | sed 's/&#93;/]/g' | sed 's/&#58;/:/g' | sed 's/&#59;/;/g' | sed 's/@@@/\n/g' >${keyconf_tmp_file}.new

# parse out keytab file and put it in /opt/zeppelin/conf folder
cat ${keytab_tmp_file} | openssl enc -base64 -d >${keytab_tmp_file}.new
if [ ! -s "${keytab_tmp_file}.new" ]; then
	echo "keytab is not decodable"
	cp ${keytab_tmp_file} ${keytab_tmp_file}.new
fi

# delete tmp properties file

 

