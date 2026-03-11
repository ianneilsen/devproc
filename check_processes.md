## check_processes

### Good Reads
https://www.cyberciti.biz/faq/show-all-running-processes-in-linux/

```bash
ps -e -o pid,vsz,comm= | sort -n -k 2
ps aux  | awk '{print $6/1024 " MB\t\t" $11}'  | sort -n
```

#### zombies

```bash
ps aux |grep "defunct"
```

or

```bash
ps aux |grep Z
```

#### list number of zombies

```bash
ps aux | awk {'print $8'}|grep Z|wc -l
```

#### show me the parent process of all zombies

```bash
pstree -paul
```

or

```bash
pstree -p -s PIDNum
```

#### kill the zombies

```bash
kill -9
```

#### check top processes sorted by ram and cpu

```bash
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
```

#### count the number of processess running

```bash
ps -auxeaf  | wc -l

ps aux | sort --key=11 | uniq -c -d --skip-fields=10 | sort -nr --key=1,1
```
