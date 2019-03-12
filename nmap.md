## nmap scans

### Good reads

https://highon.coffee/blog/nmap-cheat-sheet/


#### port scan which is semi quick, t5 is more agressive and quicker but throws false positives

	nmap -p 1-9000 -sV -sS -T4 ln103.example.com
