# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from logging import critical
from operator import truediv, truth
from random import randint

mena=["Alojz","Bernard","Cyril","David"]
zoznam=[]
plat=40000
max=100
class Hrdina:
    name=''
    zbroj=10
    utok=10
    obrana=10
    health=100
    vitalita=0
    sila=0
    obratnost=0
    sanca_na_zasah=50
    uhyb = 30
    critical=50

class Beast:
    def __init__(self,name,health,utok,obrana,sanca_na_zasah,uhyb,zbroj,critical):
        self.name=name
        self.health=health
        self.utok=utok
        self.obrana=obrana
        self.sanca_na_zasah = sanca_na_zasah
        self.uhyb = uhyb
        self.zbroj=zbroj
        self.critical=critical

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
        return False
def Critical(postava):
    kriticky=postava.critical
    sanca=randint(0,100)
    if sanca<=kriticky:
        return True
    else:
        return False
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
                if monstrum.zbroj>=hrdina.utok:
                    print("zbroj odrazila cely utok")
                    pass
                else:
                    if Critical(hrdina):
                        poskodenie=hrdina.utok*2
                        monstrum.health -= poskodenie - monstrum.zbroj
                        print("hrdina ma ktiricky utok a berie", poskodenie, " zbroj monstra zablokovala ", monstrum.zbroj)
                        print("monstrum ma", monstrum.health)
                    else:
                        monstrum.health -= hrdina.utok - monstrum.zbroj
                        print("hrdina utoci a berie",hrdina.utok," zbroj monstra zablokovala ",monstrum.zbroj)
                        print("monstrum ma",monstrum.health)
        else:
            pass
        if utok_akcia(monstrum):
            if obrana_akcia(hrdina):
                pass
            else:
                if hrdina.zbroj>=monstrum.utok:
                    print("zbroj odrazila cely utok")
                    pass
                else:
                    if Critical(monstrum):
                        poskodenie=monstrum.utok*2
                        hrdina.health-=poskodenie-hrdina.zbroj
                        print("monstrum ma ktiricky utok a berie", poskodenie, " zbroj hrdinu zablokovala ",hrdina.zbroj)
                        print("monstrum ma", hrdina.health)
                    else:
                        hrdina.health-=monstrum.utok - hrdina.zbroj
                        print("monstrum utoci a berie", monstrum.utok," hrdinova zbroj zablokovala ",hrdina.zbroj)
                        print("hrdina ma ",hrdina.health)

hrdina1=Hrdina()
monstrum1=Beast("Minotaurus",500,50,50,40,10,0,1)
zoznam.append(monstrum1)
monstrum2=Beast("Harpyja",350,30,20,50,30,0,3)
zoznam.append(monstrum2)
monstrum3=Beast("Titan",1000,50,10,30,2,0,0)
zoznam.append(monstrum3)
hrdina1.name=random.choice(mena)
skill_point=5
print(hrdina1.name)
print("Máš",skill_point," bodddov na vylepšie, aké vylepšie by si chcel?(vitalita,sila,obratnost,")
#vylepsenie(skill_point)
super=random.choice(zoznam)
print(super.name)
suboj(hrdina1,super)
'''for i in zoznam:
    print(i.meno)'''