# ota-server
Very simple HTTPS server that can easily serve firmware Over-The-Air for ESP devices 

## Quick start
* Check config.py
* Generate your own server private key and certificate (see notes) and put them into certs/
* Put your bin file into builds/
* Run ota-server.py

## Notes
* CN is important - must be the same as your server IP or domain
* To avoid infinitive downloads (e.g. after ESP restart) - call file with DELETE method - its name will be renamed to the xxx.old
