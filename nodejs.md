## nodejs

#### Good Reads

https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04


User retire.js to check for vuls
npm install -g retire


Rule 10: Audit your modules with the Node Security Platform CLI
nsp is the main command line interface to the Node Security Platform. It allows for auditing a package.json or npm-shrinkwrap.json file against the NSP API to check for vulnerable modules.

npm install nsp --global
# From inside your project directory
nsp check

Say no to sudo node app.js

Secure your Express application: Helmet for the rescue
Helmet is a series of middlewares that help secure your Express/Connect apps. Helmet helps with the following middlewares:

csp
crossdomain
xframe
xssfilter
and much more
For more info and on how to use, check out its repository: https://github.com/evilpacket/helmet.

Tools to use
npm shrinkwrap: Locks down dependency versions recursively and creates a npm-shrinkwrap.json file out of it. This can be extremely helpful when creating releases. For more info, pay NPM a visit.

retire.js: The goal of Retire.js is to help you detect the use of module versions with known vulnerabilities. Simply install with npm install -g retire. After that, running it with the retire command will look for vulnerabilities in your node_modules directory. (Also note, that retire.js works not only with node modules, but with front end libraries as well.)

