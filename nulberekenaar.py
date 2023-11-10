def verschilstap(getallen):
    verschillen = []
    for i in range(len(getallen) - 1):
        verschil = getallen[i] - getallen[i + 1]
        verschillen.append(abs(verschil))
    verschillen.append(abs(getallen[-1] - getallen[0]))

    return verschillen

getallen = [0, 4]

for _ in range(1000):
    # add a zero to the front after it is calculated and make sure the last number is 1
    getallen.insert(0, 0)
    getallen[-1] = 4
    #print(getallen)
    previous = []
    length = 0

    for i in range(1000):
        length += 1
        getallen = verschilstap(getallen)
        # print(getallen)
        previous.append(getallen)
        # if all nunbers are 0 then print it's "uitdovend" (make it for any number of numbers)
        if all(number == 0 for number in getallen):

            print("uitdovend" + "_" + str(len(getallen)))
            break

        if getallen in previous[:-1]:
            # print(getallen)
            print("Cyclisch" + "_" + str(length) + "_" + str(len(getallen)))
            break
        # print(getallen)