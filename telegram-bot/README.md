# Telegram bot on golang

---
Telegram Bot is available on the next link [https://t.me/maxche_github_bot](https://t.me/maxche_github_bot)

---

## Task description

Write telegram bot on golang with minimum three commands:
- /git - return link to git repo
- /tasks - return numbered list completed tasks
- /task # - where # is task number, return link to the folder in repo with completed task


## Info about implementation

This bot wrote on goland and use some external libraries like:

- viper to parse config files with telegram api token and repo url and parse task list
- and telebot for working with telegram api

On start from config.yaml file read telegram api token and github repo then
from tasks.yaml file read tasks list.

It's support **hot load** without needed to restart bot application, just need to add/remove task in tasks.yaml


## Config and tasks files examples

```shell
# tasks.yaml
---
TELEGRAM_API_TOKEN: "{TELEGRAM_API_TOKEN}"
GITHUB_REPO: "https://github.com/mchepukov/andersen-devops-course"

```

```shell
# tasks.yaml
---
tasks:
  task1:
    name: "python-flask-app"
    progress: "done"
    url: "https://github.com/mchepukov/andersen-devops-course/tree/main/python-flask-app"
  task2:
    name: "netstat-bash-script"
    progress: "done"
    url: "https://github.com/mchepukov/andersen-devops-course/tree/main/netstat-bash-script"
  task3:
    name: "flaskapp-docker"
    progress: "done"
    url: "https://github.com/mchepukov/andersen-devops-course/tree/main/flaskapp-docker"
  task4:
    name: "telegram-bot"
    progress: "done"
    url: "https://github.com/mchepukov/andersen-devops-course/tree/main/telegram-bot"
```

## What needs to do

[x] Create base functionality of telegram bot

[x] Add the ability to storing tokens and parameters in config file

[x] Add the ability to storing tasks in external file

[ ] Add help command to get info about command

[ ] Add hints when typing bot commands

[ ] Create service file to start golang application

[ ] Add deploy application to amazon
