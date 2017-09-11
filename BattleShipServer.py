# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:26:16 2017

@author: Aaron McCarthy
"""

import http.client
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import io
import sys

class Handle(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print("got POST")
        print(post_data)
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


#==============================================================================
# def connect(portNum):
#     
# 
# 
# def getSunk():
#     #TODO:
#     #scan baord for chars
#     #count chars found by type
#     #return sunk ships
#     with board open as myBoard:
#         cCount = 0
#         bCount = 0
#         rCount = 0
#         sCount = 0
#         dCount = 0
#         for line in myBoard.readLines():
#             cCount =  cCount + len(re.findall("C", line))
#             bCount =  bCount + len(re.findall("B", line))
#             rCount =  rCount + len(re.findall("R", line))
#             sCount =  sCount + len(re.findall("S", line))
#             dCount =  dCount + len(re.findall("D", line))
#             
#==============================================================================
        


if __name__ == "__main__":
	#global board, myServe, oppServe
    #if len(sys.argv) > 1:
        #portNum = sys.argv[1]
        #board = sys.argv[2]
        server_address = ('127.0.0.1', 8081)
        myServe = HTTPServer(server_address, Handle)
        myServe.serve_forever()
    #else:
        #print ("Need Port num followed by board.txt")
	
