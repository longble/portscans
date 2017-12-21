# Author Michael Patlovich
# This will scan all ports given a certain IP address
import os
import sys
import argparse
import socket
import select
import logging
import signal #To kill the programs nicely
import time

s = sys.argv[1]
numports = 0
print "Scanning ports"
print "_" * 60
start = time.time()
try:
	for port in range(1,65535):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		r = sock.connect_ex((s,port))
		if r == 0:
			print "Port {} is OPEN and is used for {}".format(port, socket.getservbyport(port))
			numports += 1
		sock.close()
except socket.error:
	print "Couldnt connect to the server"
	sys.exit()
	

print "Scan finished!"


print "_" * 60
print "{} port(s) found".format(numports)
end = time.time()
print "{} seconds elapsed".format(end-start)
print "{} ports per second".format(65535/(end-start))
print "_"*60
print "Terminating normally"

