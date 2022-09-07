class Stack:

    def __init__(self, size):
        self.size = size
        self.data = [None]*size
        self.top = -1


    def push(self, value):
        if self.is_full()  :
            print('가득찼어')
            # raise 
        else:
            self.top += 1
            self.data[self.top] = value


    def pop(self):
        if self.is_empty():
            print('텅비었어')
        else:
            value = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return value


    def is_full(self):
        # 1
        # if self.size == self.top + 1:
        #     return True
        # else:
        #     return False
        # 2
        # return True if self.size == self.top + 1 else False
        # 3
        return (self.top + 1 == self.size)


    def is_empty(self):
        return (self.top == -1)


    def length(self):
        return self.top + 1


    def __str__(self):
        return f'{self.data}'

stack = Stack(3)
print(stack)

stack.push(1)
print(stack)

stack.push(2)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.push(1)
print(stack)

    