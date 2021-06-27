## Build image

```shell
git clone https://github.com/mchepukov/andersen-devops-course.git
cd andersen-devops-course/flaskapp-docker/slim-image/
docker build -t flaskapp .
```

## Run application

```shell
# Run application in not daemon mode (view logs and for speed testing)
# You can stop it by Ctrl+C command
docker run -p 80:5000 flaskapp
```

## Check running application

```shell
# Run command on the host where docker installed
# or other host that have access to target host - in this case change localhost with correct name or ip address
  
curl -XPOST -d'{"animal":"shark", "sound":"dododo", "count": 3}' http://localhost
```

---

## Info

### Important

It's just experimental solution, you should not probably use it in some working cases because there are
to many moments that can't be working and difficult for finding and troubleshooting

### Description

This is multistage building:
* In the first stage we install all components that needed to compile static executable file from python applicatin and compile it.
* In the second we put necessary files and run application

#### What going on in Dockerfile when it's builgind

We are get image debian:table-slim image as base.
Then update package information and install software like python git upx and binutils etc.

Clone the repo of python-flask-app from https://github.com/mchepukov/andersen-devops-course.git

Install requirements and build binary application by pyinstaller and with staticx add additional library to final executable file.

Then we put application and other needed files in scratch container.



### Container size

You can check container size with next command ```docker images flaskapp```

```shell
REPOSITORY   TAG       IMAGE ID       CREATED             SIZE
flaskapp     latest    1dd5ae9604af   About an hour ago   9.53MB
```

Or if you have [dive](https://github.com/wagoodman/dive) installed by command ```dive flaskapp```



```shell
│ Layers ├────────────────────────────────────────────────────────────────────────────── ┃ ● Current Layer Contents ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cmp   Size  Command                                                                      Permission     UID:GID       Size  Filetree
    3.2 kB  FROM 573a5014512f0f1                                                         -rwx------         0:0     9.5 MB  ├── app-slim
       0 B  COPY tmp /tmp # buildkit                                                     -rw-r--r--         0:0     3.2 kB  ├── emoji_lib.txt
    9.5 MB  COPY /andersen-devops-course/python-flask-app/dist/app-slim / # buildkit     drwxr-xr-x         0:0        0 B  └── tmp

│ Layer Details ├───────────────────────────────────────────────────────────────────────

Tags:   (unavailable)
Id:     417867040c14a471095cd1409284a9d1a63fa69e3dbb38bb845557f1e897c919
Digest: sha256:6d0344de92082c0d14058ffb3c3383a95ef91f63dfbc78ff44b5d3514324a424
Command:
COPY /andersen-devops-course/python-flask-app/dist/app-slim / # buildkit

│ Image Details ├───────────────────────────────────────────────────────────────────────

Image name: flaskapp
Total Image size: 9.5 MB
Potential wasted space: 0 B
Image efficiency score: 100 %

Count   Total Space  Path
```

### Additional information

In the first stage usage many RUN command - as usual it's not best practice, but in this case it can make easy
troubleshooting and speed up running container creating when developing.

---

### Testing info

It's tested and works on:
* MacBook with intel processor
* Debian 10 x64

```It should work at any x64 linux distribution but not guaranteed```

It doesn't work on:
* MacBook with M1 proccessor