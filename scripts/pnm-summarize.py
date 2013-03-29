#!/usr/bin/python2

import xml.dom.minidom
from xml.dom.minidom import Node

import sys, getopt

inputfile = sys.stdin
outputfile = sys.stdout

def usage():
	print ''
	print 'generates a more human-readable output from a nmap XML output'
	print ''
	print 'usage : '
	print '  pnm-summarize.py [-i <inputfile>] [-o <outputfile>]'
	print '  pnm-summarize.py [--ifile <inputfile>] [--ofile <outputfile>]'
	print ''
	print 'if no input/output file is mentionned, the script will use standard input/output'
	print ''

def main(argv):
	global inputfile
	global outputfile
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["help","ifile=","ofile="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
	  if opt in ('-h','--help'):
		usage()
		sys.exit()
	  elif opt in ("-i", "--ifile"):
		inputfile = open(arg, 'r')
	  elif opt in ("-o", "--ofile"):
		outputfile = open(arg, 'w')


def parseXML(xml_file, res_file):
	doc = xml.dom.minidom.parse(xml_file)

	saveout = sys.stdout
	sys.stdout = outputfile

	for host_node in doc.getElementsByTagName("host") :
		if host_node.getElementsByTagName("status")[0].attributes["state"].value == "up" :
			address = ''
			for address_node in host_node.getElementsByTagName("address") :
				if address_node.attributes["addrtype"].value == "ipv4" :
					address = address_node.attributes["addr"].value
					break
			if len(address) > 0 :
				for port_node in host_node.getElementsByTagName("port") :
					portid = port_node.attributes["portid"].value
					service = port_node.getElementsByTagName("service")[0].attributes["name"].value
					print address,"	",portid,"	",service

	sys.stdout = saveout

if __name__ == "__main__":
	main(sys.argv[1:])
	parseXML(inputfile, outputfile)

