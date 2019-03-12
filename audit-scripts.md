## Auditing linux boxes


#### Find

	find /etc -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r 

Find files which have been modified in last 60mins:

	find /target_directory -type f -mmin -60

# Last 2 days

	$ find /target_directory -type f -mtime -2 

To search for files in /target_directory (and all its sub-directories) that have been modified in the last 60 minutes, and print out their file attributes:

	$ find /target_directory -type f -mmin -60 -exec ls -al {} \; 

# or use xargs

	$ find /target_directory -type f -mmin -60 | xargs ls -l 

	find -type f -mtime -30 -printf "%M %u %g %TR %TD %p\n" > last30days.txt

	find -type f -mtime -30 -exec ls -l {} \; > last30days.txt


Here is a more complex example: To find a list of all files inside "/home/mywebsite" with the extension .php that have been changed within 30 days, you can run the following command:

	find /home/mywebsite -type f -name "*.php" -ctime -30

# set tmp as
Also, consider mounting /tmp and /var/tmp like this

Code:

/dev/hdf1 on /var/tmp type ext2 (rw,noexec,nosuid,nodev)
/dev/hdf2 on /tmp type ext2 (rw,noexec,nosuid,nodev)

#### source docs
http://www.linuxquestions.org/questions/linux-security-4/tracking-source-of-hacker-461889/

https://bobcares.com/blog/how-to-find-malware-and-malicious-code-that-anti-malware-tools-cannot/


erver. There are a few PHP functions and patterns usually used along with such gibberish in website files. They are:

eval, exec, gzinflate, base64_decode, str_rot13, gzuncompress, rawurldecode, strrev, ini_set(chr, chr(rand, shell_exec, fopen, curl_exec, popen, \x..\x..


	# find /home/*/public_html/ -type f -mtime -7 -maxdepth 4 -exec egrep -q “eval\(|exec\(|gzinflate\(|base64_decode\(|str_rot13\(|gzuncompress\(|rawurldecode\(|strrev\(|ini_set\(chr|chr\(rand\(|shell_exec\(|fopen\(|curl_exec\(|popen\(|x..x..” {} \; -print > /tmp/suspected-malware.txt

Now, let’s see how this command works:

    find – This is a Linux tool that can search for files installed by default in most servers.

    /home/*/public_html/ – This is the path that find looks for files. The * is automatically replaced by all the directory names under /home.

    -type f – This denotes that I’m looking only for files, and not directories, which makes find more efficient.

    -mtime -7 – This denotes that the files should have a modification date within the last 7 days.

    -maxdepth 4 – This denotes that I need only files within 4 layers of directories from public_html. This makes find execute faster.

    -exec egrep “pattern” {} \; – This passes each file found by find to the command egrep that will look for malicious code pattern in those files.

    -print – This will output the file name if a malware pattern was found in a file.

    > /tmp/suspected-malware.txt – This will store the output into /tmp/suspected-malware.txt, one each line.
