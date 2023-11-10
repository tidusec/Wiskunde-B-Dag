import threading
import queue

def verschilstap(getallen):
    verschillen = []
    for i in range(len(getallen) - 1):
        verschil = getallen[i] - getallen[i + 1]
        verschillen.append(abs(verschil))
    verschillen.append(abs(getallen[-1] - getallen[0]))
    return verschillen

def worker(q):
    global longesttillecyclisch
    global longesttillecyclischset
    while True:
        try:
            p, q_val, r, s = q.get()
            getallen = [p, q_val, r, s]
            previous = []
            length = 0
            for i in range(1000):
                length += 1
                getallen = verschilstap(getallen)
                previous.append(getallen)
                if getallen in previous[:-1]:
                    if length > longesttillecyclisch:
                        longesttillecyclisch = length
                        longesttillecyclischset = [p, q_val, r, s]
                    break
            q.task_done()
        except queue.Empty:
            break

longesttillecyclisch = 0
longesttillecyclischset = []
q = queue.Queue()

for p in range(101):
    for q_val in range(101):
        for r in range(101):
            for s in range(101):
                print(s)
                q.put((p, q_val, r, s))

for i in range(100):  # 10 worker threads
    t = threading.Thread(target=worker, args=(q,))
    t.start()

q.join()

print(longesttillecyclisch)
print(longesttillecyclischset)