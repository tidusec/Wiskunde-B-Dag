def verschilstap(getallen):
    verschillen = []
    for i in range(len(getallen) - 1):
        verschil = getallen[i] - getallen[i + 1]
        verschillen.append(abs(verschil))
    verschillen.append(abs(getallen[-1] - getallen[0]))

    return verschillen


p = 0
q = 0
r = 0
s = 0

longesttillecyclisch = 0
longesttillecyclischset = []
time = 0

while True:
    getallen = [p, q, r, s]
    #print(getallen)
    previous = []
    length = 0
    for i in range(1000):
        length += 1
        getallen = verschilstap(getallen)
        previous.append(getallen)
        #print(getallen)
        #print(length)
        if getallen in previous[:-1]:
            if length > longesttillecyclisch:
                longesttillecyclisch = length
                longesttillecyclischset = [p, q, r, s]
            #print(getallen)
            #print("Cyclisch" + str(length))
            break
        #print(getallen)

    if p > 100 or q > 100 or r > 100 or s > 100:
        break
    else:
        # make it do all the possible combinations
        # also [91, 1, 0, 1]
        #print(p, q, r, s)
        if p == 100:
            p = 0
            q += 1
        elif q == 100:
            q = 0
            r += 1
            print(p, q, r, s)
        elif r == 100:
            r = 0
            s += 1
        else:
            p += 1


print(longesttillecyclisch)
print(longesttillecyclischset)