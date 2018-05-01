class Node:
	def __init__(self, endOfWord = False):
		self.children = {}
		self.end_of_word = endOfWord

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		current = self.root
		for i in word:
			if i in current.children:
				current = current.children[i]
			else:
				current[i] = Node()
				current = curret[i]
		current.end_of_word = True

	def search(self, word):
		current = self.root
		for i in word:
			if i in current.children:
				current = current.children[i]
			else:
				return False
		
		return current.end_of_word