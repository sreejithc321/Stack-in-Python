class Stack :
	'''Python implementation the stack'''
	
	def __init__(self):
		self.items = []
	
	def is_empty(self):
		return self.items == []
		
	def push(self,item):
		self.items.append(item)		
		
	def pop(self):
		return self.items.pop()
		
	def peek(self):
		return self.items[len(self.items)-1]
	
	def size(self):
		return len(self.items)

## Sample inputs
if __name__ == '__main__':
	s=Stack()
	print(s.is_empty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print(s.size())
	print(s.is_empty())
	s.push(8.4)
	print(s.pop())
	print(s.pop())
	print(s.size())
