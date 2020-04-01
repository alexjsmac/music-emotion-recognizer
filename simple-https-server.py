#!/usr/bin/env python3

# Ported to Python 3 by Telmo "Trooper" (telmo.trooper@gmail.com)
#
# Original code from:
# http://www.piware.de/2011/01/creating-an-https-server-in-python/
# https://gist.github.com/dergachev/7028596
#
# To generate a certificate use:
# openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

separator = "-" * 80

httpd = HTTPServer(("localhost", 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile="./server.pem", server_side=True)

print(separator)
print("Server running on https://localhost:4443")
print(separator)

httpd.serve_forever()
