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