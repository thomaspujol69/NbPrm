from math import *


file = open("C://Users//tpujo//OneDrive//Desktop//nombres_1ersV2.txt", "r")

fichier = file.readlines()
J = []
for line in fichier:
  J.append(int(line[:-1]))
file.close()

I = J[len(J)-1]
#print(J)

print("Et c'est parti ! on calcule les nombres premiers à partir de "+str(I)+",\n et ce jusqu'à l'arrêt de la machine !")

while I != 0:
  I = I + 1
  A = 1
  for K in J:
    if ((I/K) == int(I/K)):
      A=0
      break
    elif (K*K > I) :
      break
  if A == 1:
    file = open("C://Users//tpujo//OneDrive//Desktop//nombres_1ersV2.txt", "a")
    J.append(I)
    file.write(str(I)+'\n')
    file.close()
    A==1

#fin du programme