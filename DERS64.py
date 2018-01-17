class Yazýlýmcý(): #Yazýlýmcý Clasý Baþlýðý Oluþturuldu./Aþaðýda Özellikler verilecek.
    def __init__(self,isim,soyisim,maaþ,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.maaþ=maaþ
        self.diller=diller
#Buraya kadar sadece içinde oalcak özellikleri girdik.

    def bilgilerigoster(self):#Bilgileri göster fonksiyonunu ile yazýlýmcýnýn özelliklerini  görebiliriz.
        print("""
        ******************* Yazýlýmcýnýn Bilgileri *****************
        Ýsim= {}
        Soyisim= {}
        Maaþý= {}
        Bildiði diller= {}  
        ************************************************************      
        """.format(self.isim,self.soyisim,self.maaþ,self.diller))#format metodu kullandýk.


    def zam_yap(self,miktar):#Burda zamyap fonksiyonu ile maaþ'a zam yapýlabilecek.
        print("Zam yapýldý..")
        self.maaþ+=miktar
        print("Yeni Maaþ =",self.maaþ, "\n")

    def dil_ekle(self,yeni_dil):#Burda kullanýcýnýn yeni dil eklemesini saðlýyacak kodlar yer alýcak
        print("Yeni dil baþarýyla kaydedildi...", "\n")
        self.diller.append(yeni_dil)
        print("Yeni dil listeniz : ",self.diller, "\n")

#***********************************************************************************************************
#Buraya kadar CLASS iþlemlerini yaptýk.

yazilimci=Yazýlýmcý("Ömer","Akkoyun",3500,["Python","Php","Java"],)
#üstte yazilimci deðiþkene Yazýlýmcý clasýný entegre ettik içine özelliklerinide girdik.isim vsvs.

print(yazilimci.dil_ekle("HTML"))

print(yazilimci.zam_yap(520))






ÇIKTISI :

Yeni dil baþarýyla kaydedildi... 

Yeni dil listeniz :  ['Python', 'Php', 'Java', 'HTML'] 


Zam yapýldý..
Yeni Maaþ = 4020 



