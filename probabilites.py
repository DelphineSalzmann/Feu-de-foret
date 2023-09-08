# la probabilité qu'une case soit contaminé par le feu suivant sa nature :
'Correspondance nombre-nature de la case : 0:cendre, 1:arbre, 2:herbe sèche, 3:maison, 4:eau, 5:roche'

probabilité_de_combustion = {
    0: 0,
    1: 0.5,
    2: 0.7,
    3: 0.4,
    4: 0,
    5: 0.1
}

# la probabilité qu'une case contaminé s'éteigne suivant sa nature :

probabilité_feu_eteint = {
    0: 1,
    1: 0.3,
    2: 0.8,
    3: 0.2,
    4: 1,
    5: 1
}

# fonction donnant le facteur du vent suivant la direction horizontale (x) vers les x croissants (de gauche vers la droite) :

"V=(Vx,Vy) : la vitesse du vent"
"Vmax : la vitesse à partir de la quelle le feu se propage forcément"


def fact_vent_x_plus(V, Vmax, nature_case):
    p = probabilité_de_combustion[nature_case]
    if p == 0:
        return 0
    if abs(V[0]) >= Vmax:
        return 1/p
    return ((abs(V[0])/Vmax)*((1-p)/p)+1)

# fonction donnant le facteur du vent suivant la direction des x décroissants :


def fact_vent_x_moins(V, Vmax, nature_case):
    if abs(V[0]) >= Vmax:
        return 0
    return (1-abs(V[0])/Vmax)

# fonction donnant le facteur du vent suivant la direction des y croissants (du bas vers le haut) :


def fact_vent_y_plus(V, Vmax, nature_case):

    p = probabilité_de_combustion[nature_case]
    if p == 0:
        return 0
    if abs(V[1]) >= Vmax:
        return 1/p
    return ((abs(V[1])/Vmax)*((1-p)/p)+1)

# fonction donnant le facteur du vent suivant la direction des y décroissants :


def fact_vent_y_moins(V, Vmax, nature_case):
    if abs(V[1]) >= Vmax:
        return 0
    return (1-abs(V[1])/Vmax)
