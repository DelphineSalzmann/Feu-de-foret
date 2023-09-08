## Sprint 0 : Réflexion
- réflexion autour de l'objectif du projet et choix de sa modélisation
- établissement des règles (nature des cases, règles de propagation, ...)
- découpage en fonctionnalités
- début rédaction du README

## Sprint 1 : Mise en place du support de propagation
- Fonctionnalité 1 : génèrer la grille de paysage sous forme matricielle en associant à chaque case une liste [etat,  nature] -->fonction grille()
- Fonctionnalité 2 :  Afficher le paysage --> fonction paysage()
- Fonctionnalité 3 : initialiser un départ de feu --> fonction depart()

## Sprint 2 : Effet du vent
- Fonctionnalité 4 : définir un facteur de vent selon sa vitesse,sa direction et qui dépend de la position de la case par rapport au feu --> fonctions fact_vent_x_plus, fact_vent_x_moins, fact_vent_y_plus, fact_vent_y_moins

## Sprint 3 : Simulation de propagation de feu
- Fonctionnalité 5 : Configurer les probabilités de combustion et d'extinction de feu liées à une case --> dictionnaires probabilite_de_combustion et probabilite_feu_eteint
- Fonctionnalité 6 : Déterminer les voisins en feu d'une case --> fonction voisins()
- Fonctionnalité 7 : Apppliquer les règles de propagation pour une case --> fonction propagation()
- Fonctionnalité 8 : Appliquer les règles de propagation à toutes les cases du paysage --> fonction generation_suivante()
- Fonctionnalité 9 : Simuler la propagation jusqu'à satabilisation de la situation --> fonction simulation()

## Sprint 4 : Interface graphique
- Fonctionnalité 10 : utiliser Tkinter pour relever un départ de feu lorsqu'on clique sur la case
- Fonctionnalité 11 : compléter l'interface Tkinter avec des boutons et une légende pour afficher les générations successives

## Sprint 5 : Effet de la chaleur
- Fonctionnalité 12 : une case est désormais caractérisée par une liste [état, nature, chaleur] où chaleur est un entier positif --> grille_c()
- Fonctionnalité 13 : une case chaude est de couleur orange --> paysage_c()
- Fonctionnalité 14 : les règles de propagation sont affinées en conséquent: à proximité du feu, le coefficient de chaleur est augmenté de 1 et sa probabilité de brûler à la génération suivante augmentée --> fonction propagation_c()
- Fonctionnalité 15 : écrire la fonction génération suivante avec ces nouvelles règles --> fonction génération_suivante_c()

## Sprint 6 : Effet de la pluie
- Fonctionnalité 16 : Générer une grille de pluie sous forme matricielle en associant à chaque case un float entre 0 et 1 représentant l'intensité de la pluie --> fonction début_pluie()
- Fonctionnalité 17 : Faire évoluer une grille de pluie sous l'effet du vent  --> fonctions évolution_pluie_vent () et évolution_pluie()
- Fonctionnalité 18 : Modifier la grille de la forêt en fonction de la pluie selon les règles suivantes:
si une case est en feu, ce feu s'éteint avec comme probabilité l'intensité de la pluie sur cette case et sinon elle devient froide --> fonction effet_pluie()



