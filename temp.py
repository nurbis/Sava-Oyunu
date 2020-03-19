# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
class Silah:
    def __init__(self, isim:str, damage:int ):
        self.__isim=isim
        self.__damage=damage
        
    def vur(self, rakip):
        rakip.setCan(rakip.getCan()-self.__damage)
        self.__damage-=1
    def getIsim(self):
        return self.__isim
    def getDamage(self):
        return self.__damage
    
    
class Karakter:
    def __init__(self, can:int, silah:Silah):
        self.__can=can
        self.__silah=silah
    def getCan(self):
        return self.__can
    def setCan(self, yenican):
        self.__can=yenican
    def vur(self,rakip):
        self.__silah.vur(rakip)
    def getSilahIsim(self):
        return self.__silah.getIsim()
    def getDamage(self):
        return self.__silah.getDamage()
    
    
class Dusman(Karakter):
    def __init__(self, can:int, silah:Silah):
        super().__init__(can, silah)
        
class Oyuncu(Karakter):
    def __init__(self, can:int, silah:Silah, isim:str):
        super().__init__(can, silah)
        self.__isim=isim
    def getIsim(self):
        return self.__isim


      
dusmanlar = list()
for i in range(10):
    dusmanlar.append(Dusman(randint(30,50),Silah("Bıçak", randint(10,15))))
         
NurHERO=Oyuncu(140, Silah("Kılıç",35), "Nur")   
      
    
while True:
    print("Oyuncu: {} --- Can: {} --- Silah: {} --- Damage:{}".format(NurHERO.getIsim(), NurHERO.getCan(), NurHERO.getSilahIsim(), NurHERO.getDamage()))
    print("=======================================================================")
    for sayi, i in enumerate(dusmanlar):
        print("Dusman: {} --- Can: {} --- Silah: {} --- Damage:{}".format(sayi, i.getCan(), i.getSilahIsim(), i.getDamage()))
    secim=input("Düşman Seçiniz")
    vurulandusman=dusmanlar[int(secim)]
    NurHERO.vur(vurulandusman)
    if vurulandusman.getCan() <= 0:
        dusmanlar.remove(vurulandusman)
        if not dusmanlar:
            print("Kazandın")
            break
        if dusmanlar:
            dusmanlar[randint(0, len(dusmanlar)-1)].vur(NurHERO)
            if NurHERO.getCan() <= 0:
                print("Kaybettin")
                break

         
         
     
     
