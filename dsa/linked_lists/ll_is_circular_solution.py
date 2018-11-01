class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None


def cycle_check(node):
    a = b = node
    while b and b.nextnode:
        a = a.nextnode
        b = b.nextnode.nextnode
        if a is b:
            return True
    return False