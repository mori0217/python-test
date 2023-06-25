import collections
import queue

q = queue.Queue()
lq = queue.LifoQueue()
l = []
dq = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    dq.append(i)

# for _ in range(3):
    # print("FIFO queue: ", q.get())
    # print("LIFO queue: ", lq.get())
    # print("List      : ", l.pop(0))
    # print("Deque     : ", dq.popleft())

print(dq)
dq.rotate()
print(dq)
dq.rotate()
print(dq)
dq.rotate()
print(dq)
dq.extendleft("x")
dq.extend("y")
print(dq)
dq.clear()
print(dq)
