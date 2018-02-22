score = 0
ecran = "menu"
coll = False
start = False
class vaisseau:
    def __init__(self, canva):
        self.canva = canva
        self.id = canva.create_polygon(190, 485, 210, 485, 210, 475, 205, 475, 205, 470, 195, 470, 195, 475, 190, 475, fill="grey")
        canva.bind_all("<KeyPress-Right>", self.droite)
        canva.bind_all("<KeyPress-Left>", self.gauche)

    def droite(self, evt):
        if ecran == "menu":
            self.canva.move(self.id, 5, 0)
        else:
            print("Vous ne pouvez pas interagir avec le vaisseau lorsque vous avez perdu.")

    def gauche(self, evt):
        if ecran == "menu":
            self.canva.move(self.id, -5, 0)
        else:
            print("Vous ne pouvez pas interagir avec le vaisseau lorsque vous avez perdu.")

    def dessiner(self):
        global ecran
        truc = canva.coords(self.id)
        if truc[0] <= 0:
            self.canva.move(self.id, 5, 0)
        elif truc[2] >= 400:
            self.canva.move(self.id, -5, 0)
        if ecran == "menu":
            tk.after(1, az.dessiner)

class asteroide:
    def __init__(self, canva):
        self.a = 0
        self.canva = canva
        self.emplacement = [nb for nb in range(0, 400)]
        random.shuffle(self.emplacement)
        self.id = self.canva.create_rectangle(self.emplacement[0], 10, self.emplacement[0]+10, 20, state="hidden", fill="grey")
        self.xi = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        random.shuffle(self.xi)
        self.x = self.xi[0]
        self.yi = [2, 3, 4, 5, 6]
        random.shuffle(self.yi)
        self.y = self.yi[0]
        
    def start(self):
        self.canva.itemconfig(self.id, state="normal")
        tk.after(1, self.dessiner())
        tk.after(1, self.collision())
        
    def dessiner(self):
        global aff_score
        self.truc = canva.coords(self.id)
        if self.truc[0] <= 0:
            self.xi = [2, 3, 4, 5]
            random.shuffle(self.xi)
            self.x = self.xi[0]
        elif self.truc[2] >= 400:
            self.xi = [-4, -3, -2, -5]
            random.shuffle(self.xi)
            self.x = self.xi[0]
        if self.truc[1] >= 500:
            global score
            score += 1
            canva.itemconfig(aff_score, text="votre score est %s." % score)
            self.a = 1
        if self.a == 0:
            if ecran == "menu":
                self.canva.move(self.id, self.x, self.y)
                tk.after(50, self.dessiner)
                
    def name(self, name):
        self.name = name

    def gname(self):
        return self.name
            
    def collision(self):
        global ecran
        global coll
        self.truc = canva.coords(self.id)
        truc_v = canva.coords(az.id)
        if self.truc[2] <= truc_v[2] and self.truc[2] >= truc_v[0] or self.truc[0] <= truc_v[2] and self.truc[0] >= truc_v[0]:
            if self.truc[3] <= truc_v[1] and self.truc[3] >= truc_v[9] or self.truc[1] <= truc_v[1] and self.truc[0] >= truc_v[9]:
                self.d = True
                ecran = "gamemover"
                canva.itemconfig(aff_score, state="hidden")
                canva.itemconfig(aff_scoreg, state="normal", text="Votre score est %s" % score)
                canva.itemconfig(aff_gameov, state="normal")
        if self.a == 1:
            self.canva.delete(self.id)
            ast_ref(self.name)
        if ecran == "menu" and self.a != 1:
            tk.after(1, self.collision)
        
            
from tkinter import *
import time
import random
tk = Tk()
canva = Canvas(tk, width=400, height=500, bg="black")
canva.pack()
tk.title("Pilot of the space")
tk.resizable()
aff_gameov = canva.create_text(175, 250, text="Game over", fill="yellow", state="hidden", font=("Helvetica", 20))
aff_scoreg = canva.create_text(175, 350, text="Votre score est %s" % score, fill="yellow", state="hidden", font=("Helvetica", 10))
liste_ast = []
asto = liste_ast.append
az = 0
nbr_dast = 30
for i in range(nbr_dast):
    asto(asteroide(canva))
    liste_ast[i].name(i)
    

    
def ast_ref(name1):
    liste_ast[name1] = (asteroide(canva))
    liste_ast[name1].name(name1)
    liste_ast[name1].start()
aff_score = canva.create_text(40, 40, text="votre score est %s." % score, state="hidden", fill="yellow")
canva.create_rectangle(100, 200, 105, 205, fill="white")
canva.create_rectangle(200, 364, 205, 369, fill="white")
canva.create_rectangle(375, 123, 380, 128, fill="white")
canva.create_rectangle(137, 137, 142, 142, fill="white")
canva.create_rectangle(234, 256, 239, 261, fill="white")
canva.create_rectangle(256, 357, 261, 362, fill="white")
canva.create_rectangle(100, 100, 105, 105, fill="white")
canva.create_rectangle(200, 50, 205, 55, fill="white")
canva.create_rectangle(120, 283, 125, 288, fill="white")
canva.create_rectangle(390, 100, 395, 105, fill="white")
canva.create_rectangle(390, 200, 395, 205, fill="white")
canva.create_rectangle(50, 385, 55, 390, fill="white")
canva.create_rectangle(23, 276, 28, 281, fill="white")
titre = canva.create_text(200, 150, text="-- Pilot of the Space --", fill="yellow", font=("Helvetica", 30))
indication = canva.create_text(200, 200, text="Clic To Start", fill="yellow", font=("Helvetica", 15))
creator = canva.create_text(200, 390, text="**** CodiNaruto ****", fill="yellow", font=("Helvetica", 9))
def start_all(evt):
    global start
    if start == False:
        global liste_ast
        global az
        canva.itemconfig(titre, state="hidden")
        canva.itemconfig(indication, state="hidden")
        for i in range(0, 96):
            canva.move(creator, 0, -5)
            tk.update()
            time.sleep(0.03)
        canva.itemconfig(creator, state="hidden")
        canva.move(creator, 0, 480)
        canva.itemconfig(aff_score, state="normal")
        az = vaisseau(canva)
        tk.after(1, az.dessiner)
        for i in range(nbr_dast):
            liste_ast[i].start()
        start = True


canva.bind_all("<Button-1>", start_all)
tk.mainloop()
