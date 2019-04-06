Bash trcks 
===============

#### Good Links
cheatsheet for bash scripting - https://devhints.io/bash

https://github.com/awesome-lists/awesome-bash

colours in bash
https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux

## expect script magic

https://likegeeks.com/expect-command/
https://likegeeks.com/write-shell-script/
https://likegeeks.com/awk-command/

#### auto complete on some OS's

	tab - to autocomplete or install auto-completion package on centos/rpm systems

#### bash script

	#!/bin/bash
	script contents.

#### movement keys

move by each word

	alt+b - move a word backwards
	alt+e - move a word forwards

move entire line

	ctrl + a - move to start of line
	ctrl + e - move to end of line

shebang - !!

cut n pasta

	ctrl + k - cut end of line from cursor
	ctrl + Y - yank
	ctrl + U - cuts all test before cursor

delete words backwards

	ctrl + w - kill words backwards

#### Bash loops 

for i in something

#### less

use less instead of tail

	less +f /var/log/log

#### run bash when user doesnt have bin login i.e. user = nologin

You can use the -s switch to su to run a particular shell

	su -s /bin/bash -c '/path/to/your/script' testuser

