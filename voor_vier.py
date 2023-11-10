# functie die de volgende stap in de rij geeft

def verschilstap(getallen):
    verschillen = []
    for i in range(len(getallen) - 1):
        verschil = getallen[i] - getallen[i + 1]
        verschillen.append(abs(verschil))
    verschillen.append(abs(getallen[-1] - getallen[0]))

    return verschillen


p, q, r, s = 0, 0, 0, 0

langste_aantal_stappen = 0
lijst_met_langste_aantal_stappen = []

while True:
    getallen = [p, q, r, s]
    # print(getallen)
    vorige_getallen_van_lijst = []
    length = 0
    for i in range(1000):
        length += 1
        getallen = verschilstap(getallen)
        vorige_getallen_van_lijst.append(getallen)

        if getallen in vorige_getallen_van_lijst[:-1]:
            if length > langste_aantal_stappen:
                langste_aantal_stappen = length
                lijst_met_langste_aantal_stappen_ = [p, q, r, s]
            break

    if p > 100 or q > 100 or r > 100 or s > 100:
        break
    else:
        # alle mogelijke combinaties laten doen
        if p == 100:
            p = 0
            q += 1
        elif q == 100:
            print(p, q, r, s)
            q = 0
            r += 1
        elif r == 100:
            r = 0
            s += 1
        else:
            p += 1

print(langste_aantal_stappen)
print(lijst_met_langste_aantal_stappen)
