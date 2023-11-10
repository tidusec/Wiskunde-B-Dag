import itertools

def verschilstap(getallen):
    verschillen = []
    for i in range(len(getallen) - 1):
        verschil = getallen[i] - getallen[i + 1]
        verschillen.append(abs(verschil))
    verschillen.append(abs(getallen[-1] - getallen[0]))
    return tuple(verschillen)

longesttillecyclisch = 0
longesttillecyclischset = []

for p, q, r, s in itertools.product(range(101), repeat=4):
    getallen = (p, q, r, s)
    previous = set()
    length = 0
    for _ in range(1000):
        length += 1
        getallen = verschilstap(getallen)
        if getallen in previous:
            if length > longesttillecyclisch:
                longesttillecyclisch = length
                longesttillecyclischset = [p, q, r, s]
            break
        previous.add(getallen)

print(longesttillecyclisch)
print(longesttillecyclischset)