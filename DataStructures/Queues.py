import queue

q=queue.Queue()

q.put("Hello")
q.put("World")
q.put("Hello")
q.put("Mars")
q.put("Pluto")

#it returns the first entered element and deletes it
# print(q.get())
# print(q.get())

while not q.empty():
    print(q.get())



#Returns by priority number, lesser is has more priority
pq = queue.PriorityQueue()

q.put(10,"Hello World")
q.put(15,"Hello Mars")
q.put(5,"Important!!!")



