## Apache

### Good reads

* https://likegeeks.com/linux-web-server/
* https://www.linode.com/docs/web-servers/apache-tips-and-tricks/apache-configuration-basics/
* https://www.linode.com/docs/web-servers/lamp/lamp-on-centos-7/

#### Mozilla ssl configuation generator

https://mozilla.github.io/server-side-tls/ssl-config-generator/

Great site to check basic configs for various versins of http servers, old to new tyle configurations and server/openssl versions


#### config tests

```bash
	apachectl configtest nameofConfig.conf

	apachectl -t

	systemctl reload httpd

	apachectl graceful
```

#### Good reads

https://httpd.apache.org/docs/2.4/programs/apachectl.html

https://www.lisenet.com/2016/advanced-apache-configuration-with-selinux-on-rhel-7/


#### Apache on Ubuntu/debian
You can enable modules using a2enmod. For example:

```bash
	a2enmod proxy
```

That command will create a symlink inside ```/etc/apache2/mods-enabled``` that points to the module in ```/etc/apache2/mods-available```.

Likewise, to disable a module, use ```a2dismod```. That command will remove the symlink from the mods-enabled directory.

{% hint style="info" %}
Bonus tip: there exist similar commands to enable/disable sites: look at a2ensite and a2dissite.
{% endhint %}

#### Apache on Centos
