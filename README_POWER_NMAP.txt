English :
---------
Soon...

Français :
----------
PowerNmap est un outil qui permettra d'analyser les résultats issus du programme Nmap pour en analyser les vulnérabilités.
Pour trouver facilement ces vulnérabilités, l'outil se basera sur CVE-SEARCH (https://github.com/adulau/cve-search), auquel il transmettra toutes les informations en sa possession.
Si ces informations ne s'avèrent pas suffisantes, d'autres outils seront mis en place pour en recueillir. Par exemple (liste non exhaustive) :
- interrogation des ports détectés comme ouvert et :
	- analyse du message d'accueil (service et version du protocole utilisé)
	- si pas de message d'accueil, analyse des messages d'erreur après l'émission d'un message
- ...

