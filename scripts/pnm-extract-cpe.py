#!/usr/bin/python2

import xml.dom.minidom
from xml.dom.minidom import Node

import sys, getopt

inputfile = sys.stdin
outputfile = sys.stdout

def usage():
   print ''
   print 'extract CPE (Common Platform Enumeration) names from a nmap XML output with the number of occurences for each entry'
   print ''
   print 'usage : '
   print '  cpe_extract.py [-i <inputfile>] [-o <outputfile>]'
   print '  cpe_extract.py [--ifile <inputfile>] [--ofile <outputfile>]'
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
	cpe_count = {}
	
	for cpe_node in doc.getElementsByTagName("cpe") :
	  for cpe_node_child in cpe_node.childNodes :
		if cpe_node_child.nodeType == Node.TEXT_NODE :
		   cpe = cpe_node_child.data[5:]
		   if cpe_count.has_key(cpe) :
		      cpe_count[cpe]=1+cpe_count[cpe]
		   else :
		      cpe_count[cpe]=1

	saveout = sys.stdout
	sys.stdout = outputfile

	for cpe in cpe_count.keys() :
	   print cpe_count[cpe], "	", cpe
		
	sys.stdout = saveout
		
if __name__ == "__main__":
   main(sys.argv[1:])
   parseXML(inputfile, outputfile)

