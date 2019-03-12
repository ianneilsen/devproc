## Security log patterns

#### Good Links

#### Basic grep/awk patterns

	cat access.log |grep "union"

	grep ../etc/passwd

PhP web shells - obviously if you have a PHP app then this will become a little harder to track down. 
But a 200 success http code might indicate a successful shell

	grep *.php?
	grep *.php? with a 200 success

Single quote

	grep %27

Something like user=%27  may indicate a sqlinjection test. Oldie but a goodie

    grep -B 3 -A 2 'INVALID USER' /VAR/LOG/AUTH.LOG
    grep -B 3 -A 2 'cat=5218+union' access_log*

    tail -f /VAR/LOG/AUTH.LOG | grep 'INVALID USER'

    grep "AUTHENTICATION FAILURE" /VAR/LOG/AUTH.LOG | CUT -D '=' -F 8
    awk '/SSHD.*INVALID USER/ { PRINT $9 }' /VAR/LOG/AUTH.LOG

Filter on errors

    grep '.ERR&GT;' /VAR/LOG/AUTH.LOG

    cat /var/log/apache2/access.log | grep -E "wp-admin|wp-login|POST /"

run a for i in statement for numbers in .php files /wordpress/wp-content/r57.php?28 200

Example sqlinjection

     UNION ALL SELECT (SELECT CONCAT(0x7171787671,IFNULL(CAST(ID AS CHAR),0x20),0x616474686c76,IFNULL(CAST(display_name AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_activation_key AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_email AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_login AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_nicename AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_pass AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_registered AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_status AS CHAR),0x20),0x616474686c76,IFNULL(CAST(user_url AS CHAR),0x20),0x71707a7871) FROM wp.wp_users LIMIT 0,1),NULL,NULL--


    grep -B 3 -A 3 'TABLE_NAME+limit' access_log* |awk -F: '{print $1 $2 $5}'

