# check_files_content

## Description

Ce script Python vise à comparer deux fichiers textes et à identifier les éléments manquants dans l'un des fichiers par rapport à l'autre. Il identifie également les éléments présents dans les deux fichiers et éventuellement les fautes de frappe possibles.

## Fonctionnalités

lecture_fichier(lien) :
Cette fonction prend en entrée le chemin d'accès à un fichier et retourne une liste contenant le contenu du fichier après avoir supprimé les espaces inutiles.
verification(fichier1, fichier2) :
Cette fonction prend en entrée deux fichiers textes et effectue les opérations de comparaison.
Elle identifie les éléments présents dans fichier2 mais pas dans fichier1, les éléments présents dans les deux fichiers et éventuellement les fautes de frappe possibles dans fichier1.
Les éléments manquants, présents et les fautes possibles sont stockés dans des listes globales.
Utilisation

## Exécution :
L'utilisateur est invité à saisir le nom des deux fichiers à comparer.
Le script exécute ensuite la fonction verification(fichier1, fichier2).
Affichage des résultats :
Si aucun élément n'est manquant, le script affiche "Logs complète".
Sinon, il affiche les éléments manquants, présents et les fautes possibles.
