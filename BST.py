class Node:
  
  def __init__(self, value = None):
    self.value = value
    self.parent = None
    self.right = None
    self.left = None

class BST:
  
  def __init__(self):
    self.head = Node()
  
  def isEmpty(self):
    return self.head.value == None
  
  def insert(self, value):
    if self.isEmpty():
      self.createNode(value, self.head)
    else:
      self.insertAux(value, self.head)
  
  def insertAux(self, value, current):
    if self.isNIL(current):
      self.createNode(value, current)
    else:
      if current.value > value:
        self.insertAux(value, current.left)
      else:
        self.insertAux(value, current.right)
  
  def search(self, value):
    return self.searchAux(value, self.head)
  
  def searchAux(self, value, current):
    if self.isNIL(current):
      return current
    elif value == current.value:
      return current
    else:
      if current.value > value:
        return self.searchAux(value, current.left)
      else:
        return self.searchAux(value, current.right)
        
  def maximum(self, node):
    return self.maximumAux(node)
  
  def maximumAux(self, current):
    if current.right.value == None:
      return current
    return self.maximumAux(current.right)
    
  def minimum(self, node):
    return self.minimumAux(node)
  
  def minimumAux(self, current):
    if current.left.value == None:
      return current
    return self.minimumAux(current.left)
    
  
  def createNode(self, value, node):
    node.value = value
    node.right = Node()
    node.right.parent = node
    node.left = Node()
    node.left.parent = node
    
  def isLeftChild(self, node):
    return node == node.parent.left
    
  def isNIL(self, node):
    return node.value == None
    
  def transplant(self, u, v):
    if self.head == u:
      self.head = v 
    elif self.isLeftChild(u):
      u.parent.left = v 
    else:
      u.parent.right = v 
    
    if not self.isNIL(v):
      v.parent = u.parent
  
  def remove(self, value):
    node = self.search(value)
    
    if self.isNIL(node.left):
      self.transplant(node, node.right)
    elif self.isNIL(node.right):
      self.transplant(node, node.left)
    else:
      sucessor = self.minimumAux(node.right)
      
      if sucessor.parent != node:
        self.transplant(sucessor, sucessor.right)
        sucessor.right = node.right
        sucessor.right.parent = sucessor
      self.transplant(node, sucessor)
      sucessor.left = node.left
      sucessor.left.parent = node
      
  def printByLevel(self):
    currentLevel = [self.head]
    while currentLevel:
      nextLevel = []
      for i in currentLevel:
        print i.value,
        if not self.isNIL(i.left):
          nextLevel.append(i.left)
        if not self.isNIL(i.right):
          nextLevel.append(i.right)
      print " "
      currentLevel = nextLevel