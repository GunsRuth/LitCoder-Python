from collections import deque

class CustomQueue:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        
    def isEmpty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
        
    def transferStack(self):
        while len(self.stack1) > 0:
            temp = self.stack1.pop()
            self.stack2.append(temp)
    
    def enqueue(self, element):
        self.stack1.append(element)
        
    def dequeue(self):
        if self.isEmpty():
            return -1
        if len(self.stack2) == 0 and len(self.stack1) > 0:
            self.transferStack()
        return self.stack2.pop()
            
    def peek(self):
        if self.isEmpty():
            return -1
        if len(self.stack2)>0:
            return self.stack2[-1]
        else:
            self.transferStack()
            return self.stack2[-1]
            
queries = input()
queue = CustomQueue()
for query in queries.split(','):
    instruction = query.split()
    if instruction[0] == '1':
        queue.enqueue(instruction[1])
    elif instruction[0] == '2':
        queue.dequeue()
    elif instruction[0] == '3':
        print(queue.peek())
                                                                                                                            