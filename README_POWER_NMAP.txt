English :
---------
Soon...

Français :
----------
PowerNmap est un outil qui permettra d'analyser les résultats issus du programme Nmap pour en analyser les vuln�rabilit�s.
Pour trouver facilement ces vulnérabilités, l'outil se basera sur CVE-SEARCH (https://github.com/adulau/cve-search), auquel il transmettra toutes les informations en sa possession.
Si ces informations ne s'avèrent pas suffisantes, d'autres outils seront mis en place pour en recueillir. Par exemple (liste non exhaustive) :
- interrogation des ports détectés comme ouvert et :
- analyse du message d'accueil (service et version du protocole utilisé)
- si pas de message d'accueil, analyse des messages d'erreur après l'�mission d'un message
- ...

Démarche :
----------
Exécution de nmap sur un réseau ou une machine, avec sortie enregistrée dans un fichier XML
Analyse du fichier XML en utilisant l'utilitaire xmllint de la bibliothèque portable libxml
Utilisation de CVE-Search avec les mots clés trouvéé dans le fichier XML

Implémentation :
----------------
L'outil sera implémenté en Bash
Il pourra éventuellement prendre en argument le nom du fichier à parser (déjà généré par nmap) ou appeler directement nmap avec quelques param�tres pr�d�finis
L'outil peut aussi sauvegarder son interpr�tation du XML dans un format plus lisible

Retour graphique :
-------------------

Nous allons modifier la forme du fichier xml nous utiliserons ensuite le projet "d3" de "mbostock" afin de modéliser les données
