# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:42:19 2017

@author: Aaron McCarthy
"""

import http.client
import http.server
#import sys

#def fire (fireX, fireY, boi):
#    #TODO:
#    #send packet to ipnum on port portNum with coordinates
#    
#    #tell server to mark on board.txt where you fired
#    #get packet back and tell user hit, miss, or sink
#
#def printMyBoard():
#    print("-- Your board --")
#    #TODO:
#    #send packet of print myBoard to 127.0.0.1
#    #print payload of response
#    
#    
#def printTheirBoard():
#    print("-- Their board --")
#    #TODO:
#    #send packet of print otherBoard to 127.0.0.1
#    #print payload of response

if __name__ == "__main__":
    global myServer, oppServer
    print("boi")
	#if len(sys.argv) not == 5:
    #if len(sys.argv) == 0:     
        #ipNum = sys.argv[1]
        #portNum = sys.argv[2]
        #fireX = sys.argv[3]
        #fireY = sys.argv[4]
    print("man")
    myServer = http.client.HTTPConnection('127.0.0.1', 8081)
    print("man")
    myServer.request("GET", '127.0.0.1')
    print("man")
    response = myServer.getresponse()
    print("man")
    print(response.read())
        #oppserver = http.client.HTTPConnection(ipNum, portNum)
        #oppServer = http.client.HTTPConnection(127.0.0.1, 8080)
        #fire(fireX, fireY, oppServer)
        #printMyBoard()
        #printTheirBoard()
    #else:
        #print ("Need IP, port num, x coordinate, and y coordinate")
	