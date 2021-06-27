class Input:
    def inputInt(self):
        # 括号中只是提示作用
        num = input(int)
        print(type(num))


if __name__ == '__main__':
    i = Input()
    i.inputInt()
