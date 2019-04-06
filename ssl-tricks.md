## ssl - tls cert creating and verification

### Good links

http://movingpackets.net/2015/03/16/five-essential-openssl-troubleshooting-commands/
https://www.opsdash.com/blog/check-ssl-certificate.html

	openssl verify -verbose -x509_strict -CAfile *.example.com.pem -CApath nosuchdir *.example.com.pem

### Great Tools

https://testssl.sh/

#### openssl tricks to check certs and capture stuff like ocsp stapling

https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html

#### Checking certs

	curl --insecure -v https://www.example.com 2>&1 | awk 'BEGIN { cert=0 } /^\* Server certificate:/ { cert=1 } /^\*/ { if (cert) print }'

https://www.ssllabs.com/ssltest/
https://docs.acquia.com/article/verifying-validity-ssl-certificate

openssl s_client -connect example.com:443
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -showcerts -connect example.com:443
openssl s_client -showcerts -connect example.com:443
curl --insecure -v https://www.google.com 2>&1 | awk 'BEGIN { cert=0 } /^\* SSL connection/ { cert=1 } /^\*/ { if (cert) print }'
curl --insecure -v https://example.com 2>&1 | awk 'BEGIN { cert=0 } /^\* SSL connection/ { cert=1 } /^\*/ { if (cert) print }'
curl --insecure -v https://example.com

nmap -p 443 --script ssl-cert example.com
nmap -p 443 --script ssl-cert example.com

curl --insecure -v https://example.com

#### Check cert chains

Online tool to verify certificate chains

* https://tools.keycdn.com/ssl

#### check your key and csr and crt

https://www.sslshopper.com/article-most-common-openssl-commands.html

#### change the format of your openssl crts

https://www.sslshopper.com/article-most-common-openssl-commands.html
https://knowledge.digicert.com/solution/SO26630.html

#### check a csr, crt and key

Check a Certificate Signing Request (CSR)

	openssl req -text -noout -verify -in CSR.csr

Check a private key

	openssl rsa -in privateKey.key -check

Check a certificate

	openssl x509 -in certificate.crt -text -noout

Check a PKCS#12 file (.pfx or .p12)

	openssl pkcs12 -info -in keyStore.p12

#### generate a new csr from a new key

	openssl req -new -newkey rsa:2048 -nodes -keyout private/www.example.com.key -out csr/www.example.com.csr

#### Alertnative - creating a star * certificate

	openssl genrsa -out *.example.com.key 4096

	openssl req -new -key *.example.com.key -out *.example.com.csr

	openssl req -new -newkey rsa:2048 -nodes -keyout *.example.com.key -out *.example.com.csr


#### Links to other pages

http://nginx.org/en/docs/http/configuring_https_servers.html

https://www.digicert.com/ssl-certificate-installation-nginx.htm

https://www.nginx.com/resources/admin-guide/nginx-ssl-termination/

https://www.digicert.com/ssl-certificate-installation-nginx.htm

https://www.example.com/blog/2014/10/30/openssl-csr-with-alternative-names-one

https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs


#### generate a new key, csr and crt good read

https://support.rackspace.com/how-to/generate-a-csr-with-openssl/

	openssl req -new -sha256 -key www.exampleeconomics.org.2018.key -out www.exampleeconomics.org.2018.csr

#### basic setup

To generate a CSR on Nginx, please do the following:

Login to your server via your terminal client (ssh). The first step will be generating the private key.  At the prompt, type:

	openssl genrsa -out [private-key-file.key] 2048
 
Once the private key has been generated, run the command below to generate the CSR.

	openssl req -new -key [private-key-file.key] -out [CSR-file.txt] 

- Country Name (C): Use the two-letter code without punctuation for country, for example: US or CA.
- State or Province (S): Spell out the state completely; do not abbreviate the state or province name, for example: Oregon.
- Locality or City (L): The Locality field is the city or town name, for example: Eugene.
- Organization (O): If your company or department has an &, @, or any other symbol using the shift key in its name, you must spell out the symbol or omit it to enroll, for example:  XY & Z Corporation would be XYZ Corportation or XY and Z Corportation.
- Organizational Unit (OU): This field is the name of the department or organization unit making the request.
- Common Name (CN): The Common Name is the Host + Domain Name.  For example www.bbtest.net or secure.bbtest.net
- Optional Fields:  When promted, please do not enter your email address, challenge password or an optional company name when generating the CSR.  Pressing Enter/Return will leave these fields blank.
Your CSR file will then be created.
Proceed to Enrollment and paste the CSR in the enrollment form when required.


#### Simple bash script

```bash
#!/bin/bash
# BEGIN - OpenSSL inline CFG file
openssl req -new -sha256 -nodes -out example.com.csr -newkey rsa:4096 -keyout example.com.key -config <(
cat <<-EOF
[req]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C=US
ST=New York
L=Rochester
O=example.com.com
emailAddress=hosting@example.com
CN=example.com

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1=example.com
DNS.2=www.example.com
EOF
)
# END - OpenSSL inline CFG file
```

