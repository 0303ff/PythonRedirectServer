from http.server import BaseHTTPRequestHandler, HTTPServer
#import ssl
import os
from concurrent.futures import ThreadPoolExecutor


HardFile = "url.txt"
URLDict = {}

def extractURLS(URLFile):
    URLDict.clear()
    for line in URLFile:
        url = line.strip().split('|')
        URLDict[url[0]] = url[1]

URLS = open(HardFile,'r')
extractURLS(URLS)

def urlChecker():
    last_mod = os.path.getmtime(HardFile)
    while True:
        new_mod = os.path.getmtime(HardFile)
        if new_mod != last_mod:
            last_mod = new_mod
            URLS = open(HardFile,'r')
            extractURLS(URLS)

threads = []
hostName = "0.0.0.0"
serverPort = 8080

html_body = """
alert(document.domain)
"""

def direct(url):
    refresher = f'<head><meta http-equiv="refresh" content="0; url={url}"></head>'
    return refresher

class MyServer(BaseHTTPRequestHandler):
    def index(self):
        self.page()
        self.wfile.write(bytes(html_body, "utf-8"))
    
    def page(self):
        self.server_version = "1"
        self.sys_version = ""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self.index()
        for key in URLDict.keys():
            if self.path == "/"+str(key):
                self.page()
                self.wfile.write(bytes(direct(URLDict[key]), "utf-8")) 

    def do_POST(self):
        if self.path == "/thissuperlongstring":
            length = int(self.headers.get('Content-length', 0))
            data = self.rfile.read(length).decode()
            self.server_version = "1"
            self.sys_version = ""
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            newLink = data.split('&')
            if newLink[0] == "fukyou":
                print(newLink[1])
                f = open(HardFile, 'a')
                f.write(f'{newLink[1]}\n')
                f.close()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    #webServer.socket = ssl.wrap_socket(webServer.socket, certfile='fullchain.pem',keyfile='privkey.pem', server_side=True)
    print("Server started https://%s:%s" % (hostName, serverPort))
    try:
        with ThreadPoolExecutor(max_workers=5) as executor:
            threads.append(executor.submit(webServer.serve_forever))
            threads.append(executor.submit(urlChecker))
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")