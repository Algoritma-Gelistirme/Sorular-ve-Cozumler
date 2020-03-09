sayi=int(input())
adetler=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
harfler=[]
for i in range(sayi):
    word=input()
    harf=word[0]
    if harf in harfler:
        adetler[int(ord(harf))-97]+=1
    else:
        harfler.append(harf)
liste=[]
for i in range(len(adetler)):
    if adetler[i]>4:
        liste.append(chr(i+97))
cikti=""
if len(liste)>0:
    print(cikti.join(liste))
else:
    print("inzva")
