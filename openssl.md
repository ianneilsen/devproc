## openssl

### Good reads

https://www.sslshopper.com/ssl-converter.html
https://www.ssllabs.com/

#### Convert pem and crt files to pkcs12 format for IIS server

	openssl pkcs12 -export -out example.com.pfx -inkey example.com_key.key -in __example_com.crt -certfile __example_com.ca-bundle

#### Convert PFX to PEM

	openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes

#### Check openssl version

openssl version

