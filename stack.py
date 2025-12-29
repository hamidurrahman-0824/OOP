class Stack:

  def __init__(self,items):
    self.items = items.copy
  
  def push(self,item):
    self.items.append(item)
  
  def pull(self):
    return self.items.pop(-1)

  def show(self):
    return self.items

  def peek(self):
    return self.items[-1]
s1 = Stack([])
s2 = Stack([])
for i in range(4):
  s2.push(i)
s2.push('new')
s2.pull()
print(s2.peek())
print(s2.show())
