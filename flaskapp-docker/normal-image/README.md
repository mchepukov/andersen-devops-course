## Build image - flaskapp-normal

```shell

git clone https://github.com/mchepukov/andersen-devops-course.git
cd andersen-devops-course/flaskapp-docker/normal-image/
docker build -t flaskapp-normal .
```

## Run application

```shell
docker run -p 80:5000 flaskapp-normal
```

## Check running application

```shell
curl -XPOST -d'{"animal":"shark", "sound":"dododo", "count": 3}' http://localhost
```

---

## Info

### Description

This is multistage building:
* In the first stage we use python:3.9-slim-buster image for install additional requirements 
* In the second we use python:3.9-alpine image (it's smaller than python:3.9-slim-buster) than we put necessary files 
  and run application
  

### Container size

You can check container size with next command ```docker images flaskapp-normal```

```shell
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
flaskapp-normal   latest    8445093b836e   9 minutes ago   56.1MB
```

Or if you have [dive](https://github.com/wagoodman/dive) installed by command ```dive flaskapp-normal```



```shell
┃ ● Layers ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │ Current Layer Contents ├────────────────────────────────────────────────────────────────────
Cmp   Size  Command                                                                            Permission     UID:GID       Size  Filetree
    5.6 MB  FROM 00483cf3dd303ce                                                               drwxr-xr-x         0:0     825 kB  ├── bin
    1.7 MB  set -eux;  apk add --no-cache   ca-certificates   tzdata  ;                        -rwxrwxrwx         0:0        0 B  │   ├── arch → /bin/busybox
     29 MB  set -ex  && apk add --no-cache --virtual .fetch-deps   gnupg   tar   xz   && wget  -rwxrwxrwx         0:0        0 B  │   ├── ash → /bin/busybox
       0 B  cd /usr/local/bin  && ln -s idle3 idle  && ln -s pydoc3 pydoc  && ln -s python3 py -rwxrwxrwx         0:0        0 B  │   ├── base64 → /bin/busybox
    8.3 MB  set -ex;   wget -O get-pip.py "$PYTHON_GET_PIP_URL";  echo "$PYTHON_GET_PIP_SHA256 -rwxrwxrwx         0:0        0 B  │   ├── bbconfig → /bin/busybox
       0 B  #(nop) WORKDIR /app                                                                -rwxr-xr-x         0:0     825 kB  │   ├── busybox
     11 MB  #(nop) COPY dir:9a0ae57b546b22205c321a7fcd4dd09152a733da7f9b29408e278e01f6d376d0 i -rwxrwxrwx         0:0        0 B  │   ├── cat → /bin/busybox
                                                                                               -rwxrwxrwx         0:0        0 B  │   ├── chgrp → /bin/busybox
│ Layer Details ├───────────────────────────────────────────────────────────────────────────── -rwxrwxrwx         0:0        0 B  │   ├── chmod → /bin/busybox
                                                                                               -rwxrwxrwx         0:0        0 B  │   ├── chown → /bin/busybox
Tags:   (unavailable)                                                                          -rwxrwxrwx         0:0        0 B  │   ├── cp → /bin/busybox
Id:     00483cf3dd303ce6da1beb2bb47389a1ec26bf8f4f815fc9ea183c71dadddf7e                       -rwxrwxrwx         0:0        0 B  │   ├── date → /bin/busybox
Digest: sha256:b2d5eeeaba3a22b9b8aa97261957974a6bd65274ebd43e1d81d0a7b8b752b116                -rwxrwxrwx         0:0        0 B  │   ├── dd → /bin/busybox
Command:                                                                                       -rwxrwxrwx         0:0        0 B  │   ├── df → /bin/busybox
#(nop) ADD file:8ec69d882e7f29f0652d537557160e638168550f738d0d49f90a7ef96bf31787 in /          -rwxrwxrwx         0:0        0 B  │   ├── dmesg → /bin/busybox
                                                                                               -rwxrwxrwx         0:0        0 B  │   ├── dnsdomainname → /bin/busybox
│ Image Details ├───────────────────────────────────────────────────────────────────────────── -rwxrwxrwx         0:0        0 B  │   ├── dumpkmap → /bin/busybox
                                                                                               -rwxrwxrwx         0:0        0 B  │   ├── echo → /bin/busybox
                                                                                               -rwxrwxrwx         0:0        0 B  │   ├── ed → /bin/busybox
Total Image size: 56 MB                                                                        -rwxrwxrwx         0:0        0 B  │   ├── egrep → /bin/busybox
Potential wasted space: 649 kB                                                                 -rwxrwxrwx         0:0        0 B  │   ├── false → /bin/busybox
Image efficiency score: 99 %                                                                   -rwxrwxrwx         0:0        0 B  │   ├── fatattr → /bin/busybox
                                                                                               -rwxrwxrwx         0:0        0 B  │   ├── fdflush → /bin/busybox
Count   Total Space  Path                                                                      -rwxrwxrwx         0:0        0 B  │   ├── fgrep → /bin/busybox
    2        428 kB  /etc/ssl/certs/ca-certificates.crt                                        -rwxrwxrwx         0:0        0 B  │   ├── fsync → /bin/busybox
    3        178 kB  /lib/apk/db/installed                                                     -rwxrwxrwx         0:0        0 B  │   ├── getopt → /bin/busybox
    3         38 kB  /lib/apk/db/scripts.tar                                                   -rwxrwxrwx         0:0        0 B  │   ├── grep → /bin/busybox
    2        2.4 kB  /etc/passwd                                                               -rwxrwxrwx         0:0        0 B  │   ├── gunzip → /bin/busybox
    2        1.4 kB  /etc/group                                                                -rwxrwxrwx         0:0        0 B  │   ├── gzip → /bin/busybox
    2         870 B  /etc/shadow                                                               -rwxrwxrwx         0:0        0 B  │   ├── hostname → /bin/busybox
    3         500 B  /lib/apk/db/triggers                                                      -rwxrwxrwx         0:0        0 B  │   ├── ionice → /bin/busybox
    3         255 B  /etc/apk/world                                                            -rwxrwxrwx         0:0        0 B  │   ├── iostat → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/xmlrpc/__pycache__                               -rwxrwxrwx         0:0        0 B  │   ├── ipcalc → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/http/__pycache__                                 -rwxrwxrwx         0:0        0 B  │   ├── kbd_mode → /bin/busybox
    2           0 B  /usr/bin/groups                                                           -rwxrwxrwx         0:0        0 B  │   ├── kill → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/encodings/__pycache__                            -rwxrwxrwx         0:0        0 B  │   ├── link → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/email/__pycache__                                -rwxrwxrwx         0:0        0 B  │   ├── linux32 → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/distutils/command/__pycache__                    -rwxrwxrwx         0:0        0 B  │   ├── linux64 → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/distutils/__pycache__                            -rwxrwxrwx         0:0        0 B  │   ├── ln → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/ctypes/__pycache__                               -rwxrwxrwx         0:0        0 B  │   ├── login → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/concurrent/futures/__pycache__                   -rwxrwxrwx         0:0        0 B  │   ├── ls → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/concurrent/__pycache__                           -rwxrwxrwx         0:0        0 B  │   ├── lzop → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/collections/__pycache__                          -rwxrwxrwx         0:0        0 B  │   ├── makemime → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/asyncio/__pycache__                              -rwxrwxrwx         0:0        0 B  │   ├── mkdir → /bin/busybox
    2           0 B  /usr/local/lib/python3.9/__pycache__                                      -rwxrwxrwx         0:0        0 B  │   ├── mknod → /bin/busybox
    2           0 B  /usr/sbin/rfkill                                                          -rwxrwxrwx         0:0        0 B  │   ├── mktemp → /bin/busybox---
```

### Testing info

It's tested and works on:
* MacBook with intel processor
* Debian 10 x64
* MacBook with M1 processor
