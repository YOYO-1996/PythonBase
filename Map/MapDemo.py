class MapDemo:
    arrS = ['1', '2', '3', '4', '5']
    arr = [1, 2, 3, 4, 5]
    brr = [1, 2, 3, 4, 5]

    def mapInt(self):
        arrI = list(map(int, self.arrS))
        print(arrI)

    def mapSquare(self):
        arrSq = list(map(lambda x: x ** 2, self.arr))
        print(arrSq)

    def mapMultiVariable(self):
        arrSum = list(map(lambda x, y: x + y, self.arr, self.brr))
        print(arrSum)


if __name__ == '__main__':
    mapDemo = MapDemo()
    mapDemo.mapInt()
    mapDemo.mapSquare()
    mapDemo.mapMultiVariable()
