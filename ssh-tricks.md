## ssh tricks

### Good reads
https://www.rackaid.com/blog/how-to-harden-or-secure-ssh-for-improved-security/
https://www.rackaid.com/blog/how-to-block-ssh-brute-force-attacks/

#### ssh agent issues

	set | grep ^SSH
	eval `ssh-agent -s`
	set | grep ^SSH
	ssh-add -D
	ssh-add -c /home/mieow/.ssh/ep/ian_ep

#### ssh key cmds

	ssh-add wherIsMyKey
	
##### instead of using the proxycommand you can use the -J switch. Comma separate bastions for more than one jump

	ssh -J root@bastionhost.example.com:22 root@example.example.com

##### old way

	$ ssh -o ProxyCommand="ssh -W %h:%p jumphost.example.org" server.example.org

#### ssh tunneling

http://www.sbarjatiya.com/notes_wiki/index.php/Tunneling_using_SSH_server_listening_on_port_443

Tunnelling via a bastion host forwarding ports back to your machine. Good for viewing a whitelisted web server

	ssh user@123.123.123.123 -J bastionhost.example.com -L 3080:127.0.0.1:80

	sshp server_user@123.123.123.123 -L3080:localhost:80

	ssh -A admin@bastionhost.example.com -L 127.0.0.1:3080:127.0.0.1:3080

	ssh -A server_user@123.123.123.123 -J bastion.example.com -L 127.0.0.1:3080:127.0.0.1:80

#### ssh key gen

	ssh-keygen -t rsa -b 4096 -C "name@email_address.com"

#### check your ssh ket RSA fingerprint

	ssh-keygen -lf id_rsa.pub

#### ssh with port forwarding back to your own machine

	ssh -L 5901:localhost:5901 root@example.com.server

The above example will allow me to run vnc from a local remina client. You can change port and do mytsql or whatever you like.
Port 443, 80, 190, 53, etc etc.

#### ssh with x server to run a local application

	ssh -X

#### ssh without using your keys

	ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no root@host.example.com

#### tunneling through ports

Configuring Dynamic Tunneling to a Remote Server

SSH connections can be used to tunnel traffic from ports on the local host to ports on a remote host.

A dynamic tunnel is similar to a local tunnel in that it allows the local computer to connect to other resources through a remote host. A dynamic tunnel does this by simply specifying a single local port. Applications that wish to take advantage of this port for tunneling must be able to communicate using the SOCKS protocol so that the packets can be correctly redirected at the other side of the tunnel.

Traffic that is passed to this local port will be sent to the remote host. From there, the SOCKS protocol will be interpreted to establish a connection to the desired end location. This set up allows a SOCKS-capable application to connect to any number of locations through the remote server, without multiple static tunnels.

To establish the connection, we will pass the -D flag along with the local port where we wish to access the tunnel. We will also use the -f flag, which causes SSH to go into the background before executing and the -N flag, which does not open a shell or execute a program on the remote side.

For instance, to establish a tunnel on port "7777", you can type:

	ssh -f -N -D 7777 username@remote_host

#### tunnleing remotely

Configuring Remote Tunneling to a Server

SSH connections can be used to tunnel traffic from ports on the local host to ports on a remote host.

In a remote tunnel, a connection is made to a remote host. During the creation of the tunnel, a remote port is specified. This port, on the remote host, will then be tunneled to a host and port combination that is connected to from the local computer. This will allow the remote computer to access a host through your local computer.

This can be useful if you need to allow access to an internal network that is locked down to external connections. If the firewall allows connections out of the network, this will allow you to connect out to a remote machine and tunnel traffic from that machine to a location on the internal network.

To establish a remote tunnel to your remote server, you need to use the -R parameter when connecting and you must supply three pieces of additional information:

    The port where the remote host can access the tunneled connection.
    The host that you want your local computer to connect to.
    The port that you want your local computer to connect to.

These are given, in the order above (separated by colons), as arguments to the -R flag. We will also use the -f flag, which causes SSH to go into the background before executing and the -N flag, which does not open a shell or execute a program on the remote side.

For instance, to connect to example.com on port 80 on our local computer, making the connection available on our remote host on port 8888, you could type:

	ssh -f -N -R 8888:example.com:80 username@remote_host

Now, on the remote host, opening a web browser to 127.0.0.1:8888 would allow you to see whatever content is at example.com on port 80.

A more general guide to the syntax is:

	ssh -R remote_port:site_or_IP_to_access:site_port username@host

Since the connection is in the background, you will have to find its PID to kill it. You can do so by searching for the port you forwarded:

	ps aux | grep 8888


#### local tunneling

Configuring Local Tunneling to a Server

SSH connections can be used to tunnel traffic from ports on the local host to ports on a remote host.

A local connection is a way of accessing a network location from your local computer through your remote host. First, an SSH connection is established to your remote host. On the remote server, a connection is made to an external (or internal) network address provided by the user and traffic to this location is tunneled to your local computer on a specified port.

This is often used to tunnel to a less restricted networking environment by bypassing a firewall. Another common use is to access a "localhost-only" web interface from a remote location.

To establish a local tunnel to your remote server, you need to use the -L parameter when connecting and you must supply three pieces of additional information:

    The local port where you wish to access the tunneled connection.
    The host that you want your remote host to connect to.
    The port that you want your remote host to connect on.

These are given, in the order above (separated by colons), as arguments to the -L flag. We will also use the -f flag, which causes SSH to go into the background before executing and the -N flag, which does not open a shell or execute a program on the remote side.

For instance, to connect to example.com on port 80 on your remote host, making the connection available on your local machine on port 8888, you could type:

	ssh -f -N -L 8888:example.com:80 username@remote_host

Now, if you point your local web browser to 127.0.0.1:8888, you should see whatever content is at example.com on port 80.

A more general guide to the syntax is:

	ssh -L your_port:site_or_IP_to_access:site_port username@host

Since the connection is in the background, you will have to find its PID to kill it. You can do so by searching for the port you forwarded:

	ps aux | grep 8888