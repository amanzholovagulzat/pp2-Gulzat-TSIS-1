
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x , self.y)
    def move(self, x1,y1):
        newx = self.x + x1
        newy = self.y + y1
        print(newx ,newy)
    def dist(self,x2,y2):
        distx = x2 - self.x
        disty = y2 - self.y
        print ((distx**2 + disty**2)**0.5)

p1 = point(5,3)
p1.show()
p1.move(3,3)
p1.dist(8,7)


