This directory contains all scripts and resources files used by the project.
It is recommended not to save any result file in this folder during testing.

You can access all commands from this folder using relative or absolute path.
It is also possible to "install" these executable copying them in a dedicated folder and adding it to the $PATH variable.

Names of the commands included in this project start with the "pnm-" suffix.

This is a summary of different commands' utility :

# pnm-ports-hits :
	counts the number of hosts for each open port
	it generates a text-file (in tabulation separated values format) with a HTML page for a graphical visualization in specified folder
	input : nmap XML file or nmap XML output from pipe

# pnm-extract-cpe.py :
	extract the CPE (Common Plateform Enumeration) names in order to use them with CVE-SEARCH : python3 ./search.py -p <a_cpe_name>
	it generates a tabulation separated values formatted output
	input : nmap XML file or nmap XML output from pipe
	output : a TSV text file (it will be overwritten if it exists) or the standard output

# pnm-extract-mac.py :
	extract MAC addresses in order to spoof them or produce statistics
	it generates a tabulation separated values formatted output :
		- the list of couples <MAC address	vendor (if known)>
		- the number of MAC addresses for each vendor if the --group-by-vendor argument is passed
	input : nmap XML file or nmap XML output from pipe
	output : a TSV text file (it will be overwritten if it exists) or the standard output



possibles improvements :
- replace the python xml.dom.minidom library by another to enhance performance
