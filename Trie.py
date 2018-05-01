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
				current.children[i] = Node()
				current = current.children[i]
		current.end_of_word = True

	def search(self, word):
		current = self.root
		for i in word:
			if i in current.children:
				current = current.children[i]
			else:
				return False
		
		return current.end_of_word
	
	def remove(self, word):
		return self.removeAux(word, 0, self.root)

	def removeAux(self, word, index, current):
		if len(word) == index:
			if not current.end_of_word:
				return False
			current.end_of_word = False
			return len(current.children) == 0

		next_node = current.children[word[index]]
		if next_node == None:
			return False
		should_delete = self.removeAux(word, index + 1, next_node)
		if should_delete:
			del[current.children[word[index]]]
			return len(current.children) == 0
		return False