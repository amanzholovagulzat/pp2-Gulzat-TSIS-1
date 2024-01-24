class stroka():
    def __init__(self, stroka):
        self.stroka = stroka

    def getstring(self):
        print(self.stroka)

    def printString(self):
        b = self.stroka
        print(b.upper())
a = input()
slovo = stroka(a)
slovo.getstring()
slovo.printString()


        
        