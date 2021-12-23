from StackClass import Stack

dict_ballance = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def check(test_str):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(test_str) and balanced:
        symbol = test_str[index]
        if symbol in dict_ballance:
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                stack.pop()
        index = index + 1
    if balanced and stack.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    test_str = input('Введите строку для проверки:')
    if check(test_str) == True:
        print('Сбалансированны')
    else:
        print('Несбалансированны')
