class print_nums:
    def print_nums(self, lower_bound, upper_bound):
        result = ''
        for i in range(lower_bound, upper_bound + 1):
            if i % 7 == 0 and i % 5 != 0:
                result += str(i) + ','
        print(result[:-1])


if __name__ == '__main__':
    lb = 2000
    ub = 3200
    obj = print_nums()
    obj.print_nums(lb, ub)
