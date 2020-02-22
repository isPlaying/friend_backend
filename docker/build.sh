cd ..
cp -r api docker/api
cd docker
TIMENOW=`date +%Y%m%d`
docker build -t isplaying/friend_backend:dev_${TIMENOW} .
rm -rf api/
docker push isplaying/friend_backend:dev_${TIMENOW}
