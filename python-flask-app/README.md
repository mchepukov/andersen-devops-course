# Homework

## Need to write flask app

The description of the homework is at the following link -
[home task](docs/ansible_assignment.md)

Basic tasks that need implement:

- [x] Create basic functionality of application
  - [x] Add request JSON validation
  - [x] Override processing errors 404 and 403
  - [x] Create different errors for curl or browser requests
  - [x] Add support https (443)
  - [x] Add support emoji functionality
  - [x] Add interesting output when serving /
  - [x] Review and rewrite code finally
- [x] Create service to run application
- [x] Add ansible role to deploy application
  - [x] Create iptables rules to allow only 22,80,433 ports
  - [x] Generate certificate for application
  - [x] Add service to autostart
  - [x] Add supporting ansible vault
- [x] Write instructions how to deploy application on target system

## Description

This application should do exactly as described in task [here](docs/ansible_assignment.md)

It's response only at 443 port with certificates, if you use ```curl``` for checking,
please add ```-k``` for ```curl``` without, it you will get next error:
```curl: (60) SSL certificate problem: self signed certificate```

Example of request with self-signed certificate:
```shell
curl -k -XPOST -d'{"animal":"shark", "sound":"dododo", "count": 3}' https://debian-host

# It should return next response

🦈 says dododo
🦈 says dododo
🦈 says dododo
Made with ❤️ by Maxim Chepukov
```

## Preparation for deployment

### Check the ansible version on your system
This script is working and tested on macOS BigSur 11.14 with ansible 2.9.20 (python version = 3.9.5)

It might work with any system that can run ansible.
I't not tested with ansible version 4

You can check your ansible version with command ```ansible --version```

You must have already copied your ssh key to the target system if not please add

### Add your ssh key to target host

```shell
# Copy ssh key to remote server, please insert your ip address in command below
ssh-copy-id -i ~/.ssh/id_rsa 192.168.1.68
```

### Check possibility to connection to debian host

```shell
# Clone full repo and go to the project python-flask-app in directory with ansible role
git clone https://github.com/mchepukov/andersen-devops-course.git
cd andersen-devops-course/python-flask-app/ansible/
ansible -i inventory/hosts.yaml all -m ping
```

```shell
# if everything is ok you should see something like this

debian | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
```

### Check and change ansible script parameters if you need it

- **apply_firewall_rules** - if set *True* then apply firewall rules if *False* - than no
- **installation_dir** - your can change installation directory of app

```shell
vim inventory/group_vars/all.yaml

# apply_firewall_rules: True
# installation_dir: "/opt/flaskapp"
```

### Executing deployment script

```shell
ansible-playbook -i inventory/hosts.yaml main.yaml --ask-vault-pass
# Enter vault pass: 12345
```

After deployment complete - please check that's all working by command

```shell
# Use -k option to connect to server with self-signed certificate anyway
curl -k -XPOST -d'{"animal":"shark", "sound":"dododo", "count": 3}' https://debian-host
```

### Additional info

This script works only on 443 port with self-signed certificate. It can be run on both ports 80 and 443 if we will be using
nginx or something else as proxy server between client and flask application - but not at this time.
I strongly recommended do it in production ready deployment.


