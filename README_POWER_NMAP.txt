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

D�marche :
----------
Ex�cution de nmap sur un r�seau ou une machine, avec sortie enregistr�e dans un fichier XML
Analyse du fichier XML en utilisant l'utilitaire xmllint de la biblioth�que portable libxml
Utilisation de CVE-Search avec les mots cl�s trouv�s dans le fichier XML

Impl�mentation :
----------------
L'outil sera impl�ment� en Bash
Il pourra �ventuellement prendre en argument le nom du fichier � parser (d�j� g�n�r� par nmap) ou appeler directement nmap avec quelques param�tres pr�d�finis
L'outil peut aussi sauvegarder son interpr�tation du XML dans un format plus lisible

Retour graphique :
-------------------

Nous allons modifier la forme du fichier xml nous utiliserons ensuite le projet "d3" de "mbostock" afin de modéliser les données
