## Build image - - flaskapp-slim

```shell
git clone https://github.com/mchepukov/andersen-devops-course.git
cd andersen-devops-course/flaskapp-docker/slim-image/
docker build -t flaskapp-slim .
```

## Run application

```shell
# Run application in not daemon mode (view logs and for speed testing)
# You can stop it by Ctrl+C command
docker run -p 80:5000 flaskapp-slim
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
* In the first stage we install all components that needed to compile static executable file from python application and compile it.
* In the second we put necessary files and run application

#### What going on in Dockerfile when it's building

We are get image amd64/debian:stable-slim image as base.
Then update package information and install software like python git upx and binutils etc.

Clone the repo of python-flask-app from https://github.com/mchepukov/andersen-devops-course.git

Install requirements and build binary application by pyinstaller and with staticx add additional library to final executable file.

Then we put application and other needed files in scratch container.



### Container size

You can check container size with next command ```docker images flaskapp-slim```

```shell
REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
flaskapp-slim   latest    b2d00b07f24a   4 minutes ago   9.61MB
```

Or if you have [dive](https://github.com/wagoodman/dive) installed by command ```dive flaskapp-slim```



```shell
┃ ● Layers ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │ Current Layer Contents ├─────────────────────────────────────────────────────
Cmp   Size  Command                                                             Permission     UID:GID       Size  Filetree
    3.2 kB  FROM 866fe5b21fb09c7                                                -rw-r--r--         0:0     3.2 kB  └── emoji_lib.txt
       0 B  #(nop) COPY dir:737a50ce360d39605f306124cc8a335f86c184026ab92f3d94c
    9.6 MB  #(nop) COPY file:78c684d9dc5b53e52eaeeaa87988b03d4d7239418e3cb634a1

│ Layer Details ├──────────────────────────────────────────────────────────────

Tags:   (unavailable)
Id:     866fe5b21fb09c7a209b394ce7e94506c9a1c2d516a9fc12cc203424923d9db5
Digest: sha256:67584c5cdd2d49f4f3e1cd78df0118c420148653ec8d875b186e6b301f018207

Command:
#(nop) COPY file:fccb378945275cc190854b9e66ecfedfe29f07a276f9297ea3d30b9742dcb7
39 in /

│ Image Details ├──────────────────────────────────────────────────────────────


Total Image size: 9.6 MB
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
* MacBook with M1 processor