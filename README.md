# PythonRedirectServer  
HTTP Server to serve as a way to redirect links and shorten longer links.  

## Starting the server  

###### Enable SSL by uncommenting lines 2 and 78 in redirect_serv.py  

`python3 redirect_serv.py`  

## Adding and removing links  

All links are stored in `url.txt` with the key and link seperated by a `|`  
Example: `test|example.com`   

### Adding links  

#### add_url.py script:  
`python3 add_url.py -k test -u https://example.com`  

#### POST request:  
`curl -X POST --data 'fukyou' --data 'l|https://example.com' http://0.0.0.0:8080/thissuperlongstring -v`  

### Removing links  

#### add_url.py script:  
`python3 add_url.py -d test`