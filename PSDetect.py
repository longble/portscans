# Author Michael Patlovich
# Detects a port scan
from scapy.all import *
import os
import sys
import argparse
import socket
import select
import logging
import signal #To kill the programs nicely
import time

offendersip = []
offenderstime = []
offenderstime1 = []

def action(packet):
	start = time.time()
	srcip = packet[0][1].src
	position = -1
	leng = 0
	while leng < len(offendersip):
		if str(srcip) == str(offendersip[leng]):
			position = leng
			break
		leng += 1
	if position >= 0:
		offenderstime[position] += 1
		offenderstime1[position] = time.time() - offenderstime1[position]
		if offenderstime[position] >= 15 and offenderstime1[position] < 5:
			offenderstime[position] = 0
			return 'Scanner detected. The scanner originated from host {}'.format(packet[0][1].src)
	elif position == -1:
		offendersip.extend([packet[0][1].src])
		offenderstime.extend([0])
		offenderstime1.extend([time.time() - start])
	
	
	

print sniff(filter="ip", prn=action)





