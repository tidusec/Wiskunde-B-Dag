import itertools

def verschilstap(getallen):
    [zie 1.5]

longesttillecyclisch = 0
longesttillecyclischset = []

for p, q, r in itertools.product(range(101), repeat=3):
    getallen = (p, q, r)
    previous = set()
    length = 0
    for _ in range(1000):
        length += 1
        getallen = verschilstap(getallen)
        if getallen in previous:
            if length > longesttillecyclisch:
                longesttillecyclisch = length
                longesttillecyclischset = [p, q, r]
            break
        previous.add(getallen)

print(longesttillecyclisch)
print(longesttillecyclischset)