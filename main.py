# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from operator import truediv, truth
from random import randint

mena=["Alojz","Bernard","Cyril","David"]
zoznam=[]
plat=40000
max=100
class Hrdina:
    name=''
    zbroj=0
    utok=10
    obrana=10
    health=100
    vitalita=0
    sila=0
    obratnost=0
    sanca_na_zasah=50
    uhyb = 50

class Beast:
    def __init__(self,name,health,utok,obrana,sanca_na_zasah,uhyb):
        self.name=name
        self.health=health
        self.utok=utok
        self.obrana=obrana
        self.sanca_na_zasah = sanca_na_zasah
        self.uhyb = uhyb

def utok_akcia(postava):
    utok=postava.sanca_na_zasah
    if utok>=100:
        utok=100
    sanca=randint(0,100)
    if sanca<=postava.sanca_na_zasah:
        print("utoci uspesne",postava.name)
        return True
    else:
        print(postava.name,"netrafila")
        return False
def obrana_akcia(postava):
    akcia=''
    deflect=postava.obrana
    if deflect>100:
        deflect=100
    uhyb=postava.uhyb
    if uhyb>100:
        uhyb=100
    sanca_uhyb=randint(0,100)
    sanca_deflect=randint(0,100)
    if sanca_uhyb<=uhyb:
        print(postava.name," sa uhol")
        akcia='uhyb'
        return True
    elif sanca_deflect<=deflect:
        print(postava.name,"zablokoval ranu")
        akcia='deflect'
        return True
    else:
        False

def vylepsenie(body):
    while (body > 0):
        vstup = input(str)

        if vstup == "vit":
            #hrdina1.vitalita += 1
            hrdina1.health += 10
            hrdina1.obrana += 5

            body -= 1
            #print("Nová hodnota je", hrdina1.vitalita)
        elif vstup == "sila":
            #hrdina1.sila += 1
            hrdina1.utok += 5
            hrdina1.health += 5
            body -= 1
            #print("Nová hodnota je", hrdina1.sila)
        elif vstup == "obr":
            hrdina1.obrana += 5
            hrdina1.uhyb=+5
            body -= 1
            #afjlkprint("Nová hodnota je", hrdina1.obratnosť)
        else:
            print("zadal si zle, opakuj")
            continue
        print("zostalo", body, "bodov")
def suboj(hrdina,monstrum):
    while hrdina.health>0 and monstrum.health>0:
        if utok_akcia(hrdina):
            if obrana_akcia(monstrum):
                pass
            else:
                monstrum.health -= hrdina.utok
                print("hrdina utoci a berie",hrdina.utok)
                print("monstrum ma",monstrum.health)
        else:
            pass
        if utok_akcia(monstrum):
            if obrana_akcia(hrdina):
                pass
            else:
                hrdina.health-=monstrum.utok
                print("monstrum utoci a berie", monstrum.utok)
                print("hrdina ma ",hrdina.health)

hrdina1=Hrdina()
monstrum1=Beast("Minotaurus",500,50,50,40,10)
zoznam.append(monstrum1)
monstrum2=Beast("Harpyja",350,30,20,50,30)
zoznam.append(monstrum2)
monstrum3=Beast("Titan",1000,50,10,20,2)
zoznam.append(monstrum3)
hrdina1.name=random.choice(mena)
skill_point=5
print(hrdina1.name)
print("Máš",skill_point," bodddov na vylepšie, aké vylepšie by si chcel?(vitalita,sila,obratnost,")
#vylepsenie(skill_point)
#print(hrdina1)
#print(monstrum1.health)
#print(monstrum1.utok)
#print(monstrum1.obrana)

print("ahoj")
super=random.choice(zoznam)
print(super.name)
suboj(hrdina1,super)
suboj
'''for i in zoznam:
    print(i.meno)'''