English :
---------
Soon...

Français :
----------
PowerNmap est un ensemble d'outils permettant de synthétiser les résultats issus du programme Nmap pour en analyser les vulnérabilités.
Pour trouver facilement ces vulnérabilités, l'outil se basera sur CVE-SEARCH (https://github.com/adulau/cve-search), auquel il transmettra toutes les informations en sa possession.
Si ces informations ne s'avèrent pas suffisantes, d'autres outils seront mis en place pour en recueillir. Par exemple (liste non exhaustive) :
- interrogation des ports détectés comme ouvert et :
- analyse du message d'accueil (service et version du protocole utilisé)
- si pas de message d'accueil, analyse des messages d'erreur après l'émission d'un message
- ...

Démarche :
----------
Exécution de nmap sur un réseau ou une machine, avec sortie enregistrée dans un fichier XML
Interprétation du fichier XML en utilisant des scripts
# Utilisation de CVE-Search avec les mots clés trouvés dans le fichier XML
Représentation des résultats sous forme graphique

Implémentation :
----------------
Les outils seront implémentés en Bash ou en Python
Ils pourront éventuellement prendre en argument le nom du fichier à parser (déjà généré par nmap) ou lire la sortie de nmap depuis l'entrée standard
On peut aussi sauvegarder les interprétations du XML dans un format plus lisible visuellement

Représentation graphique :
--------------------------
Le fichier XML sera interprété et transformé
Nous utiliserons ensuite l'outil "d3" de "mbostock" afin de modéliser les données
