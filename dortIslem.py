#15.Hafta Kontrol Et!

def yazdır(metin):
    print(metin)
    
class islemler:
    def topla(a,b):
        return a+b
    def cikar(a,b):
        return a-b
    def carp(a,b):
        return a*b
    def bol(a,b):
        return a/b
    
class dosya: 
    def ekle(metin):
        f=open("test.txt","a")
        f.write(metin + "\n")
        f.close()

    def üzerineYaz(metin):
        f=open ("test.txt","w")
        f.write(metin + "\n")
        f.close()
        