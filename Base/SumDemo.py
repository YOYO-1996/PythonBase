class SumDemo:
    arr = [1, 2, 3, 4, 5]
    arr2d = [[1, 2], [3, 4]]
    arr2dp1 = [1, 2]
    arr2dp2 = [3, 4]

    def sumCommon(self):
        print(sum(self.arr))
        # 计算arr再加start
        print(sum(self.arr, 1))

    def sumList(self):
        print(sum(self.arr2d, []))
        # 上面的sum操作相当于arr2d中每一行相加
        # -> 即每一行一维数组连接
        # 由于start默认值为0，所以start需改为一个空数组
        print(self.arr2dp1 + self.arr2dp2)


if __name__ == '__main__':
    sumDemo = SumDemo()
    sumDemo.sumCommon()
    sumDemo.sumList()
