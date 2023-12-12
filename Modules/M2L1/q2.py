from collections import deque

class CustomStack:
    def __init__(self):
        self.stack = deque()
        self.prev = None
    
    def save(self):
        self.prev = self.stack.copy()
    
    def insert(self, string):
        self.save()
        for char in string:
            self.stack.append(char)
    
    def delete(self, count):
        if len(self.stack)<count:
            return -1
        self.save()
        for i in range(count):
            self.stack.pop()
        return count
        
    def get(self, index):
        if len(self.stack)<index:
            return -1
        return self.stack[index-1]
        
    def undo():
        self.stack = self.prev.copy()
        
queries = input()
stack = CustomStack()
for query in queries.split(','):
    inst = query.split()
    if inst[0] == '1':
        stack.insert(inst[1])
    elif inst[0] == '2':
        stack.delete(int(inst[1]))
    elif inst[0] == '3':
        print(stack.get(int(inst[1])))
    elif inst[0] == '4':
        stack.undo()
                                                                                                                            