class Queue:
    def __init__(self, *args) -> None:
        self.data = list(args)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)
    
    def __iter__(self):
        iterator = iter(self.data)
        print("A new Iterator was created!")
        return iterator
    

for _ in range(3):
    for x in Queue(1, 2, 3):
        pass 