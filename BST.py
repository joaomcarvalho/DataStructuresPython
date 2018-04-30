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
    if current.value == None:
      self.createNode(value, current)
    else:
      if current.value > value:
        self.insertAux(value, current.left)
      else:
        self.insertAux(value, current.right)
  
  def search(self, value):
    return self.searchAux(value, self.head)
  
  def searchAux(self, value, current):
    if current == None:
      return -1
    elif value == current.value:
      return current.value
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