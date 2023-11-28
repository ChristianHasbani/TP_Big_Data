import csv
import matplotlib.pyplot as plt
import matplotlib.image as img

def disp(index):
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
    print("data[0] = ", data[index])

    fig = plt.figure(figsize=(10, 7))

    fig.add_subplot(2, 2, 1) 
    plt.imshow(data[index])

    #fig.add_subplot(2, 2, 2) 
    #plt.imshow(data[0])

    plt.show()
    return (data)

def distance(index1,index2):
    with open('dataset\optdigits.tra', 'r') as f:
        file = csv.reader(f,delimiter=',')
        for i in range(0,index1):
            im1 = next(file)
        im2 = next(file)
        diff = 0
        for k in range(0,64):
            diff = diff + abs(int(im1[k])-int(im2[k]))
    return diff

disp(3)
disp(4)
print(distance(3,4000))
        