from tkinter import *
import numpy as np
from generation import generation_suivante
from functools import partial
from random import *
from pluie import début_pluie, évolution_pluie
import time
from Chaleur import generation_suivante_c

n = 50
size = 800
cote = size // n
n_pix = n * cote  # nombre de pixels par ligne

automatic = False

automatic = False


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.size = size
        self.config = np.zeros((n, n, 3), dtype=np.uint8)
        self.pluie = np.zeros((n,n))
        self.window = Toplevel()
        self.window.title("Propagation d'un feu de forêt")
        self.creer_widgets()
        self.legende()
        self.grille()
        self.interface_vent()
        self.interface_pluie()
        self.paysage()

    def creer_widgets(self):

        self.can = Canvas(self.window, bg="white", width=size, height=size)

        for i in range(n):
            self.can.create_line(0, i * cote, n_pix, i *
                                 cote, fill='black', width=1)
            self.can.create_line(i * cote, 0, i * cote,
                                 n_pix, fill='black', width=1)

        self.can.grid()

        label_button = Label(self, text="Actions",
                             font='8c').grid(row=3, column=0)

        self.new_fire_button = Button(
            self, text="NEW FIRE", width=12, state=DISABLED, command=lambda: self.init_manuelle("feu"))
        self.new_fire_button.grid(row=4, column=0, sticky=W, pady=4)

        self.next_button = Button(
            self, text="NEXT STEP", width=12, state=DISABLED, command=lambda: self.update())
        self.next_button.grid(row=4, column=2, sticky=W, pady=4)
        self.can.grid()

        label_button = Label(self, text="Actions",
                             font='8c').grid(row=3, column=0)

        self.new_fire_button = Button(
            self, text="NEW FIRE", width=12, state=DISABLED, command=lambda: self.init_manuelle("feu"))
        self.new_fire_button.grid(row=4, column=0, sticky=W, pady=4)

        self.next_button = Button(
            self, text="NEXT STEP", width=12, state=DISABLED, command=lambda: self.update())
        self.next_button.grid(row=4, column=2, sticky=W, pady=4)

        self.pompiers_button = Button(
            self, text="ADD A FIREMAN", width=12, state=DISABLED, command=lambda: self.init_manuelle("eau"))
        self.pompiers_button.grid(row=6, column=2, sticky=W, pady=4)

        self.valider_vent_button = Button(
            self, text="RECORD WIND", width=12, command=lambda: self.wind_ok()).grid(row=6, column=0)

        self.clear_button = Button(
            self, text="RESET", width=12, command=lambda: self.reset()).grid(row=4, column=4)

        self.exit_button = Button(
            self, text="QUIT", width=12, command=quit).grid(row=6, column=4)

    def reset(self):
        self.interface_pluie()
        self.grille()
        self.paysage()
        self.value_x.set(0)
        self.value_y.set(0)

    def legende(self) :
        label = Label(self, text = "Légende", font = "8c").grid(row = 8, column = 0)
        label1 = Label(self, text = "En feu", bg = "red", width = 11).grid(row = 9, column = 0)
        label2 = Label(self, text = "Cendres", bg = "black", width = 11, fg = "white").grid(row = 9, column = 1)
        label3 = Label(self, text = "Arbre", bg = "#024701", width = 11).grid(row = 9, column = 2)
        label4 = Label(self, text = "Herbe sèche", bg =  "#55FF52", width = 11).grid(row = 10, column = 0)
        label5 = Label(self, text = "Eau", bg = "blue", width = 11).grid(row = 10, column = 1)
        label6 = Label(self, text = "Rocher", bg = "grey", width = 11).grid(row = 10, column = 2)
        label7 = Label(self, text = "Habitation", bg = "#835B07", width = 11).grid(row = 9, column = 3)
        label8 = Label(self, text = "Chaud", bg = "orange", width = 11).grid(row = 10, column = 3)


    def paysage(self):

        for i in range(n):
                for j in range(n) :
                    etat = self.config[i][j][0]
                    type = self.config[i][j][1]
                    chaleur = self.config[i][j][2]
                    
                    if etat == 1 : # l'arbre brûle
                        self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = "red")

                    elif chaleur > 0 :  # la case ne brule pas mais elle est chaude
                        self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill="orange")
                    
                    else : # l'arbre ne brûle pas ou plus
                        if type == 0 : # cendre
                            self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = "black")
                        if type == 1 : # arbre
                            self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = '#024701')
                        if type == 2 : # herbe sèche
                            self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = "#55FF52")
                        if type == 3 : # maison
                            self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = "#835B07")
                        if type == 4 : # eau
                            self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = "blue")
                        if type == 5 : # rocher
                            self.can.create_rectangle(cote * j, cote * i, cote * (j+1), cote * (i+1), fill = "grey")

                        if self.pluie[i,j] >= 0.5 : # met un disque bleu là où il pleut
                            self.can.create_oval(cote * (j+0.25), cote * (i + 0.25), cote * (j+0.75), cote * (i+0.75), fill = "blue")
                            
            
        print(self.config)

        self.can.grid()

    def grille(self):
        for i in range(n):
            for j in range(n):
                self.config[i][j][0] = 0
                self.config[i, j, 2] = 0
                a = random()
                if a < 0.06:
                    self.config[i][j][1] = 5
                elif a > 0.45:
                    self.config[i][j][1] = 1
                else:
                    self.config[i][j][1] = 2
        # A la main on modèle le paysage
        for i in range(4):
            for j in range(7):
                self.config[35+i][41+j][1] = 4
                self.config[37-i][39-j][1] = 4
                self.config[36-i][37+j][1] = 4
                self.config[38+i][35-j][1] = 4

        for i in range(3):
            for j in range(4):
                self.config[29-i][39-j][1] = 3
                self.config[32+i][30-j][1] = 3
                self.config[41+i][39-j][1] = 3
                self.config[7+j][3+i][1] = 3

    def init_manuelle(self, action):
        # size : largeur de la grille (en pixels)
        # n : nombre de cellules par ligne
        def get_pos(click):
            x, y = click.x, click.y
            num_ligne = int(y) // (size / n)
            num_colonne = int(x) // (size / n)
            x0, y0 = num_colonne * size / n, num_ligne * size / n
            x1, y1 = x0 + size / n, y0 + size / n
            if action == 'feu':
                self.config[int(num_ligne), int(num_colonne), 0] = 1
                self.can.create_rectangle(x0, y0, x1, y1, fill="red")
            elif action == 'eau':
                self.config[int(num_ligne), int(num_colonne), 0] = 0
                self.config[int(num_ligne), int(num_colonne), 1] = 4
                self.can.create_rectangle(x0, y0, x1, y1, fill="blue")
            elif action == 'pluie' :
                self.pluie = début_pluie(n, n, x=int(num_ligne), y=int(num_colonne), taille = (10,10), intensité = self.intense)
                self.can.create_oval(cote * (num_colonne+0.25), cote * (num_ligne + 0.25), cote * (num_colonne+0.75), cote * (num_ligne+0.75), fill = "blue")

  

        pos_str = StringVar()
        pos_x, pos_y = StringVar(), StringVar()
        pos_str.set("Position du clic")
        pos_x.set("x")
        pos_y.set("y")

        self.can.bind("<Button-1>", get_pos)

    def update(self):
        self.config = generation_suivante_c(
            self.config, self.pluie, (self.vent_x, self.vent_y))
        self.pluie = évolution_pluie(self.pluie, (self.vent_x, self.vent_y))
        self.paysage()

    def wind_ok(self):
        self.vent_x = int(self.entry_x.get())
        self.vent_y = int(self.entry_y.get())
        self.next_button.config(state=NORMAL)
        self.new_fire_button.config(state=NORMAL)
        self.pompiers_button.config(state=NORMAL)

    def interface_vent(self):

        label = Label(self, text='Vent', font='8c').grid(row=0, column=0)

        value_x = IntVar(self)
        scale_x = Scale(self, from_=-100, to=100, showvalue=True, label="Vent Vx :",
                        variable=value_x, tickinterval=50, orient='h', sliderlength=20)
        self.entry_x = Entry(self, textvariable=value_x)
        scale_x.grid(row=1, column=0)
        self.entry_x.grid(row=1, column=1)

        value_y = IntVar(self)
        scale_y = Scale(self, from_=-100, to=100, showvalue=True, label="Vent Vy :",
                        variable=value_y, tickinterval=50, orient='h', sliderlength=20)
        self.entry_y = Entry(self, textvariable=value_y)

        scale_y.grid(row=1, column=2)
        self.entry_y.grid(row=1, column=3)

    def rain_ok(self):
        self.intense = float(self.intensite.get())
        self.ajout_pluie_button.config(state = NORMAL)

    def interface_pluie(self):

        label = Label(self, text = 'Pluie', font = '8c').grid(row = 12, column=0)

        self.ajout_pluie_button = Button(self, text = "ADD RAIN", state = DISABLED, command = lambda : self.init_manuelle("pluie"))

        self.ajout_pluie_button.grid(row = 15, column = 0)

        self.intensite = Scale(self, label = "Intensité pluie :", from_ = 0, to_ = 1, showvalue = True, sliderlength = 30, orient = 'h', resolution=0.1)
        self.intensite.grid(row=13, column=0)

        self.valider_pluie_button = Button(self, text = "RECORD INSENSITY", command = lambda : self.rain_ok()).grid(row=13, column=1)

        



        

if __name__ == "__main__":
    app = App()
    app.title("Paramétrage")
    app.mainloop()
