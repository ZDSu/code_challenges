"""
Create a simple class, MaxSizeList, that acts a little bit like a list, with a pre-configured limit on its size. The integer argument passed to the constructor will determine the maximum size of the list being held by the MaxSizeList object.  So, what attributes will each instance have to have to support this behavior?
"""


class MaxSizeList:
    def __init__(self, max):
        self.list = []
        try:
            self.max_size = int(max)
        except ValueError:
            return

    def push(self, item):
        self.list.append(item)
        if len(self.list) > self.max_size:
            self.list.pop(0)

    def get_list(self):
        return self.list


# test it:
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('hey')
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())  # ['hi', "let's", 'go']
print(b.get_list())  # ['go']
