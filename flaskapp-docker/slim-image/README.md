## Build image

```shell

git clone https://github.com/mchepukov/andersen-devops-course.git
cd andersen-devops-course/flaskapp-docker/slim-image/
docker build -t flaskapp .
```

## Run application

```shell
docker run -p 80:5000 flaskapp
```

## Check running application

```shell
curl -k -XPOST -d'{"animal":"shark", "sound":"dododo", "count": 3}' http://localhost
```
