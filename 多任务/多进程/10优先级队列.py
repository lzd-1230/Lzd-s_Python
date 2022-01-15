import queue

q = queue.PriorityQueue(3)

q.put((0,"00"))
q.put((1,"11"))
q.put((2,"22"))

print(q.get())