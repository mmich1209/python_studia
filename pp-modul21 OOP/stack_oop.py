# class Stack: #definiowanie klasy stosu
#     def __init__(self):
#         self.stack_list = []
#
# stack_obj = Stack()
# stack_obj.stack_list.append(1)
# stack_obj.stack_list.append(1)
# print(len(stack_obj.stack_list))


# class Stack:  # definiowanie klasy stosu
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, item):
#         self.__stack_list.append(item)
#
#     def pop(self):
#         item = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return item
#
#
#
#
#
# stack_obj = Stack()
# stack_obj.push(3)
# stack_obj.push(2)
# stack_obj.push(1)
# print(stack_obj.pop())
# print(stack_obj.pop())
# print(stack_obj.pop())
#
# stack1 = Stack()
# stack2 = Stack()
#
# stack1.push(1)
# stack2.push("Ala")
# stack1.push(2)
# stack2.push("ma")
# stack1.push(3)
# stack2.push("kota")
#
# print()
#
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
#
# print()
#
# print(stack2.pop())
# print(stack2.pop())
# print(stack2.pop())



class Stack:  # definiowanie klasy stosu
    def __init__(self):
        self.__stack_list = []

    def push(self, item):
        self.__stack_list.append(item)

    def pop(self):
        item = self.__stack_list[-1]
        del self.__stack_list[-1]
        return item

    def empty(self):
        return (len(self.__stack_list) == 0)

    def size(self):
        return len(self.__stack_list)

    def top(self):
        return self.__stack_list[-1]

stack = Stack()
print("Jest pusttyy?", stack.empty())

stack.push("Ala")
stack.push("Tomek")

print("Jest pusttyy?", stack.empty())
print("Ile elementów?", stack.size())
print("Na samej górze?", stack.top())


# class StuckSum(Stack):
#     def getSum(self):
#         return sum(self._Stack__stack_list)


#
# stack = StuckSum()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.getSum())
# print(stack.pop())

