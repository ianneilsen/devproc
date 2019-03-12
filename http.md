## httpd 


#### Good reads

Link to Apache htpasswd directives

* https://httpd.apache.org/docs/2.4/programs/htpasswd.html

Httpd status codes

* https://www.restapitutorial.com/httpstatuscodes.html

#### http redirect or rewrite rules

* Easy to read rewrite readme

https://www.addedbytes.com/blog/url-rewriting-for-beginners

* Test your rules

https://htaccess.madewithlove.be/

* regex tester

https://www.regextester.com/

#### Security for your website

* Don't use old SSL/TLS ciphers and protocols
Strict-Transport Security" max-age=3153600
Content-Security-Policy
--what sources are my images coming from
--where is my javascript coming from
-Content-Security-Policy: default 'none'; img-src 'self' data:; script-src 'self' 'unsafe-inline'

frame source - sometimes you need to
Referer-Policy: Only send referrers under certain conditions
--no path information
-- dont send me referrer info
-- strict-origin
-- you may need hostname referrers

Feature-Policy:
geoLocation - 'none'; vibrate 'none'
-- stop google android phones from getting info

x-content-type-options: no-sniff
-- dont second guess mime types
-- dont guess, if its wrong break

Dont tell people what web server you are running

Generate SRI on js or images etc

Cookies
-- set secure Secure on cookie
-- SameSite=Strict
-- stops CSRF or helps to stop it
-- check libs support it
-- add header to the end


turn on http2
-- supports multiplexing
-- more efficent

New headers coming
-- H2ModernTLSOnly on

-- Network Error Logging coming

Logging
-- adjust logs to show protocols and ciphers being used so you know what clients ar eusing on your site
