auditing a web server for compromise
======================================

### Good Links
https://community.rackspace.com/general/f/general-discussion-forum/75/investigating-compromised-servers
http://www.gregfreeman.io/2013/how-to-tell-if-your-php-site-has-been-compromised/


# looking for suspect code in html or stylised web pages

style="display: none;"

grep -r "="hidden"" interch/*

iframe



# looking for md5 gzipinflate, encodings in pages


# looking for sql injectionin logs


# looking for user breachs


# logs

INPUTBODY:action=update

cat access_log* |grep "action=update"

cd /var/log/httpd
for i in `ls * |grep access`; do echo $i && grep wget $i; done
for i in `ls * |grep access`; do echo $i && grep curl $i; done



What to look for:

    netstat -natp : Looks for any suspicious connections running on odd ports
    ps -wauxxef : look for suspicious files like bash running under www context
    lsof <pid> : helps to determine where the pid above is running from




lsattr /usr/sbin | less
lsattr /usr/bin | less
lsattr /bin | less
lsattr /sbin | lessThe following command searches for all .htaccess files in all subdirectories that contains ‘http’. This will list all redirect rules that may include malicious redirect



# setgid checks

find / -xdev -user root \( -perm -4000 -o -perm -2000 \)


# The following command searches for all .htaccess files in all subdirectories that contains ‘http’. This will list all redirect rules that may include malicious redirect

find . -type f -name '\.htaccess' | xargs grep -i http;

# looking for special files with the following in them

find . -type f -name ‘*.php’ | xargs grep -l “eval *(” –color
find . -type f -name ‘*.php’ | xargs grep -l “base64_decode *(” –color
find . -type f -name ‘*.php’ | xargs grep -l “gzinflate *(” –color


# look for hidden shell code

https://github.com/neohapsis/neopi





