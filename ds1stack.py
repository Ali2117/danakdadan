import time
class stack:
    def __init__ (self):
        self.items=[]
    def isEmpty (self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size (self):
        return len(self.items)
    def display (self):
        return (self.items)
s=stack()
print(s.isEmpty())
print("push oprations")
s.push(12)
s.push(11)
s.push(13)
print(s.display())
print("size",s.size())
print(s.pop())
print(s.pop())
print(s.display())
print("size",s.size())

        