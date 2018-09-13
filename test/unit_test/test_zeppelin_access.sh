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

