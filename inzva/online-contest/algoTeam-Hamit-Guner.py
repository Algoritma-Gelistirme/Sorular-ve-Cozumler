ÜniHamit Güner, [09.03.20 19:16]
N=int(input())
name=[]
for i in range(N):
    name.append(input())

string=""
sayac=0
harfler=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in harfler:
    sayac=0
    for j in name:
        if j[0]==i:
            sayac+=1
    if sayac>4:
        string+=i

if string=="":
    print("inzva")
else:
    print(string)
