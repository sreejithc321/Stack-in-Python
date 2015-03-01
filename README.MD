# Stack

A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This ordering principle is called LIFO, last-in first-out.
The stack operations are given below.

- Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
- push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
- pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
- peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
- is_empty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
- size() returns the number of items on the stack. It needs no parameters and returns an integer.
  
### Implementing a Stack in Python 

- stack.py

### Solving the Balanced Parentheses Problem

Balanced parentheses means that each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested. 

- balanced_parantheses.py

### Converting Decimal Numbers to Binary Numbers

The function takes an argument that is a decimal number and repeatedly divides it by 2. 
Then extract the remainder and pushes it on the stack until the division process reaches 0.
The binary string is then returned.

- decimal_to_binary.py

### Infix, Prefix and Postfix Expressions

In infix the operator is in between the two operands that it is working on. eg : A + B * C .
In postfix, the expression would be A B C * + and + A * B C in prefix.

- infix_to_postfix.py : Converting Infix Expressions to Postfix Expressions 
- postfix_eval.py : Postfix Evaluation


