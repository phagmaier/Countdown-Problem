import copy

class Node:
	def __init__(self, value):
		self.parent = None
		self.children = []
		self.string = ''
		self.value = None
		self.original = value
		self.used = {}



class Tree:
	def __init__(self, numbers, target):
		self.numbers = numbers
		self.results = []
		self.target = target
		#self.used = {k:v for k,v in zip(numbers, [False for i in range(len(numbers))])}
		self.root = None
		self.add = lambda x,y: x+y
		self.sub = lambda x,y: x-y if x>=y else None
		self.mul = lambda x,y: x*y 
		self.div = lambda x,y: x/y if x%y == 0 else None
		self.operations = {'+':self.add, '-': self.sub, '*': self.mul, '/': self.div}


	def insert(self, value, parent=None):
		if not self.root and parent is None:
			self.root = Node(value)
			self.root.string += str(value)
			self.root.original = value
			self.root.used = {k:v for k,v in zip(self.numbers, [False for i in range(len(self.numbers))])}
			self.root.used[value] = True
			self.root.value = value

		else:
			self._insert(value,parent)

	def _insert(self,value,parent):
		#self.new_vals = []
		for i in self.operations.keys():
			result = self.operations[i](parent.value,value)
			if result:
				if result == self.target:
					final = parent.string + i + str(value)
					self.results.append(final)
				else:
					temp = Node(result)
					temp.original = value
					temp.string = parent.string + i + str(value) 
					temp.value = result
					temp.used = copy.deepcopy(parent.used)
					temp.used[value] = True
					parent.children.append(temp)
					iterate = [i for i in temp.used.keys() if not temp.used[i]]
					for i in iterate:
						self._insert(i,temp)


#numbers = [5, 10, 20]
#numbers = [5, 10, 15,7]
#target = 35




def main(numbers=numbers, target=target):
	partial = []
	final = set()
	for i in numbers:
		tree = Tree(numbers,target)
		tree.insert(i)
		other = [num for num in numbers if num != i]
		for a in other:
			tree.insert(a,tree.root)
			partial += tree.results
	for part in partial:
		final.add(part)
	print(final)
	return final

#main()


