# balances parentheses check


def balance_check(s):
    
    # Check is even number of brackets
    if len(s)%2 != 0:
        return False
    
    # Set of opening brackets
    opening = set('([{') 
    
    # Matching Pairs
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    # Use a list as a "Stack"
    stack = []
    
    # Check every parenthesis in string
    for paren in s:
        
        # If its an opening, append it to list
        if paren in opening:
            stack.append(paren)
        
        else:
            
            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False
            
            # Check the last open parenthesis
            last_open = stack.pop()
            
            # Check if it has a closing match
            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0


# Implement a Queue - Using Two Stacks
# Uses lists instead of your own Stack class.

class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        
        # FILL OUT CODE HERE
        self.stack1.append(element)
    
    def dequeue(self):
        
        # FILL OUT CODE HERE
        if self.stack1 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        temp = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return temp