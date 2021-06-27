class StringDemo:
    ss = 'aaabbb'

    def stringFind(self):
        after = self.ss.replace('aa','a')
        print(self.ss.find('aa'))
        print(after)

if __name__ == '__main__' :
    stringDemo = StringDemo()
    stringDemo.stringFind()