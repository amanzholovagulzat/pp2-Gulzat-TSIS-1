class rectangle(shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def area3(self):
        area = self.a * self.b
        print(area)

hhh = rectangle(3,4)
hhh.area3()

