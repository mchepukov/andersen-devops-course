# Homework

## Need to write python flask app

The description of the homework is at the following link -
[home task](docs/ansible_assignment.md)

Basic tasks that need implement:

- [x] Create basic functionaly of application
  - [x] Add request JSON validation
  - [x] Override processing errors 404 and 403
  - [x] Create different errors for curl or browser requests
  - [x] Add support https (443)
  - [x] Add support emoji functionality
  - [ ] Add interesting output when serving /
  - [ ] Review and rewrite code finally
- [x] Create service to run application
- [x] Add ansible role to deploy application
  - [x] Create iptables rules to allow only 22,80,433 ports
  - [x] Generate certificate for application
  - [x] Add service to autostart
  - [x] Add supporting ansible vault
- [ ] Write instructions how to deploy application on target system

## Description

This application should do exactly as described in task [here](docs/ansible_assignment.md)

At 20 Jan it's response only at 443 port with certificates, if you use ```curl``` for checking,
please add ```-k``` for ```curl``` without, it you will get next error:
```curl: (60) SSL certificate problem: self signed certificate```

Example of request with self signed certificate:
```shell
curl -k -XPOST -d'{"animal":"shark", "sound":"dododo", "count": 3}' https://debian-host

# It should return next response

🦈 says dododo
🦈 says dododo
🦈 says dododo
Made with ❤️ by Maxim Chepukov
```

## Deployment

### Add your ssh key to target host

```shell
export TARGET_HOST=192.168.1.68
ssh-copy-id -i ~/.ssh/id_rsa $TARGET_HOST
```

### Check possibility to connection to debian host

```shell
cd andsible
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

### Executing deployment script

```shell
ansible-playbook -i inventory/hosts.yaml main.yaml --ask-vault-pass
# Enter vault pass: 12345
```

