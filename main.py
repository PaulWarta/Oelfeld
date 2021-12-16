borfeld = [                     # Hier muss das Array eingeben werden, ich habe auf eine komplizierte Eingabe Mehtodik verzichtet, funktioniert nur bei Arrays mit gleichbleibender Breite.
    [0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1]
]

def stripBorfeld (borfeld):
    array = []
    for i in borfeld:
        for j in i:
            array.append(j)
    return array
borfeld1D = stripBorfeld(borfeld)


R = []
L = []
def generateLists():
    for i in range(len(borfeld1D)):
        R.append(i)
        L.append([i])
generateLists()


print(len(borfeld1D))
def nachbarnVorhanden (position):
    neueNachbarn = []
    for i in range(len(R)):
        if R[i] == position:
            if i + 1 < len(borfeld1D) and (i + 1) % len(borfeld[0]) != 0:
                if borfeld1D[i + 1] == 1 and R[i + 1] != position:
                    neueNachbarn.append(i + 1)
            if i - 1 > -1 and (i % len(borfeld[0])) != 0:
                if borfeld1D[i - 1] == 1 and R[i - 1] != position:
                    neueNachbarn.append(i - 1)
            if i - len(borfeld[0]) > -1:
                if borfeld1D[i - len(borfeld[0])] == 1 and R[i - len(borfeld[0])] != position:
                    neueNachbarn.append(i - len(borfeld[0]))
            if i + len(borfeld[0]) < len(borfeld1D) - 1:
                if borfeld1D[i + len(borfeld[0])] == 1 and R[i + len(borfeld[0])] != position:
                    neueNachbarn.append(i + len(borfeld[0]))
    return neueNachbarn

def main(k):
    valid_fields = 0
    for i in range(len(borfeld1D)):
        if borfeld1D[i] == 1:
            while(True):
                neueNachbarn = nachbarnVorhanden(i)
                if len(neueNachbarn) == 0:
                    break
                else:
                    for j in neueNachbarn:
                        L[j] = []
                        L[i].append(j)
                        R[j] = i
                    neueNachbarn = []
    print("Diese zusammenhängenden Felder sind in der gewünschten Groeßenordnung: ")
    for f in L:
        unique = []
        for e in f:
            if e not in unique:
                unique.append(e)
        f = unique
        if len(f) >= k:
            valid_fields = valid_fields + 1
            print()
            print(f)
    print("Somit sind insegsamt " + str(valid_fields) + " Felder zu erschließen.")
        

main(4) #Hier wird k eingegeben

