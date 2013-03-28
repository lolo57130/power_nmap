#!/usr/bin/python2

import xml.dom.minidom
from xml.dom.minidom import Node

import sys, getopt

inputfile = sys.stdin
outputfile = sys.stdout
group_by_vendor = 0

def usage():
	print ''
	print 'extract MAC addresses (and associated vendor) from a nmap XML output'
	print ''
	print 'usage : '
	print '  pnm-extract-mac.py [-i <inputfile>] [-o <outputfile>] [-g]'
	print '  pnm-extract-mac.py [--ifile <inputfile>] [--ofile <outputfile>] [--group-by-vendor]'
	print ''
	print 'if no input/output file is mentionned, the script will use standard input/output'
	print 'the group-by-vendor option will count occurences of MAC addresses for each vendor'
	print ''

def main(argv):
	global inputfile
	global outputfile
	global group_by_vendor
	try:
		opts, args = getopt.getopt(argv,"hi:o:g",["help","ifile=","ofile=","group-by-vendor"])
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
	  elif opt in ("-g", "--group-by-vendor"):
		group_by_vendor = 1


def parseXML(xml_file, res_file):
	doc = xml.dom.minidom.parse(xml_file)

	saveout = sys.stdout
	sys.stdout = outputfile

	vendor_count = {}

	for address_node in doc.getElementsByTagName("address") :
		if address_node.attributes["addrtype"].value == "mac" :
			if address_node.attributes.has_key("vendor") :
				vendor = address_node.attributes["vendor"].value
			else :
				vendor = 'unknow'
			if not group_by_vendor :
				print address_node.attributes["addr"].value, "	", vendor
			else :
				if vendor_count.has_key(vendor) :
					vendor_count[vendor]=1+vendor_count[vendor]
				else :
					vendor_count[vendor]=1
	
	if group_by_vendor :
		for vendor in vendor_count.keys() :
			print vendor_count[vendor], "	", vendor
	
	sys.stdout = saveout

if __name__ == "__main__":
	main(sys.argv[1:])
	parseXML(inputfile, outputfile)

