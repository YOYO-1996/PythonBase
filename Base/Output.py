class Output:

    # 单个打印
    def printSingel(self):
        print('Hello World!')

    # print多个，以空格间隔
    def printMulti(self):
        print('1', '2', '3')

    # 使用%格式化打印
    def printPercent(self):
        name = 'tong'
        age = 25
        print('My name is %s, age is %d' % (name, age))

    # 使用string.format格式化打印
    def printFormat(self):
        name = 'tong'
        age = 25
        print('My name is {}, age is {}'.format(name, age))
        print('My name is {name}, age is {age}'.format(name='tt', age=25))


if __name__ == '__main__':
    p = Output()
    p.printSingel()
    p.printMulti()
    p.printPercent()
    p.printFormat()
