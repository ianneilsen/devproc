## swap checks

### Good reads

Simple check

```bash
	for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done
```

To sort by highest to lowest 

```bash
	for file in /proc/*/status ; do awk '/VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 2 -n -r | less
```

AND OR use

```bash
	yum install smem
	smem
```
#### how much swap used

```bash

$ free
               total        used        free      shared  buff/cache   available
Mem:        98785652    16218972    68235664      533768    12731960    82566680
Swap:        8388604           0     8388604
```

or

```bash
	(echo "COMM PID SWAP"; for file in /proc/*/status ; do awk '/^Pid|VmSwap|Name/{printf $2 " " $3}END{ print ""}' $file; done | grep kB | grep -wv "0 kB" | sort -k 3 -n -r) | column -t
```

#### smem

```bash
	yum install smem

	smem -s swap -r
```