#### check for binary in logs

	grep [[:cntrl:]] /var/log/*.log

#### look for all POST commands to server

  cat ssl_request_log* |grep POST

#### ps

  ps -ef | head -1; ps -ef | grep "your-pattern-goes-here"
  ps awuxf

#### ep patterns

  grep ‘\(^\|[^0-9]\)\{1\}\([345]\{1\}[0-9]\{3\}\|6011\)\{1\}[-]\?[0-9]\{4\}[-]\?\[0-9]\{2\}[-]\?[0-9]\{2\}-\?[0-9]\{1,4\}\($\|[^0-9]\)\{1\}’ FILE_TO_SEARCH

  grep ‘\([345]\{1\}[0-9]\{3\}\|6011\)\{1\}[ -]\?[0-9]\{4\}[ -]\?[0-9]\{2\}[-]\?[0-9]\{2\}[ -]\?[0-9]\{1,4\}’ –color -H -n FILE_TO_SEARCH

  grep '163\.com' /var/log/maillog  | wc -l

  tail -F /var/log/audit/audit.log | grep AVC

  grep ^type=AVC /var/log/audit/audit.log*

  xzless database-name.sql.xz

  for  i in *.xz;do xzgrep [Pp]assword $i;done
  for  i in *.xz;do xzgrep --color [Pp]assword $i;done
  for  i in *.xz;do xzgrep --color [0-9]{8} $i;done

  grep [0-9]{4} oldlog/audit/*
  grep [0-9]{8} oldlog/audit/*
  grep [0-9]{12} oldlog/audit/*

  xzgrep [Pp]assword *.xz
  xzgrep --color [Pp]assword *.xz
  xzgrep --color "[0-9]{16}"
  xzgrep --color "[0-9]{16}" *.xz
  cd /var/log/
  ls
  xzgrep --color "[0-9]{16}" *.xz
  xzgrep --color "[0-9]{8}" *.xz

  find . -name '*.xz' | xargs xzgrep -P '\b\d{16}\b' | tee -a /tmp/maybe-cc.txt | wc -l

  grep -P '[0-9]{16}' .psql_history 
  grep -P 'credit' .psql_history 
  grep -P 'password' .psql_history 

  grep -Po '\b\d{16}\b' | sort | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt
  grep -Po '\b\d{16}\b' | sort | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txtf /tmp/maybe-cc.txt 
  grep -Po '\b\d{16}\b' | sort | xargs -l /tmp/tee /tmp/luhn-cc.txtf /tmp/maybe-cc.txt 
  grep -Po '\b\d{16}\b' /tmp/maybe-cc.txt | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt
  head /tmp/maybe-cc.txt 
  grep -Po '\b\d{16}\b' /tmp/maybe-cc.txt | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt

  find . -name '*.gz' | zgrep -P '\b\d{16}\b' | wc -l
  find . -name '*.gz' | xargs zgrep -P '\b\d{16}\b' | wc -l
  find . -name '*.gz' | xargs zgrep -P '\b\d{16}\b' | tee /tmp/maybe-cc.txt | wc -l
  find . -name '*.xz' | xargs xzgrep -P '\b\d{16}\b' | tee -a /tmp/maybe-cc.txt | wc -l

  grep autodiscover /var/log/httpd-general.log| grep -vPi '"(GET|POST) /autodiscover/autodiscover.xml '|less
  grep -i autodiscover /var/log/httpd-general.log|less

  grep cookie-notice /var/log/httpd-general.log | grep -v support\\.example\\.com | less
  grep 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)' /var/log/httpd-general.log | grep -i jquery | less
  grep -F 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)' /var/log/httpd-general.log | grep -i jquery | less
  grep -F 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)' /var/log/httpd-general.log
  grep -i jquery /var/log/httpd-general.log  | less
  grep -i jquery /var/log/httpd-general.log  | grep -v admin
  grep -i jquery /var/log/httpd-general.log  | grep -v admin | grep -v /404\\.php | less
  grep -F 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)' /var/log/httpd-general.log | less
  
  grep -F 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)' /var/log/httpd-general.log | less
  grep '64.64.64.64' /var/log/httpd-general.log | less
  grep '64.64.64.64' /var/log/httpd-general.log | grep '"status": "200"' | less
  grep -i jquery /var/log/httpd-general.log  | grep -v admin | less
  grep -i jquery /var/log/httpd-general.log  | grep -v admin | grep -v /process | less
  grep -i jquery /var/log/httpd-general.log  | grep -v admin | grep -v /process | grep -v '\.css' | less- (xzcat /var/log/httpd-general.log-2018*xz; cat /var/log/httpd-general.log) | grep 'GET /eticket' | less

  (xzcat /var/log/httpd-general.log-2018*xz; cat /var/log/httpd-general.log) | grep 'GET /eticket' | grep -vP '/eticket/(order|barcode)'
  (xzcat /var/log/httpd-general.log-2018*xz; cat /var/log/httpd-general.log) | grep 'GET /eticket' | grep -vP '/eticket/(order|barcode|passbook)'
  (xzcat /var/log/httpd-general.log-2018*xz; cat /var/log/httpd-general.log) | grep 'GET /eticket' | grep passbook | less
  grep -Po '\b\d{16}\b' | sort | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt
  grep -Po '\b\d{16}\b' /tmp/maybe-cc.txt | sort | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt
  grep -Po '\b\d{16}\b' /tmp/maybe-cc.txt | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt
  grep -Po '\b\d{16}\b' /tmp/maybe-cc.txt | xargs -l /tmp/luhn | tee /tmp/luhn-cc.txt
  ./check-pci.sh -l /var/log\*.gz -z zgrep [Pp]assword
  ./check-pci.sh -l /var/log/\*.gz -z zgrep [Pp]assword
  ./check-pci.sh -l /var/log/\*.gz -z zgrep -s [Pp]assword
  ./check-pci.sh -l /var/log/\*.gz -z zgrep -s [Uu]sername
  ./check-pci.sh -l /var/log/ -z grep -s [Uu]sername
  ./check-pci.sh -l /var/log/ -z grep -s [0-9]{4}-[0-9]{4}
  ./check-pci.sh -l /var/log/ -z grep -s [0-9]{8}
  ./check-pci.sh -l /var/log/ -z grep -s [Pp]assword

  ./check-pci.sh -l /tmp/ -z grep -s [0-9]{8}
  ./check-pci.sh -l /tmp/ -z grep -s [Pp]assword
  ./check-pci.sh -l /tmp/ -z grep -s [Uu]sername
  ./check-pci.sh -l /tmp/ -z grep -s [0-9]{4}

  ./check-pci.sh -l /var/log/ -z zgrep -s [0-9]{8}
  ./check-pci.sh -l /var/log/ -z zgrep -s [0-9]{8}
  ./check-pci.sh -l /var/log/\*.gz -z zgrep -s [0-9]{8}
  ./check-pci.sh -l /var/log/\*.gz -z zgrep -s [0-9]{16}
  ./check-pci.sh -l /var/log/\*.gz -z zgrep -s [0-9]{12}
  /check-pci.sh -l /var/log/\*.gz -z zgrep -s [Pp]assword
  ./check-pci.sh -l /var/log/\*.gz -z zgrep -s [Uu]sername
  ./check-pci.sh -l /var/log/\*.xz -z zgrep -s [Uu]sername
  ./check-pci.sh -l /var/log/\*.xz -z xzgrep -s [Uu]sername
  ./check-pci.sh -l /var/log/\*.xz -z xzgrep -s [Pp]assword
 
  ./check-pci.sh -l /var/tmp -z grep -s [0-9]{16}
  ./check-pci.sh -l /var/tmp -z grep -s [0-9]{4}
  ./check-pci.sh -l /var/tmp -z grep -s [Pp]assword
  ./check-pci.sh -l /var/tmp -z grep -s [Uu]sername
 
  ./check-pci.sh -l /var/tmp -z grep -s [Pp]assword
  ./check-pci.sh -l /var/tmp -z grep -s [Uu]sername
  ./check-pci.sh -l /var/tmp -z grep -s [0-9]{12}
 
  ./check-pci.sh -l /home/postgres -z grep -s [Uu]sername
  ./check-pci.sh -l ~postgres -z grep -s [Uu]sername
  ./check-pci.sh -l ~postgres -z grep -s [Pp]assword
  /check-pci.sh -l ~postgres -z zgrep -s [Pp]assword
  ./check-pci.sh -l ~postgres/9.5/backups/ -z zgrep -s [Pp]assword
  ./check-pci.sh -l ~postgres/9.5/backups/ -z xzgrep -s [Pp]assword
 
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s [Pp]assword
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s [Uu]sername
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s [0-9]{4}
  ./check-pci.sh -l ~postgres/9.5/backups/ -z xzgrep -s [0-9]{4}
 
  zgrep [0-9]{4}
  xzgrep [0-9]{4} *
  xzgrep -E [0-9]{4} *
   
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s [0-9]{4}
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s "[0-9]{4}"
   
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s "[0-9]{4}"
  ./check-pci.sh -l ~postgres/9.5/backups -z xzgrep -s [0-9]{4}
  ./check-pci.sh -l ~postgres/9.5/backups/ -z xzgrep -s [0-9]{4}
 
  check-pci.sh -l . -z xzgrep -s [0-9]{4}
  check-pci.sh -l $PWD -z xzgrep -s [0-9]{4}
  check-pci.sh -l $PWD -z xzgrep -s [Pp]assword
 
  xzgrep [0-9]{12} *
  xzgrep [0-9]{4} *
  xzgrep [0-9]{4}-[0-4]{4} *
  xzgrep [Pp]asswprd *
  xzgrep [Pp]assword *
  xzgrep [Uu]sername *
 
  for i in  !(*.gz); do printf "\nScanning $i...\n";grep -rw --color -E "[pP]assword" $i;done
  for i in  *.xz; do printf "\nScanning $i...\n";xzgrep -rw --color -E "[pP]assword" $i;done
  for i in  *.xz; do printf "\nScanning $i...\n";xzgrep -E "[pP]assword" $i;done
 
  for i in  *.xz; do printf "\nScanning $i...\n";xzgrep -E "[pP]assword" $i;done >> /root/tmp/jan-xzcat.txt
 
  xzcat *xz|grep -E [Pp]assword
  xzcat *xz|grep -E "^5[1-5][0-9]{2}[]{8}[0-9]{4}$|^4[0-9]{3}[]{8}[0-9]{4}$|^3[47][*][0-9]{4}$" 
  xzgrep -E "^5[1-5][0-9]{2}[]{8}[0-9]{4}$|^4[0-9]{3}[]{8}[0-9]{4}$|^3[47][*][0-9]{4}$" databasename.sql.xz 
  for i in *.xz; do xzgrep -E "^5[1-5][0-9]{2}[]{8}[0-9]{4}$|^4[0-9]{3}[]{8}[0-9]{4}$|^3[47][*][0-9]{4}$" $i;done
  for i in !(*.gz) ;do printf "\nScanning $i..\n";egrep -rw --color -E "^5[1-5][0-9]{2}[]{8}[0-9]{4}$|^4[0-9]{3}[]{8}[0-9]{4}$|^3[47][*][0-9]{4}$" $i;done 
  for i in *.xz ;do printf "\nScanning $i..\n";xzgrep -rw --color -E "^5[1-5][0-9]{2}[]{8}[0-9]{4}$|^4[0-9]{3}[]{8}[0-9]{4}$|^3[47][*][0-9]{4}$" $i;done 
  for i in *.xz ;do printf "\nScanning $i..\n";xzgrep --color -E "^5[1-5][0-9]{2}[]{8}[0-9]{4}$|^4[0-9]{3}[]{8}[0-9]{4}$|^3[47][*][0-9]{4}$" $i;done 

 
  xzgrep -Ev ".*(qrcode|code128|barcode).*\b[3456][0-9]{3}[-\[:space:]\[:digit:]][0-9]{3,4}[-\[:space:]\[:digit:]][0-9]{3,4}[-\[:space:]\[:digit:]][0-9]{1,4}" *.xz
  xzgrep -Ev ".*(qrcode|code128|barcode).*\b[3456][0-9]{3}[-\[:space:]\[:digit:]][0-9]{3,4}[-\[:space:]\[:digit:]][0-9]{3,4}[-\[:space:]\[:digit:]][0-9]{1,4}" *.xz
