#### lsof

### Good reads


	lsof -i

	netstat -p
	netstat -tup

	ss -tup
	ss -nap | grep process id

	lsof -i -a -p 'pidOf process'


#### Kill all processes of type

https://stackoverflow.com/questions/6381229/how-to-kill-all-processes-matching-a-name

This kill uses ps , grep and awk to find the ip address and kill all connections from it.

	ps aux | grep -ie 31.192.108.123 |awk '{print $2}'| xargs kill -9

or

The kill process kills all processes with name "process_name"

	kill -9 $(pgrep process_name)


