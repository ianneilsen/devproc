find modifed files tricks
===========================

#### find all files with format 

find $1 -type f -print0 | xargs -0 stat --format '%Y :%y %n' | sort -nr | cut -d: -f2- | head


#### files which have changed in the last 30mins

	find /home/ -mmin -30 -ls

	find srch_dir -cmin -60

	find / -cmin -60

#### Find files changed in last 24 hours

	find /directory_path -mtime -1 -ls

	find . -mtime -0

find /home/mieow/ -mtime -0 | sort -r | more
find . -mtime 0 -printf '%T+\t%s\t%p\n' 2>/dev/null | sort -r | more

#### Find files modified between - ctime relates to file  mtime relates to content.

	find -ctime +20  -ctime -30

#### Find files modified 2500 and 2800 minutes ago

	find -cmin +2500  -cmin -2800

#### find files in the last 3 days

	find -mtime -3

#### find files longer than 3 days ago

	find -mtime +3


#### files by modification time

find srch_dir -mmin -60

#### find all files modified in last hour

find . -mtime -1
	
the . is the search path
-mtime time parameter
-1 list files modified in the last 24 hours

#### access time

find srch_dir -amin -60 

#### find all files with zero 0 - you can add alot more here, but this get you started.

find $dir -size 0 -type f

##### You may have to print the output sometimes.

find "$dir" -size 0 -print


#### pstree

pstree -pa


#### diff

diff -qr

vimdiff fileName fileNAme

colordiff

#### find all files which are allowed +x executable



