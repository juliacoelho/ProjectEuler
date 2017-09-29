dict_nb = {nb:0 for nb in range(1, 1000001)}
biggestNb = 1
biggestChain = 1

#print(dict_nb)

def collatz(nb):
    nb_ = nb
    global dict_nb
    count = 1
    while nb != 1:
        if nb < 1000001 and dict_nb[nb] != 0:
            count += dict_nb[nb] - 1
            nb = 1
        else:
            count += 1
            if nb%2 == 0:
                nb = nb/2
            else:
                nb = 1 + 3*nb
    dict_nb[nb_] = count


for key in dict_nb.keys():
    collatz(key)
    if dict_nb[key]>biggestChain:
        biggestNb = key
        biggestChain = dict_nb[key]

print (biggestNb)
