from stack import Stack

def dec_to_bin(number):
	'''Decimal to binary convertion'''
	
	s = Stack()
	
	while (number) >0 :
		s.push(number%2) # remainder
		number = number / 2 
	
	binary =''	
	while not s.is_empty() :
		binary = binary + str(s.pop())
	return binary

print dec_to_bin(145)
