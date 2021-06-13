# Homework - Task 2

## Need to write bash script

### Than should do something like than next script

```bash
sudo netstat -tunapl | awk '/firefox/ {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n5 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F':' '/^Organization/ {print $2}' ; done
```

Full description of task [here](hw-task.md)

Syntax:

```bash
nstat.sh [-p PID] - get information by process pid
nstat.sh [-n NAME] - get information by process name
nstat.sh [-c NUMBER] - limit output information
nstat.sh [-s STATE] - show only with this state
nstat.sh [-r GET_INFO] - get this info from whois"
```

Usage:

For example to get information about *Organization* with process with name *firefox* and limit onput to 6 line and state is established:

```bash
sudo ./netstat.sh -n firefox -r Organization -c 6 -s established
```

Output example:

```bash
----------------------------------
Running with following parameters:
----------------------------------
Get the next info from whois by regexp: ^Organization|organisation|org-name|person|descr
Output lines limit is: 6
State connection is: ESTABLISHED
Information for process name: firefox
----------------------------------
1 : 44.238.3.246 : Amazon.com, Inc. (AMAZO-4) Amazon.com, Inc. (AMAZO-47)
```

By default:

if *STATE* paraments is not given, it's will be *established*

if *GET_INFO* paraments is not given, it's will be *^Organization|organisation|org-name|person|descr*
