isimSayisi =(int)(input())
isimListe=[]
ilkHarf=[]
harfKontrol=[]

sayac=0
sayac2=0

for i in range(isimSayisi):
    isim = input()
    isimListe += isim.split()

isimListe.sort()

for i in range(isimSayisi):
    ilkHarf += isimListe[i][0]
    sayac = (int)(ilkHarf.count(isimListe[i][0]))
    if sayac >= 5:
        harfKontrol+=isimListe[i][0]
        sayac2=1
a=sorted(harfKontrol)

b=set(harfKontrol)
c=list(b)
c.sort()
print("".join(c),end="")

if sayac2!=1:
    print("inzva")
