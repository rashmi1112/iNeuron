class print_name:
    def print_name(self, first_name, last_name):
        result = ''
        for i in reversed(first_name):
            result += i
        result += ' '
        for j in reversed(last_name):
            result += j
        print(result)


if __name__ == '__main__':
    first = input('Enter Your First Name: ')
    last = input('Enter Your Last Name: ')
    obj = print_name()
    obj.print_name(first, last)
