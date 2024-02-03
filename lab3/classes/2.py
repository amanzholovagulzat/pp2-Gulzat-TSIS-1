
class shape():
    def __init__(self):
        self.plosh = 0
    def area1 (self):
        print (self.plosh)

class square(shape):
    def __init__(self,a):
        self.a = a
    def area2(self):
        self.plosh = self.a * self.a 
        print(self.plosh)

kv = shape()
kv.area1()
kv2 = square(5)
kv2.area2()

