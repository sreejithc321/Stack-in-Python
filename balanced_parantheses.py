from stack import Stack

def paratheses_checker(data) :
	'''Balanced parantheses checker function'''
	s = Stack()
	balanced = True
	index = 0
	while index < len(data) and balanced:
		symbol = data[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()
		index = index + 1
	
	# check if stack is empty and symbols are balanced
	if balanced and s.is_empty():
		return True
	else:
		return False

## Example	
print(paratheses_checker('((())))'))

