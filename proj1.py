
import sys
myfile = open("cuccos.txt",'w')


name = input("Add meg a neved! ")
print("Üdvözöllek " +name+ "!")

kor = input("Add meg a korod! ")

lakhely = input("Add meg a lakhelyed! ")

"""jegyek = []
n = 5

for i in range(1,n+1):
  jegyek.append(i)

print(jegyek)
"""

tanulojegy = ["","","",""]
tanulojegy[0] = input("Matek év végi jegy: ")

if tanulojegy[0] > str(5) or str(1) > tanulojegy[0]:
  print("ERROR")
  exit()
else:
     pass
  
targyak = ["Matematika", "Magyar Nyelv és Irodalom", "Történelem", "Informatika"]

tanulojegy[1]= input("Magyar év végi jegy: ")

if tanulojegy[1] > str(5) or str(1) > tanulojegy[1]:
  print("ERROR")
  exit()
else:
     pass
  


tanulojegy[2]= input("Történelem év végi jegy: ")


if tanulojegy[2] > str(5) or str(1) > tanulojegy[2]:
  print("ERROR")
  exit()
else:
     pass
  
tanulojegy[3]=input("Informatika év végi jegy: ")


if tanulojegy[3] > str(5) or str(1) > tanulojegy[3]:
  print("ERROR")
  exit()
else:
     pass



atlag=sum(map(int,tanulojegy)) / len(tanulojegy)

joez = print("Neved: " +name+"\n" +"Korod: "+kor+"\n" + "Lakhelyed: " + lakhely + "\n \n \n", 
"Tárgyaid:\n" + str(targyak[0])+" " + tanulojegy[0] + "\n",                     str(targyak[1])+" " + tanulojegy[1] + "\n",
     str(targyak[2])+" " + tanulojegy[2] + "\n",
    str(targyak[3])+" " + tanulojegy[3] + "\n")

print("Átlagod: " + str(atlag))

with open('cuccos.txt', 'w') as f:
    
   print("Neved: " +name+"\n" +"Korod: "+kor+"\n" + "Lakhelyed: " + lakhely + "\n \n \n", 
"Tárgyaid:\n" + str(targyak[0])+" " + tanulojegy[0] + "\n",                     str(targyak[1])+" " + tanulojegy[1] + "\n",
     str(targyak[2])+" " + tanulojegy[2] + "\n",
    str(targyak[3])+" " + tanulojegy[3] + "\n",
     "Átlagod: " + str(atlag), file=f)


myfile.close()

kutyaaa