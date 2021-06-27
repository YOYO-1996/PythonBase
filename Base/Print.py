class Print:

    def printSingel(self):
        print('Hello World!')

    # print多个，以空格间隔
    def printMulti(self):
        print('1', '2', '3')


if __name__ == '__main__':
    p = Print()
    p.printSingel()
    p.printMulti()
