class Node:
  def __init__(self, val):
    self.value = val
    self.next = None
    self.prev = None

# node1 = Node(1) 
# node2 = Node(2) 
# node3 = Node(3) 

# node1.next = node2 # 1 => 2
# node2.next = node3 # 2 => 3
# print(node2.next.value) # 3

class LinkedList:
  def __init__(self, head=None):
    self.head = head

  def add(self, value):
    newNode = Node(value)
    newNode.prev = self.head
    newNode.next = self.head
    self.head = newNode

  def remove(self, value):
    current = self.head
    previous = None
    found = False

    while current and found is False:
      if current.value == value:
        found = True
      else:
        previous = current
        current = current.next

    if current is None:
      raise ValueError('not found')
    if previous is None:
      self.head = current.next
    else:
      previous.next = current.next
      previous.prev = current.prev

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next
    return count

  def isEmpty(self):
    if (self.size() == 0):
      return True
    else:
      return False
    
  def print(self):
    current = self.head
    value = str(self.head.value)

    while current.prev != None:
      current = current.prev
      value = value + ' ' + str(current.value)

    print(value)

# myList = LinkedList()

# myList.add(1)
# myList.add(2)
# myList.add(3)
# myList.remove(2)
# # 1, 3

# print(myList.head.prev.value) # 3
# print(myList.size()) # 2


class Stack:
  def __init__(self):
    self._list = LinkedList()

  def push(self, value):
    self._list.add(value)

  def pop(self):
    headValue = self._list.head.value
    self._list.remove(headValue)

  def peek(self):
    if (self._list.head == None):
      return None
    else:
      return self._list.head.value

  def isEmpty(self):
    return self._list.isEmpty()

  def size(self):
    return self._list.size()

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
# 1 2 3

myStack.pop()
# 1 2

print(myStack.peek()) # 2
print(myStack.isEmpty()) # false
print(myStack.size()) # 2


class Queue:
  def __init__(self):
    self._list = LinkedList()

  def enqueue(self, value):
    self._list.add(value)    

  def dequeue(self):
    current = self._list.head

    while current.prev != None:
      current = current.prev

    self._list.remove(current.value)

  def isEmpty(self):
    return self._list.isEmpty()

  def size(self):
    return self._list.size()

  def print(self):
    self._list.print()

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.dequeue()
myQueue.size()
myQueue.enqueue(4)

myQueue.print() # 2, 3

class Deque:
    def __init__(self):
        self._list = LinkedList()

    def addFront(self, value):
        # loop through self._list each prev node
        # at first node create new node and set newNode.next to currentNode
        current = self._list.head

        while current.prev != None:
          current = current.prev

        self._list.remove(current.value)

    def addRear(self, value):
        self._list.add(value)

    def removeFront(self):
        current = self._list.head
        while current.prev != None:
            current = current.prev

        self._list.remove(current.value)

    def removeRear(self):
        headValue = self._list.head.value
        self._list.remove(headValue)

    def isEmpty(self):
        return self._list.isEmpty()

    def size(self):
        return self._list.size()

    def print(self):
        self._list.print()

myDeque = Deque()
myDeque.addRear(1)
myDeque.addRear(3)
myDeque.addRear(2)
myDeque.removeFront()
myDeque.removeRear()
myDeque.isEmpty()
myDeque.size()
myDeque.print()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.dequeue()
myQueue.size()
myQueue.enqueue(4)

myQueue.print() # 2, 3