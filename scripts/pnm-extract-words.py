#!/usr/bin/python2

import xml.dom.minidom
from xml.dom.minidom import Node

import sys, getopt

inputfile = sys.stdin
outputfile = sys.stdout

def usage():
	print ''
	print 'extract all interesting words from a nmap XML output'
	print ''
	print 'usage : '
	print '  pnm-extract-words.py [-i <inputfile>] [-o <outputfile>]'
	print '  pnm-extract-words.py [--ifile <inputfile>] [--ofile <outputfile>]'
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

def addWord(words_count, word):
	if words_count.has_key(word) :
		words_count[word]=1+words_count[word]
	else :
		words_count[word]=1
		
def addValueIfAttributeExists(words_count, node, attribute):
	if node.attributes.has_key(attribute) :
		addWord(words_count, node.attributes[attribute].value)

def parseXML(xml_file, res_file):
	doc = xml.dom.minidom.parse(xml_file)

	words_count = {}

	for service_node in doc.getElementsByTagName("service") :
		addWord(words_count, service_node.attributes["name"].value)
		addValueIfAttributeExists(words_count, service_node, "product")
		addValueIfAttributeExists(words_count, service_node, "extrainfo")
		addValueIfAttributeExists(words_count, service_node, "ostype")
		addValueIfAttributeExists(words_count, service_node, "devicetype")

	saveout = sys.stdout
	sys.stdout = outputfile
	
	for word in words_count.keys() :
	   print words_count[word], "	", word

	sys.stdout = saveout

if __name__ == "__main__":
	main(sys.argv[1:])
	parseXML(inputfile, outputfile)

