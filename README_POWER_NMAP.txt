English :
---------
Soon...

Fran�ais :
----------
PowerNmap est un outil qui permettra d'analyser les r�sultats issus du programme Nmap pour en analyser les vuln�rabilit�s.
Pour trouver facilement ces vuln�rabilit�s, l'outil se basera sur CVE-SEARCH (https://github.com/adulau/cve-search), auquel il transmettra toutes les informations en sa possession.
Si ces informations ne s'av�rent pas suffisantes, d'autres outils seront mis en place pour en recueillir. Par exemple (liste non exhaustive) :
- interrogation des ports d�tect�s comme ouvert et :
	- analyse du message d'accueil (service et version du protocole utilis�)
	- si pas de message d'accueil, analyse des messages d'erreur apr�s l'�mission d'un message
- ...

