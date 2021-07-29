# Exam task - Andersen DevOps course

## Two public repos for this exam task on Gitlab.com

1. Golang -  [https://gitlab.com/MaximChepukov/hellogolangapp](https://gitlab.com/MaximChepukov/hellogolangapp)

2. Python - [https://gitlab.com/MaximChepukov/pythonhelloapp](https://gitlab.com/MaximChepukov/pythonhelloapp)

## Languages

### Golang for first application

* gin framework
* should return "Hello world 1"
* <https://gitlab.com/MaximChepukov/hellogolangapp>
* ```curl ec2-18-223-108-14.us-east-2.compute.amazonaws.com```

### Python for second application

* flask framework
* should return "Hello world 2"
* <https://gitlab.com/MaximChepukov/pythonhelloapp>
* ```curl http://ec2-18-189-188-247.us-east-2.compute.amazonaws.com```

## Description

### Tools

* CI\CD - GitLab (hosted on gitlab.com)

* SCM\Source Control - GitLab \ Git

* Registry - Docker hub

* Infrastructure - Amazon ECS (Elastic Container Service)

* Notification - Slack

### Infrastructure - Stack

For deploy application I chose Amazon Elastic Container Service (ECS) because I never used it before,
and it's enough for this task.

Create two cluster for each application manually but in real project better to describe deployment like this in
file and store in git and deploy it from pipeline.

### Infrastructure - network bindings

#### Port forwarding

For Golang App

* Host port 80 -> Containter Port 8080 (tcp)

For Python App

* Host Port 80 -> Containter Port 5000 (tcp)

## CI/CD

### Info

Nobody can push to master branch directly - only throw creating new branch from master, and then create merger request.
When push commit automatically start linting stage. Then when is merged start stages: build, sast and deploy.

For python application deploy run in manual mode.

For golang application deploy run automatically.

### Stages

#### Linting

For golang app run next linters:

* golangci-lint
* hadolint
* dockerfilelint
* markdownlint

For python run next linters:

* pylint
* isort
* flake8
* black
* bandit
* hadolint
* dockerfilelint
* markdownlint

#### Build

Just build image and push it to repository

#### Sast

Check by snyk and sonar-qube. I implemented it as not necessary - that's why it can be skipped.

#### Deploy

Connect to ECS and update task definition for using new version of application.

### Notification

If something going wrong during CI/CD or on success I get notification in a Slack channel.
