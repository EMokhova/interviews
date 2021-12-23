list1 = [1, 2, 3, 4, 5, 6, 7]


class Stack(list):

    def isEmpty(self):
        return len(self) == 0

    def push(self, new_elem):
        self.append(new_elem)

    def pop(self):
        if not self.isEmpty():
            item = self[-1]
            self.__delitem__(-1)
        return item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        z = len(self)
        return z


stack = Stack(list1)
print(stack.isEmpty())
print(stack.peek())
print(stack.size())
stack.push(3)
print(stack)
print(stack.pop())
