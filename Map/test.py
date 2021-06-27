class test:

    def getP(self):
        for i in range(0, 36):
            row = self.n - 1 - i // (self.n)
            if row & 1:
                col = i % self.n
            else:
                col = self.n - 1 - i % self.n
            print(i + 1, row, col)


if __name__ == '__main__':
    t = test()
    t.n = 6
    t.getP()
