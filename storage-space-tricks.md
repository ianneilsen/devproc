## Find what is eating up your storage


### Good reads
https://unix.stackexchange.com/questions/117093/find-where-inodes-are-being-used

#### search all directories and show which dir is using the most space

	du -x /home |sort -rnb |more

#### list files as well as folders

	du -ah / | sort -n


	du -Sh |sort -rh | head -23

####https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/

	du -hsMB /var/* | sort -n

#### inodes 

	find / -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n

	df -i
