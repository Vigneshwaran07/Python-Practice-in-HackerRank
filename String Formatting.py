def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(n))
    for i in range(1, number+1):
        print("{:{width}d} {:{width}o} {:{width}X} {:{width}b}".format(i,i,i,i,width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
