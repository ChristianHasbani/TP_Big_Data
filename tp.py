import csv
import matplotlib.pyplot as plt
import matplotlib.image as img

data = []

with open('dataset\optdigits.tra', 'r') as f:
    file = csv.reader(f,delimiter=',')
    for line in file:
        matLine = []
        for ligneNumber in range(0,8):
            ligne = []
            for element in range(ligneNumber*8,ligneNumber*8+8):
                #print("ligneNumber*8 = ",ligneNumber*8,"ligneNumber*8+8 = ",ligneNumber*8+8)
                ligne.append(int(line[element]))
                #print("ligne = ", ligne)
            matLine.append(ligne)
            #print("matLine = ",matLine)
        data.append(matLine)
        #print("data = ",data)

print("data = ",data) 
print("data[0] = ", data[0])
plt.imshow(data[6])
plt.show()