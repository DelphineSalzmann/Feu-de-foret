# Incendies en foret !
## Name
Propagation des feux de forêts

## Membres du projet

GAZZEH Hamdi
LOCK Julian
OIKNINE Nathan
SALZMANN Delphine


## Description

Les feux de forêts sont devenus des phénomènes récurrents et extrêmement violents. Il suffit de considérer les incendies dévastateurs en Californie, en Australie et même en France. Afin de lutter contre ces catastrophes, il convient de comprendre la propagation des feux et les modéliser.
Vous vous retrouvez face à un paysage constitué de végétaux, de rochers et d'habitation. Vous pouvez fixer la direction du vent et l'endroit du départ de feu pour ensuite étudier la propagation du feu jusqu'à stabilisation. Etudiez l'effet de la pluie sur votre feu de foret et faites intervenir les pompiers pour endiguer l'incendie.


## Installation du projet 
Ayez une version de python à jour : au moins 3.10.6

Pour avoir accès au projet entrez dans le terminal : 

git clone git@gitlab-cw3.centralesupelec.fr:delphine.salzmann/incendies-en-foret.git

Les bibliothèques numpy, random, numpy.random et tkinter seront utilisées dans ce projet.
Installez les modules nécessaires avec cette commande :

py -m pip install -r requirements.txt

Pour commencer la simulation, appelez main_simulation.py en entrant dans le terminal:

py main_simulation.py


## Prise en main de la simulation

Choisissez la direction et l'intensité du vent, puis cliquer sur RECORD WIND

Cliquer sur New Fire puis sur la case ou vous souhaiter provoquer un départ de feu

Vous pouvez faire apparaitre un nuage de pluie :  
Selectionner l'intensité puis RECORD RAIN
Placer le nuage sur la grille en cliquant sur ADD RAIN

Vous pouvez ajouter des points d'eaux avec ADD A FIREMAN

Cliquer sur NEXT STEP pour voir l'état suivant

## Règles du jeu
A une nature de case (arbre, maison, point d'eau, herbe sèche, etc...) correspond une probabilité de combustion qui est liée au matériau. La propagation du feu est modélisée donc de manière probabiliste. 

Le paysage est une matrice 3D: à une case correspond une liste [etat, nature, chaleur]

Etat de la case:
0:ras
1:en feu

Correspondance nombre-nature de la case : 
0:cendre
1:arbre
2:herbe sèche
3:maison
4:eau
5:roche

chaleur est un coefficient décrit plus bas

#Direction du vent: h, b , g, d pour haut, bas, gauche, droite
si diagonale: d'abord direction verticale puis horizontale:hg, hd, bg, hd

Effet du vent: on va le modéliser par un facteur qui dépend de sa vitesse et de sa direction.
Pour un vent de direction horizontale ( axe des x ), le facteur vaut en partant de la case en feu dans le sens des x croissants:
- 1 si la vitesse est nulle ( pas d'effet ).
- 1/p si la vitesse atteigne une vitesse maximale Vmax ( p est la probabilité que la cas brule ) --> cela implique que le feu se propage forcément et dans la direction du vent.
Ainsi si on suppose que ce facteur suit une loi affine on peut déterminer ce facteur pour chaque case. ( f = (V/Vmax)*((1-p)/p)+1 )
Pour un vent de direction horizontale ( axe des x ), le facteur vaut en partant de la case en feu dans le sens des x décroissants:
- 1 si la vitesse est nulle
- 0 si la vitesse atteigne une vitesse maximale Vmax  --> ( f= 1-V/Vmax )

#Modélisation de la pluie:
On représente la pluie par une matrice n*m dont les coefficients compris entre 0 et 1 représentent l'intensité de la pluie au niveau de la case: 0 correspond à une absence de pluie et 1 à une pluie très intense éteignant immédiatement le feu

Effet de la pluie: si la case de la foret est en feu, elle s'éteint avec comme probablilité l'intensité de la pluie sur cette case.
Sinon, elle refroidit avec cette même probabiité.

#Prise en compte d'une propagation de chaleur:
Une case est maintenant caractérisée par une liste [état, nature, chaleur] où chaleur est un entier positif. Lorsqu'une case est voisine d'un incendie, deux configurations sont possibles : 
soit elle brûle et devient rouge, 
soit elle ne brûle pas mais son coefficient de chaleur augment, elle devient orange. 

Ce coefficient de chaleur augmente la probabilité que la case brûle à la prochaine génération.
Lorsqu'une case n'est entourée d'aucun voisin en feu, elle refroidit et son coefficient de chaleur diminue. Lorsque chaleur = 0 , elle retrouve sa couleur d'origine.



